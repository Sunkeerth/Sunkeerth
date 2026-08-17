

# """
# SICK TiM320 Industrial Field Monitor
# ====================================

# Communication:
#     USB 2.0
#     CoLa-A
#     PyUSB

# Device:
#     SICK TiM320 / TiM32x
#     VID: 0x19A2
#     PID: 0x5001

# Current application:
#     Field evaluation monitoring

# Reads:
#     - Device identification
#     - Device state
#     - Active field set
#     - LIDoutputstate

# Decodes:
#     OUT1 / OUT2 / OUT3
#     Field 1 / Field 2 / Field 3

# IMPORTANT:
#     This software is a monitoring/integration interface.
#     Do NOT use Python/USB as the sole safety channel for
#     personnel protection or safety-rated robot stopping.
# """

# from __future__ import annotations

# import logging
# import signal
# import sys
# import time
# from dataclasses import dataclass
# from enum import Enum
# from typing import Optional

# import usb.core
# import usb.util


# # ============================================================
# # CONFIGURATION
# # ============================================================

# USB_VID = 0x19A2
# USB_PID = 0x5001

# USB_INTERFACE = 0

# USB_EP_OUT = 0x02
# USB_EP_IN = 0x81

# USB_WRITE_TIMEOUT_MS = 2000
# USB_READ_TIMEOUT_MS = 500

# COMMAND_TIMEOUT_S = 2.0

# POLL_PERIOD_S = 0.10

# MAX_USB_READ = 4096


# # ============================================================
# # LOGGING
# # ============================================================

# logging.basicConfig(
#     level=logging.INFO,
#     format=(
#         "%(asctime)s | "
#         "%(levelname)-8s | "
#         "%(message)s"
#     ),
# )

# logger = logging.getLogger("tim320")


# # ============================================================
# # ENUMS
# # ============================================================

# class DeviceState(Enum):

#     UNKNOWN = "UNKNOWN"
#     BUSY = "BUSY"
#     READY = "READY"
#     ERROR = "ERROR"


# class FieldState(Enum):

#     UNKNOWN = "UNKNOWN"
#     CLEAR = "ALL_FIELDS_CLEAR"
#     FIELD_3 = "FIELD_3_INFRINGED"
#     FIELD_2 = "FIELD_2_INFRINGED"
#     FIELD_1 = "FIELD_1_INFRINGED"
#     COMMUNICATION_ERROR = "COMMUNICATION_ERROR"


# # ============================================================
# # DATA STRUCTURES
# # ============================================================

# @dataclass
# class OutputState:

#     out1: int
#     out2: int
#     out3: int

#     out1_count: int
#     out2_count: int
#     out3_count: int


# @dataclass
# class Tim320Status:

#     timestamp: float

#     device_state: DeviceState

#     active_field_set: Optional[int]

#     output_state: Optional[OutputState]

#     field_state: FieldState


# # ============================================================
# # TIM320 DRIVER
# # ============================================================

# class Tim320:

#     def __init__(self) -> None:

#         self.device = None
#         self.interface_claimed = False

#         self._stop_requested = False

#     # --------------------------------------------------------
#     # FIND
#     # --------------------------------------------------------

#     def find(self) -> None:

#         logger.info(
#             "Searching for TiM320 "
#             "(VID=0x%04X PID=0x%04X)",
#             USB_VID,
#             USB_PID,
#         )

#         self.device = usb.core.find(
#             idVendor=USB_VID,
#             idProduct=USB_PID,
#         )

#         if self.device is None:

#             raise RuntimeError(
#                 "TiM320 not found. "
#                 "Check: lsusb -d 19a2:5001"
#             )

#         logger.info(
#             "TiM320 found"
#         )

#         logger.info(
#             "VID=0x%04X PID=0x%04X",
#             self.device.idVendor,
#             self.device.idProduct,
#         )

#     # --------------------------------------------------------
#     # OPEN
#     # --------------------------------------------------------

#     def open(self) -> None:

#         if self.device is None:

#             raise RuntimeError(
#                 "Device has not been found."
#             )

#         try:

