<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=32&duration=3000&pause=500&color=36BCF7&center=true&vCenter=true&width=700&lines=Sunkeerth+Y;AI+%26+Robotics+R%26D+Engineer;Agentic+AI+%7C+Embodied+AI;Sensor-Level+Multi-Agent+Systems" alt="Typing SVG" />
</div>

<div align="center">
  <a href="mailto:sunkeerthaiml.bitm@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://www.linkedin.com/in/sunkeerth-y">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://github.com/Sunkeerth">
    <img src="https://img.shields.io/github/followers/Sunkeerth?label=Followers&style=for-the-badge&color=0e75b6&logo=github" alt="GitHub followers" />
  </a>
</div>

<br/>

## 👨‍🔬 About Me

I'm an **AI & Robotics R&D Engineer** working at the intersection of **Agentic AI**, **Embodied Robotics**, and **Digital Twins**. After completing my B.Tech in AI & ML (CGPA 8.06/10), I moved from academic research into applied R&D — building systems that don't just predict, but *perceive, reason, and act* in the physical world.

My current focus is **sensor-level multi-agent architectures for autonomous mobile robots (AMRs)** — where each sensor (lidar, camera, IMU, actuators) runs its own lightweight agent, and a coordinating arbitrator fuses their proposals into a single action, rather than relying on one monolithic policy.

- 🔭 **Current R&D:** Hybrid **Imitation Learning + Reinforcement Learning** framework for AMR navigation — teleoperated demonstrations feed IL, RL rewards refine it, and the same behavior generalizes to full autonomy.
- 🧩 **Architecture focus:** Per-sensor ROS 2 agent nodes (3D lidar, 2D lidar × 2, 3D camera, 6-axis IMU, actuators/steering) coordinated by a central arbitration agent.
- 🌱 **Exploring:** Agentic AI system design, VLA (Vision-Language-Action) pipelines, OpenUSD/NVIDIA Warp digital twins, and edge-device optimization.
- 🏆 **Milestones:** National finalist, NIDAR Drone Competition (top 12 of 300+ teams — autonomous agricultural navigation).
- 🤝 **Open to:** R&D collaborations, robotics/agentic-AI research roles, and open-source contributions.

---

## 🛠️ Technical Arsenal

| **Domain** | **Technologies & Frameworks** |
|---|---|
| **Agentic AI** | LangChain, multi-agent orchestration, arbitration/coordinator design, retry & memory logic, RAG, LLMs (GPT, Phi‑3, LLaMA) |
| **Robotics & Simulation** | ROS 2 (Humble), Gazebo, RViz2, Nav2, Behavior Trees, ros2_control, OpenUSD, NVIDIA Warp, Sensor Fusion |
| **Learning Systems** | Imitation Learning (IL), Reinforcement Learning (RL), hybrid IL+RL pipelines, PyTorch, TensorFlow |
| **Perception / CV** | YOLOv8, CLIP, Transformers, FAISS, multimodal reasoning (VLA/VLM pipelines) |
| **Embedded / Edge AI** | ESP32, ESP8266, ESP‑NOW, UART telemetry, TensorFlow Lite, Embedded C, servo control (Panasonic MINAS A6) |
| **Languages & Infra** | Python, C++, JavaScript, SQL, AWS (EC2/Lambda), Docker, Git, Linux, MLOps |

---

## 🔬 Featured R&D Projects

### 🤖 Sensor-Level Multi-Agent Framework for AMR (Hybrid IL + RL) — *In Progress*
A new architecture for autonomous mobile robots where each sensor modality runs its own agent instead of feeding one central policy.
* **Sensor suite:** 3D lidar, dual 2D lidars (left/rear), 3D camera, 6-axis IMU, actuators & steering.
* **Design:** Each sensor agent proposes an action from its own local context; a coordinating arbitrator resolves conflicting proposals into the final command.
* **Learning loop:** Manual teleoperation data is structured and stored for IL; RL rewards are forwarded back into the IL store so the system "remembers" full sensor context, letting autonomous behavior converge toward demonstrated driving.
* **Platform:** Prototyping on an AGV forklift vehicle, simulated in Gazebo + RViz — targeted as the basis for a research paper.

