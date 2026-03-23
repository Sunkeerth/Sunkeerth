<!--- Modern, 3D‑inspired GitHub Profile README for Sunkeerth --->

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Inter&weight=700&duration=3000&pause=500&color=F7F7F7&center=true&vCenter=true&width=900&height=100&lines=Embedded+AI+%7C+ROS2+%7C+XR+Simulations;Building+real‑world+systems+that+save+lives" alt="Typing SVG" />
</div>

<!-- Social badges with hover effects -->
<p align="center">
  <a href="https://www.linkedin.com/in/sunkeerth-ab14b3337/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://sunkeerth.github.io/" target="_blank">
    <img src="https://img.shields.io/badge/Portfolio-111111?style=for-the-badge&logo=vercel&logoColor=white" />
  </a>
  <a href="mailto:sunkeerthaiml.bitm@gmail.com">
    <img src="https://img.shields.io/badge/Email-EB4335?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
  <img src="https://komarev.com/ghpvc/?username=Sunkeerth&style=for-the-badge&label=Profile+views" />
</p>

<!-- CSS for 3D card effect, gradient backgrounds, and animations -->
<style>
  /* Smooth scrolling and gradient background */
  body {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    color: #f0f0f0;
    margin: 0;
    padding: 0;
  }
  .project-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 1.8rem;
    margin: 2rem 0;
  }
  .project-card {
    background: rgba(20, 20, 40, 0.7);
    backdrop-filter: blur(12px);
    border-radius: 1.5rem;
    padding: 1.2rem;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
  }
  .project-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 30px -10px rgba(0,0,0,0.4);
    border-color: rgba(100,150,255,0.5);
  }
  .project-video {
    width: 100%;
    border-radius: 1rem;
    margin-bottom: 0.8rem;
    background: #000;
  }
  .project-title {
    font-size: 1.3rem;
    font-weight: 600;
    margin: 0.5rem 0;
    background: linear-gradient(135deg, #fff, #aaccff);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }
  .project-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin: 0.8rem 0;
  }
  .tech-badge {
    background: rgba(255,255,255,0.1);
    padding: 0.2rem 0.6rem;
    border-radius: 20px;
    font-size: 0.7rem;
    font-weight: 500;
  }
  .project-links a {
    color: #88aaff;
    text-decoration: none;
    margin-right: 1rem;
    font-size: 0.9rem;
  }
  .project-links a:hover {
    text-decoration: underline;
  }
  .skills-section {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
    margin: 2rem 0;
  }
  .skill-category {
    background: rgba(0,0,0,0.4);
    border-radius: 2rem;
    padding: 0.8rem 1.2rem;
    border-left: 3px solid #3b82f6;
  }
  .achievement-timeline {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin: 1.5rem 0;
  }
  .achievement-item {
    background: rgba(255,255,255,0.05);
    border-radius: 1rem;
    padding: 0.8rem 1.2rem;
    display: flex;
    align-items: center;
    gap: 1rem;
  }
  .achievement-icon {
    font-size: 1.8rem;
  }
  hr {
    border: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, #3b82f6, transparent);
    margin: 2rem 0;
  }
</style>

---

## 🧠 **About Me**

I build **intelligent systems** at the intersection of perception, autonomy, and real‑world impact.  
My expertise spans:

- **Embedded AI** – TensorFlow Lite on edge, real‑time detection, sensor fusion.
- **Robotics & Simulation** – ROS2, Gazebo, Nav2, digital twins, industrial automation.
- **XR/VR/MR** – Unity, immersive learning environments, spatial computing.
- **IoT & Drones** – ESP32, telemetry, autonomous navigation, drone systems.

> 🚀 **Currently:** Prototyping a **Vision‑Language‑Action (VLA)** system for autonomous navigation and road safety.

---

## 🔥 **Featured Projects** *(click to play videos)*

<div class="project-grid">

  <!-- Project 1: Embedded AI Blind Spot Detection -->
  <div class="project-card">
    <video class="project-video" controls poster="https://via.placeholder.com/640x360?text=Blind+Spot+Demo">
      <source src="https://drive.google.com/uc?export=download&id=1Kz3dT7vVK9Jzer1csSB3vP8FhpN61bkW" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <div class="project-title">Embedded AI Blind Spot Detection</div>
    <div class="project-tech">
      <span class="tech-badge">ESP32-CAM</span>
      <span class="tech-badge">TensorFlow Lite</span>
      <span class="tech-badge">Ultrasonic</span>
    </div>
    <div class="project-links">
      <a href="https://github.com/Sunkeerth/Embedded-AI-Blind-Spot-Detection">📂 Repo</a>
      <a href="https://drive.google.com/file/d/1Kz3dT7vVK9Jzer1csSB3vP8FhpN61bkW/view">📄 PDF Report</a>
    </div>
  </div>

  <!-- Project 2: Autonomous Drone System -->
  <div class="project-card">
    <video class="project-video" controls poster="https://via.placeholder.com/640x360?text=Drone+Flight">
      <source src="https://drive.google.com/uc?export=download&id=1Kz3dT7vVK9Jzer1csSB3vP8FhpN61bkW" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <div class="project-title">Autonomous Drone System</div>
    <div class="project-tech">
      <span class="tech-badge">ESP32</span>
      <span class="tech-badge">ESP‑NOW</span>
      <span class="tech-badge">GPS</span>
      <span class="tech-badge">UART</span>
    </div>
    <div class="project-links">
      <a href="https://github.com/Sunkeerth/Autonomous-Drone-System">📂 Repo</a>
      <a href="https://drive.google.com/drive/folders/1gpgImszF6rsuyoYargwEqgUpb2M51p9N">🎥 Demo Videos</a>
    </div>
  </div>

  <!-- Project 3: AI‑Powered VLA Robotics -->
  <div class="project-card">
    <video class="project-video" controls poster="https://via.placeholder.com/640x360?text=VLA+Robot">
      <source src="https://drive.google.com/uc?export=download&id=YOUR_VIDEO_ID" type="video/mp4">
    </video>
    <div class="project-title">AI‑Powered VLA Robotics</div>
    <div class="project-tech">
      <span class="tech-badge">ROS2</span>
      <span class="tech-badge">YOLOv8</span>
      <span class="tech-badge">LangChain</span>
      <span class="tech-badge">Gazebo</span>
    </div>
    <div class="project-links">
      <a href="https://github.com/Sunkeerth/AI-Powered-Vision-Language-Action-Robotics-System">📂 Repo</a>
    </div>
  </div>

  <!-- Project 4: RAGC Virtual University -->
  <div class="project-card">
    <video class="project-video" controls poster="https://via.placeholder.com/640x360?text=VR+University">
      <source src="https://drive.google.com/uc?export=download&id=YOUR_VIDEO_ID" type="video/mp4">
    </video>
    <div class="project-title">RAGC Virtual University</div>
    <div class="project-tech">
      <span class="tech-badge">Unity</span>
      <span class="tech-badge">WebXR</span>
      <span class="tech-badge">React</span>
      <span class="tech-badge">Node.js</span>
    </div>
    <div class="project-links">
      <a href="https://github.com/Sunkeerth/RAGC-Virtual-university-">📂 Repo</a>
    </div>
  </div>

  <!-- Project 5: Industrial Robotic Spray Simulation -->
  <div class="project-card">
    <video class="project-video" controls poster="https://via.placeholder.com/640x360?text=Spray+Sim">
      <source src="https://drive.google.com/uc?export=download&id=YOUR_VIDEO_ID" type="video/mp4">
    </video>
    <div class="project-title">Industrial Robotic Spray Simulation</div>
    <div class="project-tech">
      <span class="tech-badge">NVIDIA Warp</span>
      <span class="tech-badge">OpenUSD</span>
      <span class="tech-badge">Python</span>
    </div>
    <div class="project-links">
      <a href="https://github.com/Sunkeerth/Industrial-Robotic-Spray-Simulation">📂 Repo</a>
    </div>
  </div>

  <!-- Project 6: AI‑Assisted Telemedicine Kiosk -->
  <div class="project-card">
    <video class="project-video" controls poster="https://via.placeholder.com/640x360?text=Telemedicine">
      <source src="https://drive.google.com/uc?export=download&id=YOUR_VIDEO_ID" type="video/mp4">
    </video>
    <div class="project-title">AI‑Assisted Telemedicine Kiosk</div>
    <div class="project-tech">
      <span class="tech-badge">Node.js</span>
      <span class="tech-badge">Express</span>
      <span class="tech-badge">Speech‑to‑Text</span>
    </div>
    <div class="project-links">
      <a href="https://github.com/Sunkeerth/MINI_PROJECT_KISOK">📂 Repo</a>
    </div>
  </div>

</div>

---

## 🧰 **Skills Snapshot**

<div class="skills-section">
  <div class="skill-category">🤖 Embedded AI: ESP32‑CAM · TensorFlow Lite · Ultrasonic</div>
  <div class="skill-category">🚀 Robotics: ROS2 · Gazebo · Nav2 · Sensor Fusion</div>
  <div class="skill-category">🥽 XR/VR/AR: Unity · XR Toolkit · WebXR · Blender</div>
  <div class="skill-category">🧠 AI/ML: PyTorch · YOLOv8 · LangChain · OpenCV</div>
  <div class="skill-category">🛸 IoT & Drones: ESP‑NOW · GPS · Telemetry · C++</div>
  <div class="skill-category">☁️ Cloud & Tools: AWS · Docker · Git · Linux</div>
</div>

---

## 🏆 **Achievements**

<div class="achievement-timeline">
  <div class="achievement-item">
    <div class="achievement-icon">🥈</div>
    <div><strong>2nd Place, Inter‑College Hackathon</strong><br/>AI Telemedicine Kiosk for Rural India</div>
  </div>
  <div class="achievement-item">
    <div class="achievement-icon">🚁</div>
    <div><strong>NIDAR Drone Competition Finalist</strong><br/>National‑level drone challenge (PR1 & PR2 missions)</div>
  </div>
  <div class="achievement-item">
    <div class="achievement-icon">🚛</div>
    <div><strong>Embedded AI Road Safety</strong><br/>Blind‑spot detection system for Indian trucks (field‑test ready)</div>
  </div>
  <div class="achievement-item">
    <div class="achievement-icon">📜</div>
    <div><strong>Certifications</strong><br/>Google GenAI · AWS Cloud Practitioner · Python Programming · Unity XR (in progress)</div>
  </div>
</div>

---

## 📊 **GitHub Stats**

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Sunkeerth&show_icons=true&theme=radical&hide_border=true" width="48%" />
  <img src="https://streak-stats.demolab.com/?user=Sunkeerth&theme=radical&hide_border=true" width="48%" />
</p>

---

## 🤝 **Let’s Connect**

I'm open to collaborations in **embedded AI, robotics, road safety, and XR for education**.

<div align="center">
  <a href="mailto:sunkeerthaiml.bitm@gmail.com">📧 sunkeerthaiml.bitm@gmail.com</a> &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="https://sunkeerth.github.io/">🌐 Portfolio</a> &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/sunkeerth-ab14b3337/">🔗 LinkedIn</a>
</div>

<hr/>

<div align="center">
  <i>“Building intelligent systems that bridge the physical and virtual worlds — one truck, one drone, one student at a time.”</i>
</div>