#             if self.device.is_kernel_driver_active(
#                 USB_INTERFACE
#             ):

#                 logger.info(
#                     "Detaching kernel USB driver"
#                 )

#                 self.device.detach_kernel_driver(
#                     USB_INTERFACE
#                 )

#         except (NotImplementedError, usb.core.USBError):

#             pass

#         usb.util.claim_interface(
#             self.device,
#             USB_INTERFACE
#         )

#         self.interface_claimed = True

#         logger.info(
#             "USB interface %d claimed",
#             USB_INTERFACE,
#         )

#         self._validate_endpoints()

#     # --------------------------------------------------------
#     # VALIDATE ENDPOINTS
#     # --------------------------------------------------------

#     def _validate_endpoints(self) -> None:

#         configuration = (
#             self.device.get_active_configuration()
#         )

#         interface = configuration[
#             (USB_INTERFACE, 0)
#         ]

#         found_in = False
#         found_out = False

#         for endpoint in interface:

#             address = endpoint.bEndpointAddress

#             if address == USB_EP_IN:
#                 found_in = True

#             if address == USB_EP_OUT:
#                 found_out = True

#         if not found_in:

#             raise RuntimeError(
#                 f"USB IN endpoint 0x{USB_EP_IN:02X} "
#                 "not found"
#             )

#         if not found_out:

#             raise RuntimeError(
#                 f"USB OUT endpoint 0x{USB_EP_OUT:02X} "
#                 "not found"
#             )

#         logger.info(
#             "USB endpoints verified: "
#             "OUT=0x%02X IN=0x%02X",
#             USB_EP_OUT,
#             USB_EP_IN,
#         )

#     # --------------------------------------------------------
#     # FLUSH
#     # --------------------------------------------------------

#     def _flush_input(self) -> None:

#         if self.device is None:
#             return

#         while True:

#             try:

#                 self.device.read(
#                     USB_EP_IN,
#                     MAX_USB_READ,
#                     timeout=30,
#                 )

#             except usb.core.USBError:

#                 break

#     # --------------------------------------------------------
#     # BUILD COLA-A
#     # --------------------------------------------------------

#     @staticmethod
#     def _build_cola_a(
#         command: str,
#     ) -> bytes:

#         return (
#             b"\x02"
#             + command.encode("ascii")
#             + b"\x03"
#         )

#     # --------------------------------------------------------
#     # SEND COMMAND
#     # --------------------------------------------------------

#     def command(
#         self,
#         command: str,
#     ) -> str:

#         if self.device is None:

#             raise RuntimeError(
#                 "TiM320 is not connected"
#             )

#         telegram = self._build_cola_a(
#             command
#         )

#         self._flush_input()

#         logger.debug(
#             "TX: %s",
#             command,
#         )

#         try:

#             written = self.device.write(
#                 USB_EP_OUT,
#                 telegram,
#                 timeout=USB_WRITE_TIMEOUT_MS,
#             )

#         except usb.core.USBError as exc:

#             raise RuntimeError(
#                 f"USB write failed: {exc}"
#             ) from exc

#         if written != len(telegram):

#             raise RuntimeError(
#                 f"Short USB write: "
#                 f"{written}/{len(telegram)}"
#             )

#         response = bytearray()

#         deadline = (
#             time.monotonic()
#             + COMMAND_TIMEOUT_S
#         )

#         while time.monotonic() < deadline:

#             try:

#                 data = self.device.read(
#                     USB_EP_IN,
#                     MAX_USB_READ,
#                     timeout=USB_READ_TIMEOUT_MS,
#                 )

#                 response.extend(
#                     bytes(data)
#                 )

#                 # CoLa-A telegram terminates with ETX
#                 if 0x03 in response:

#                     break

#             except usb.core.USBError:

#                 continue

#         if not response:

#             raise TimeoutError(
#                 f"No response for command: "
#                 f"{command}"
#             )

#         try:

#             text = bytes(response).decode(
#                 "ascii",
#                 errors="strict",
#             )

#         except UnicodeDecodeError as exc:

#             raise RuntimeError(
#                 "TiM320 returned non-ASCII "
#                 "telegram"
#             ) from exc

#         text = text.strip(
#             "\x02\x03"
#         )

#         logger.debug(
#             "RX: %s",
#             text,
#         )

#         return text

#     # --------------------------------------------------------
#     # DEVICE IDENTIFICATION
#     # --------------------------------------------------------

#     def get_device_ident(self) -> str:

#         return self.command(
#             "sRN DeviceIdent"
#         )

#     # --------------------------------------------------------
#     # DEVICE STATE
#     # --------------------------------------------------------

#     def get_device_state(
#         self,
#     ) -> DeviceState:

#         response = self.command(
#             "sRN SCdevicestate"
#         )

#         parts = response.split()

#         if len(parts) < 3:

#             return DeviceState.UNKNOWN

#         try:

#             code = int(
#                 parts[2]
#             )

#         except ValueError:

#             return DeviceState.UNKNOWN

#         if code == 0:
#             return DeviceState.BUSY

#         if code == 1:
#             return DeviceState.READY

#         if code == 2:
#             return DeviceState.ERROR

#         return DeviceState.UNKNOWN

#     # --------------------------------------------------------
#     # ACTIVE FIELD SET
#     # --------------------------------------------------------

#     def get_active_field_set(
#         self,
#     ) -> Optional[int]:

#         response = self.command(
#             "sRN ActiveFieldSet"
#         )

#         parts = response.split()

#         if len(parts) < 3:
#             return None

#         try:

#             return int(
#                 parts[2]
#             )

#         except ValueError:

#             return None

#     # --------------------------------------------------------
#     # OUTPUT STATE
#     # --------------------------------------------------------

#     def get_output_state(
#         self,
#     ) -> OutputState:

#         response = self.command(
#             "sRN LIDoutputstate"
#         )

#         parts = response.split()

#         if len(parts) < 10:

#             raise RuntimeError(
#                 "Invalid LIDoutputstate telegram: "
#                 + response
#             )

#         if parts[0] != "sRA":

#             raise RuntimeError(
#                 "Unexpected response: "
#                 + response
#             )

#         if parts[1] != "LIDoutputstate":

#             raise RuntimeError(
#                 "Unexpected telegram: "
#                 + response
#             )

#         try:

#             return OutputState(

#                 out1=int(
#                     parts[4],
#                     16,
#                 ),

#                 out1_count=int(
#                     parts[5],
#                     16,
#                 ),

#                 out2=int(
#                     parts[6],
#                     16,
#                 ),

#                 out2_count=int(
#                     parts[7],
#                     16,
#                 ),

#                 out3=int(
#                     parts[8],
#                     16,
#                 ),

#                 out3_count=int(
#                     parts[9],
#                     16,
#                 ),
#             )

#         except ValueError as exc:

#             raise RuntimeError(
#                 "Could not decode "
#                 "LIDoutputstate: "
#                 + response
#             ) from exc

#     # --------------------------------------------------------
#     # FIELD DECODER
#     # --------------------------------------------------------

#     @staticmethod
#     def determine_field(
#         outputs: OutputState,
#     ) -> FieldState:

#         o1 = outputs.out1
#         o2 = outputs.out2
#         o3 = outputs.out3

#         if (
#             o1 == 0
#             and o2 == 0
#             and o3 == 0
#         ):

#             return FieldState.CLEAR

#         if (
#             o1 == 0
#             and o2 == 0
#             and o3 == 1
#         ):

#             return FieldState.FIELD_3

#         if (
#             o1 == 0
#             and o2 == 1
#             and o3 == 1
#         ):

#             return FieldState.FIELD_2

#         if (
#             o1 == 1
#             and o2 == 1
#             and o3 == 1
#         ):

#             return FieldState.FIELD_1

#         return FieldState.UNKNOWN

#     # --------------------------------------------------------
#     # COMPLETE STATUS
#     # --------------------------------------------------------

#     def read_status(self) -> Tim320Status:

#         state = self.get_device_state()

#         field_set = (
#             self.get_active_field_set()
#         )