### 🧠 Embodied AI: Vision-Language-Action Robotics System
> **[View Repository](https://github.com/Sunkeerth/Vision-Language-Action-Based-Robotic-Navigation-System-with-Multimodal-Transformer-Reasoning)**

An end‑to‑end VLA pipeline enabling a robot to perceive its environment, understand natural language instructions, and execute complex autonomous tasks.
* **Architecture:** YOLOv8 (Detection) + CLIP (Relational Understanding) → LangChain (Orchestration) → Phi-3 (Reasoning) → ROS2 Nav2 (Execution).
* **Innovation:** Persistent memory module for state tracking and dynamic failure re-planning in Gazebo environments.

<div align="center">
  <a href="https://drive.google.com/file/d/13vN3dY9bAXRFbN5lKrTCaJZLXe9vyfb6/view?usp=drive_link" target="_blank">
    <img src="https://img.shields.io/badge/▶️_Watch_VLA_Demo-4285F4?style=for-the-badge&logo=googledrive&logoColor=white" alt="Open in Google Drive" />
  </a>
</div>

<br/>

### 🎙️ Agentic AI: Multi-Agent Audio Dubbing System
A multi-agent pipeline for automated audio dubbing, orchestrating ASR, translation/reasoning, and speech synthesis agents with retry and memory logic.
* **Architecture:** Whisper (ASR) → Groq LLaMA (reasoning/translation) → edge-tts (synthesis), with a Gradio front end.
* **Innovation:** Agent-level retry and memory handling for robustness against pipeline failures; run end-to-end in Google Colab.

<br/>

### 🚁 Autonomous Swarm: Drone Communication & Agriculture System
> **[View Research Demo](https://www.linkedin.com/posts/sunkeerth-ab14b3337_nidar-dronetechnology-bitm-ugcPost-7424705466426941440-QX82)**

A resilient, low-latency communication mesh for autonomous agricultural scanning and spraying drones.
* **Architecture:** ESP32/ESP8266 using ESP-NOW and UART for real-time telemetry.
* **Innovation:** Custom lightweight packet protocol with ACKs, retries, and sequence numbers — 100% data integrity over a 90×90m field radius.

<div align="center">
  <a href="https://drive.google.com/drive/folders/1gpgImszF6rsuyoYargwEqgUpb2M51p9N?usp=drive_link" target="_blank">
    <img src="https://img.shields.io/badge/▶️_Watch_Drone_Demo-4285F4?style=for-the-badge&logo=googledrive&logoColor=white" alt="Open in Google Drive" />
  </a>
</div>

<br/>

### 🏭 Digital Twins: Industrial Robotic Spray Simulation
> **[View Repository](https://github.com/Sunkeerth/Simulated-Paint-Spraying-on-a-Wall-Mesh-with-Isaac-Warp-and-OpenUSD)**

A GPU-accelerated simulation of an industrial robotic spray-coating process — a foundational digital twin for manufacturing optimization.
* **Architecture:** NVIDIA Warp + OpenUSD for scene description.
* **Innovation:** Real-time physics modeling of spray density, nozzle pressure, and dynamic fluid interactions.

<div align="center">
  <a href="https://drive.google.com/file/d/1YuEfcAn7geeOS4lUxMUSKe_vZmqinJQd/view?usp=drive_link" target="_blank">
    <img src="https://img.shields.io/badge/▶️_Watch_Simulation_Demo-4285F4?style=for-the-badge&logo=googledrive&logoColor=white" alt="Open in Google Drive" />
  </a>
</div>

<br/>

### 🚗 Edge Computing: AI Overtake Safety System
> **[View Research Output](https://www.linkedin.com/posts/sunkeerth-ab14b3337_roadsafety-embeddedai-smarttransportation-ugcPost-7407277010462420993-20JD)**

An optimized deep learning model deployed directly onto micro-controllers for real-time vehicular safety analysis.
* **Architecture:** ESP32-CAM running TensorFlow Lite models natively in Embedded C.
* **Innovation:** High-accuracy, low-latency vehicle detection under strict hardware constraints to assist safe overtaking.

<div align="center">
  <a href="https://drive.google.com/file/d/1Kz3dT7vVK9Jzer1csSB3vP8FhpN61bkW/view?usp=drive_link" target="_blank">
    <img src="https://img.shields.io/badge/▶️_Watch_Edge_AI_Demo-4285F4?style=for-the-badge&logo=googledrive&logoColor=white" alt="Watch Demo" />
  </a>
</div>

---

## 💼 Experience & Engagements

* **AI & Robotics R&D Engineer** — building agentic, sensor-driven autonomy systems (current)
* **Data Science & Analytics Intern** @ *Amdox* (Mar 2026 – May 2026)
  *Developed predictive ML models and scalable behavior-analysis pipelines.*
* **Future Founder Intern** @ *Ascender Foundation* (Jul 2025 – Sep 2025)
  *Architected LLM-based automation prototypes using LangChain and advanced prompt engineering.*
* **2nd Place Winner** @ *Inter-College Hackathon*
  *Built an AI-Assisted Telemedicine Kiosk combining NLP, Speech-to-Text, and hardware interfaces.*

---

## 📈 GitHub Analytics

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Sunkeerth&show_icons=true&theme=radical&hide_border=true&bg_color=0D1117" alt="GitHub Stats" width="48%" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=Sunkeerth&theme=radical&hide_border=true&background=0D1117" alt="GitHub Streak" width="48%" />
</div>

<br/>

<div align="center">
  <img src="https://raw.githubusercontent.com/trinib/trinib/82213791fa9ff58d3ca768ddd6de2489ec23ffca/images/footer.svg" width="100%" />
</div>