#         outputs = (
#             self.get_output_state()
#         )

#         field = self.determine_field(
#             outputs
#         )

#         return Tim320Status(

#             timestamp=time.time(),

#             device_state=state,

#             active_field_set=field_set,

#             output_state=outputs,

#             field_state=field,
#         )

#     # --------------------------------------------------------
#     # CLOSE
#     # --------------------------------------------------------

#     def close(self) -> None:

#         if self.device is None:
#             return

#         if self.interface_claimed:

#             try:

#                 usb.util.release_interface(
#                     self.device,
#                     USB_INTERFACE,
#                 )

#             except usb.core.USBError:

#                 pass

#             self.interface_claimed = False

#         usb.util.dispose_resources(
#             self.device
#         )

#         logger.info(
#             "USB resources released"
#         )


# # ============================================================
# # APPLICATION
# # ============================================================

# class Tim320Application:

#     def __init__(self):

#         self.sensor = Tim320()

#         self.last_field = None

#         self.last_device_state = None

#         self.last_field_set = None

#         self.running = True

#     # --------------------------------------------------------
#     # SIGNAL HANDLER
#     # --------------------------------------------------------

#     def stop(self, *_args):

#         logger.info(
#             "Shutdown requested"
#         )

#         self.running = False

#     # --------------------------------------------------------
#     # PRINT HEADER
#     # --------------------------------------------------------

#     @staticmethod
#     def print_header():

#         print()
#         print("=" * 78)
#         print("SICK TiM320 INDUSTRIAL FIELD MONITOR")
#         print("=" * 78)

#     # --------------------------------------------------------
#     # PRINT STATUS
#     # --------------------------------------------------------

#     def print_status(
#         self,
#         status: Tim320Status,
#     ):

#         outputs = status.output_state

#         self.print_header()

#         print(
#             f"Timestamp        : "
#             f"{time.strftime('%Y-%m-%d %H:%M:%S')}"
#         )

#         print(
#             f"Device state     : "
#             f"{status.device_state.value}"
#         )

#         print(
#             f"Active field set : "
#             f"{status.active_field_set}"
#         )

#         if outputs:

#             print()

#             print(
#                 f"OUT1             : "
#                 f"{outputs.out1} "
#                 f"(count={outputs.out1_count})"
#             )

#             print(
#                 f"OUT2             : "
#                 f"{outputs.out2} "
#                 f"(count={outputs.out2_count})"
#             )

#             print(
#                 f"OUT3             : "
#                 f"{outputs.out3} "
#                 f"(count={outputs.out3_count})"
#             )

#         print()

#         print(
#             f"FIELD STATE      : "
#             f"{status.field_state.value}"
#         )

#         print("=" * 78)

#     # --------------------------------------------------------
#     # EVENT
#     # --------------------------------------------------------

#     def report_event(
#         self,
#         status: Tim320Status,
#     ):

#         new_field = status.field_state.value

#         if new_field != self.last_field:

#             logger.info(
#                 "FIELD EVENT: %s",
#                 new_field,
#             )

#             self.last_field = new_field

#         if (
#             status.device_state.value
#             != self.last_device_state
#         ):

#             logger.info(
#                 "DEVICE STATE EVENT: %s",
#                 status.device_state.value,
#             )

#             self.last_device_state = (
#                 status.device_state.value
#             )

#         if (
#             status.active_field_set
#             != self.last_field_set
#         ):

#             logger.info(
#                 "FIELD SET EVENT: %s",
#                 status.active_field_set,
#             )

#             self.last_field_set = (
#                 status.active_field_set
#             )

#     # --------------------------------------------------------
#     # RUN
#     # --------------------------------------------------------

#     def run(self):

#         signal.signal(
#             signal.SIGINT,
#             self.stop,
#         )

#         signal.signal(
#             signal.SIGTERM,
#             self.stop,
#         )

#         try:

#             self.sensor.find()

#             self.sensor.open()

#             ident = (
#                 self.sensor.get_device_ident()
#             )

#             logger.info(
#                 "Device: %s",
#                 ident,
#             )

#             while self.running:

#                 try:

#                     status = (
#                         self.sensor.read_status()
#                     )

#                     self.report_event(
#                         status
#                     )

#                     self.print_status(
#                         status
#                     )

#                     time.sleep(
#                         POLL_PERIOD_S
#                     )

#                 except (
#                     usb.core.USBError,
#                     TimeoutError,
#                     RuntimeError,
#                 ) as exc:

#                     logger.error(
#                         "Communication error: %s",
#                         exc,
#                     )

#                     if not self.running:
#                         break

#                     logger.warning(
#                         "Attempting USB recovery..."
#                     )

#                     self.sensor.close()

#                     time.sleep(1.0)

#                     try:

#                         self.sensor.find()

#                         self.sensor.open()

#                         logger.info(
#                             "USB recovery successful"
#                         )

#                     except Exception as reconnect_error:

#                         logger.error(
#                             "USB recovery failed: %s",
#                             reconnect_error,
#                         )

#                         time.sleep(2.0)

#         finally:

#             self.sensor.close()

#             print()
#             print(
#                 "TiM320 monitor stopped."
#             )


# # ============================================================
# # ENTRY POINT
# # ============================================================

# def main():

#     application = (
#         Tim320Application()
#     )

#     try:

#         application.run()

#     except KeyboardInterrupt:

#         pass

#     except Exception as exc:

#         logger.critical(
#             "Fatal error: %s",
#             exc,
#         )

#         sys.exit(1)


# if __name__ == "__main__":

#     main()

from __future__ import annotations

import logging
import signal
import sys
import time
from dataclasses import dataclass
from enum import Enum
from typing import Optional

import usb.core
import usb.util

VID = 0x19A2
PID = 0x5001
INTERFACE = 0
EP_OUT = 0x02
EP_IN = 0x81
WRITE_TIMEOUT_MS = 1000
READ_TIMEOUT_MS = 100
COMMAND_TIMEOUT_S = 0.5
HEALTH_PERIOD_S = 1.0
MAX_READ = 4096

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d | %(levelname)-8s | %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("tim320")


class DeviceState(Enum):
    UNKNOWN = "UNKNOWN"
    BUSY = "BUSY"
    READY = "READY"
    ERROR = "ERROR"


class FieldState(Enum):
    UNKNOWN = "UNKNOWN"
    CLEAR = "ALL_FIELDS_CLEAR"
    FIELD_3 = "FIELD_3_INFRINGED"
    FIELD_2 = "FIELD_2_INFRINGED"
    FIELD_1 = "FIELD_1_INFRINGED"


class Trigger(Enum):
    UNKNOWN = "UNKNOWN"
    NORMAL = "NORMAL_OPERATION"
    WARNING = "WARNING_ZONE"
    SLOW = "SLOW_DOWN"
    STOP = "STOP_REQUEST"


@dataclass(frozen=True)
class OutputState:
    out1: int
    out2: int
    out3: int
    out1_count: int
    out2_count: int
    out3_count: int


@dataclass(frozen=True)
class Status:
    timestamp: float
    device_state: DeviceState
    field_set: Optional[int]
    outputs: OutputState
    field: FieldState
    trigger: Trigger


class Tim320:
    def __init__(self) -> None:
        self.dev = None
        self.claimed = False

    def connect(self) -> None:
        self.dev = usb.core.find(idVendor=VID, idProduct=PID)
        if self.dev is None:
            raise RuntimeError("TiM320 not found. Check: lsusb -d 19a2:5001")

        try:
            if self.dev.is_kernel_driver_active(INTERFACE):
                self.dev.detach_kernel_driver(INTERFACE)
        except (NotImplementedError, usb.core.USBError):
            pass

        usb.util.claim_interface(self.dev, INTERFACE)
        self.claimed = True

        cfg = self.dev.get_active_configuration()
        iface = cfg[(INTERFACE, 0)]
        addresses = {ep.bEndpointAddress for ep in iface}
        if EP_IN not in addresses or EP_OUT not in addresses:
            raise RuntimeError(
                f"Expected endpoints OUT=0x{EP_OUT:02X}, IN=0x{EP_IN:02X}; "
                f"found {[hex(x) for x in addresses]}"
            )

        log.info("TiM320 connected: VID=0x%04X PID=0x%04X", VID, PID)
        log.info("USB interface %d claimed; OUT=0x%02X IN=0x%02X", INTERFACE, EP_OUT, EP_IN)

    def _flush(self) -> None:
        if self.dev is None:
            return
        while True:
            try:
                self.dev.read(EP_IN, MAX_READ, timeout=10)
            except usb.core.USBError:
                return

    @staticmethod
    def _cola_a(command: str) -> bytes:
        return b"\x02" + command.encode("ascii") + b"\x03"

    def command(self, command: str) -> str:
        if self.dev is None:
            raise RuntimeError("TiM320 is not connected")

        self._flush()
        packet = self._cola_a(command)
        written = self.dev.write(EP_OUT, packet, timeout=WRITE_TIMEOUT_MS)
        if written != len(packet):
            raise RuntimeError(f"Short USB write: {written}/{len(packet)}")

        rx = bytearray()
        deadline = time.monotonic() + COMMAND_TIMEOUT_S
        while time.monotonic() < deadline:
            try:
                rx.extend(bytes(self.dev.read(EP_IN, MAX_READ, timeout=READ_TIMEOUT_MS)))
                if 0x03 in rx:
                    break
            except usb.core.USBError:
                continue

        if not rx:
            raise TimeoutError(f"No response to {command}")

        # CoLa-A telegram is ASCII between STX and ETX.
        try:
            text = bytes(rx).decode("ascii", errors="strict").strip("\x02\x03")
        except UnicodeDecodeError as exc:
            raise RuntimeError("Non-ASCII TiM320 telegram") from exc

        return text

    def device_ident(self) -> str:
        return self.command("sRN DeviceIdent")

    def device_state(self) -> DeviceState:
        parts = self.command("sRN SCdevicestate").split()
        if len(parts) < 3:
            return DeviceState.UNKNOWN
        try:
            code = int(parts[2])
        except ValueError:
            return DeviceState.UNKNOWN
        return {0: DeviceState.BUSY, 1: DeviceState.READY, 2: DeviceState.ERROR}.get(
            code, DeviceState.UNKNOWN
        )

    def active_field_set(self) -> Optional[int]:
        parts = self.command("sRN ActiveFieldSet").split()
        if len(parts) < 3:
            return None
        try:
            return int(parts[2])
        except ValueError:
            return None

    def output_state(self) -> OutputState:
        text = self.command("sRN LIDoutputstate")
        parts = text.split()
        if len(parts) < 10 or parts[0] != "sRA" or parts[1] != "LIDoutputstate":
            raise RuntimeError(f"Invalid LIDoutputstate: {text}")
        try:
            return OutputState(
                out1=int(parts[4], 16), out1_count=int(parts[5], 16),
                out2=int(parts[6], 16), out2_count=int(parts[7], 16),
                out3=int(parts[8], 16), out3_count=int(parts[9], 16),
            )
        except ValueError as exc:
            raise RuntimeError(f"Cannot decode LIDoutputstate: {text}") from exc

    @staticmethod
    def field_from_outputs(o: OutputState) -> FieldState:
        pattern = (o.out1, o.out2, o.out3)
        return {
            (0, 0, 0): FieldState.CLEAR,
            (0, 0, 1): FieldState.FIELD_3,
            (0, 1, 1): FieldState.FIELD_2,
            (1, 1, 1): FieldState.FIELD_1,
        }.get(pattern, FieldState.UNKNOWN)

    @staticmethod
    def trigger_from_field(field: FieldState) -> Trigger:
        return {
            FieldState.CLEAR: Trigger.NORMAL,
            FieldState.FIELD_3: Trigger.WARNING,
            FieldState.FIELD_2: Trigger.SLOW,
            FieldState.FIELD_1: Trigger.STOP,
        }.get(field, Trigger.UNKNOWN)

    def close(self) -> None:
        if self.dev is None:
            return
        if self.claimed:
            try:
                usb.util.release_interface(self.dev, INTERFACE)
            except usb.core.USBError:
                pass
            self.claimed = False
        usb.util.dispose_resources(self.dev)
        self.dev = None
        log.info("USB resources released")


class Application:
    def __init__(self) -> None:
        self.sensor = Tim320()
        self.running = True
        self.last_field: Optional[FieldState] = None
        self.last_trigger: Optional[Trigger] = None
        self.state = DeviceState.UNKNOWN
        self.field_set: Optional[int] = None

    def stop(self, *_args) -> None:
        self.running = False

    def trigger(self, trigger: Trigger) -> None:
        # Replace these integration points with your ROS2/PLC/robot API.
        # They are deliberately transition-based: one event per field change.
        if trigger == Trigger.STOP:
            log.critical("TRIGGER: STOP ROBOT")
        elif trigger == Trigger.SLOW:
            log.warning("TRIGGER: SLOW DOWN ROBOT")
        elif trigger == Trigger.WARNING:
            log.warning("TRIGGER: WARNING ZONE")
        elif trigger == Trigger.NORMAL:
            log.info("TRIGGER: NORMAL OPERATION")
        else:
            log.error("TRIGGER: UNKNOWN")

    def print_event(self, status: Status) -> None:
        o = status.outputs
        print("\n" + "=" * 78)
        print("SICK TiM320 DETECTION EVENT")
        print("=" * 78)
        print(f"Time             : {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Device state     : {status.device_state.value}")
        print(f"Active field set : {status.field_set}")
        print(f"OUT1             : {o.out1}")
        print(f"OUT2             : {o.out2}")
        print(f"OUT3             : {o.out3}")
        print(f"Detection        : {status.field.value}")
        print(f"TRIGGER          : {status.trigger.value}")
        print("=" * 78)

    def run(self) -> None:
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

        try:
            self.sensor.connect()
            log.info("Device: %s", self.sensor.device_ident())

            # Slow-changing information: cache it.
            self.state = self.sensor.device_state()
            self.field_set = self.sensor.active_field_set()
            log.info("Initial state=%s field_set=%s", self.state.value, self.field_set)

            next_health = time.monotonic() + HEALTH_PERIOD_S

            while self.running:
                try:
                    now = time.monotonic()

                    if now >= next_health:
                        self.state = self.sensor.device_state()
                        self.field_set = self.sensor.active_field_set()
                        next_health = now + HEALTH_PERIOD_S

                    # ---------------- HOT PATH ----------------
                    # Only one command/response transaction here.
                    outputs = self.sensor.output_state()
                    field = self.sensor.field_from_outputs(outputs)
                    trigger = self.sensor.trigger_from_field(field)

                    status = Status(
                        timestamp=time.time(),
                        device_state=self.state,
                        field_set=self.field_set,
                        outputs=outputs,
                        field=field,
                        trigger=trigger,
                    )

                    # Trigger only when detection state changes.
                    if field != self.last_field:
                        self.trigger(trigger)
                        self.print_event(status)
                        self.last_field = field
                        self.last_trigger = trigger

                except (usb.core.USBError, TimeoutError, RuntimeError) as exc:
                    log.error("Communication error: %s", exc)
                    if not self.running:
                        break
                    # Reconnect outside the normal detection path.
                    self.sensor.close()
                    time.sleep(0.25)
                    try:
                        self.sensor.connect()
                        self.state = self.sensor.device_state()
                        self.field_set = self.sensor.active_field_set()
                        next_health = time.monotonic() + HEALTH_PERIOD_S
                        log.info("USB recovery successful")
                    except Exception as recovery_exc:
                        log.error("USB recovery failed: %s", recovery_exc)
                        time.sleep(1.0)

        finally:
            self.sensor.close()
            print("TiM320 monitor stopped.")


def main() -> None:
    app = Application()
    try:
        app.run()
    except Exception as exc:
        log.critical("Fatal error: %s", exc)
        sys.exit(1)


if __name__ == "__main__":
    main()