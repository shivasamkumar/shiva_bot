# Shiva Sam Kumar Govindan  
**Robotics Engineer**  

Wichita, Kansas  
shivasamkumarg@gmail.com — +1 (602) 921-8754  
[LinkedIn](https://www.linkedin.com/in/shiva-sam-kumar/) — [GitHub](https://github.com/shivasamkumar) — [Portfolio](https://shivasamkumar.github.io)  

## Summary  
I am a robotics engineer with over three years of hands-on experience in developing autonomous systems, industrial automation, and UAV technologies. I hold an MS in Robotics and Autonomous Systems from Arizona State University and a B.Tech in Aeronautical Engineering, which have provided me with a strong foundation in mechanical systems (Design and Analysis), control theory, visual perception, and real-time computing. My expertise spans digital twin simulations, sensor fusion, and AI-driven perception and environment understanding, and I am passionate about advancing autonomous navigation, sensor fusion, multi-robot communication and coordination techniques through research. :contentReference[oaicite:22]{index=22}

## Research Interests  
- Autonomous Navigation & Motion Planning  
- Multi-Robot Coordination & Distributed Control  
- Advanced Control Systems & Nonlinear Optimization  
- Visual Perception & Decision-Making in Robotics  
- Reinforcement Learning for Adaptive Control :contentReference[oaicite:23]{index=23}

## Skills  
- **Programming Languages:** Python, C++, MATLAB, SQL, LaTeX  
- **Robotics Frameworks:** ROS2, MoveIt, Nav2, OMPL, STOMP, GTSAM, PX4 Autopilot, MAVLink, FreeRTOS, ROS-I  
- **Perception & AI:** OpenCV, TensorFlow, PyTorch, Kalibr, scikit-learn, PCL, LOAM, RTAB-Map  
- **Simulation & Modeling:** Gazebo, CARLA, Blender, AWS RoboMaker, Siemens NX  
- **Embedded Systems & IoT:** STM32, Raspberry Pi, NVIDIA Jetson, TMC2209, Socket CAN, EtherCAT, Beckhoff PLCs  
- **Mechanical Design & Analysis Tools:** 3D Printing, CATIA V5, SolidWorks, Ansys, HyperMesh :contentReference[oaicite:24]{index=24}

## Education  
**Arizona State University**, Tempe, AZ  
– Master of Science in Robotics and Autonomous Systems (GPA: 3.63/4.00)  
Aug 2022 – May 2024 :contentReference[oaicite:25]{index=25}  

**Vel Tech Rangarajan Dr. Sagunthala R&D Institute of Science & Technology**, Chennai, India  
– Bachelor of Technology in Aeronautical Engineering  
Aug 2016 – May 2020 :contentReference[oaicite:26]{index=26}

## Professional Experience  

### Epics pro, Arizona state University  
**Robotics Engineer**, jul 2024 – Present  
- Developed and implemented optimized control software for ABB IRB 2600 robotic arms using ROS-I and MoveIt, integrating EtherCAT to streamline operations and reduce cycle time by 25%.  
- Deployed a perception & simulation framework by creating a Kalman filter in ROS2 to fuse LiDAR and RealSense data—achieving 97% obstacle detection accuracy—and built a digital twin in NVIDIA Isaac Sim for AGV path planning, cutting real-world testing costs by 40%.  
- Tuned CHOMP and STOMP planners for 7-DOF manipulators, boosting grasp success by 30% and reducing motion jerk by 30%, enhancing manipulation precision.  
- Implemented visual-language architectures combining large language models and CNNs for enhanced decision-making on live camera feeds. :contentReference[oaicite:27]{index=27}
- Designed carbon-fiber PETG UAV frames, achieving a 25% weight reduction and validating structural integrity via Ansys simulations.  
- Processed LiDAR with PCL and deployed LOAM on NVIDIA Xavier NX for real-time 3D terrain reconstruction.  
- Built an autonomous UAV pipeline integrating ORB-SLAM and sensor fusion in ROS2, using Python and OpenCV for live image processing.  
- Ran AWS RoboMaker swarm simulations (50+ UAVs), reducing cloud compute costs by 35% and achieving 95% coordination success. :contentReference[oaicite:28]{index=28}

### Launch Trax Private Limited, Bangalore, India  
**Robotics Application Engineer**, Feb 2020 – Jul 2022  
- Processed LiDAR DEMs with GRASS GIS and GDAL, automating flood-risk mapping using Python and scikit-learn clustering for disaster-response missions.  
- Deployed an OpenVINO-optimized YOLOv5 on Intel NUC and developed a CANopen stack on Raspberry Pi 4 for real-time UAV payload communication with Pixhawk.  
- Streamlined geo-spatial workflows via Python, PostgreSQL, and GeoServer to render 10 000:1 scale aeronautical charts—reducing clutter by 50% and improving interpretability by 30%.  
- Crafted C++ trajectory planners to cut UAV fuel consumption by 22% on long-range missions; wrote Python + OpenCV/GDAL routines to boost navigational accuracy by 40%. :contentReference[oaicite:29]{index=29}

## Projects  

### Autonomous Guided Vehicles: Lane Tracking, Obstacle Avoidance & Behavioral Planning (2024)  
**Skills:** ROS2, Python, Sensor Fusion, State Machine Design, Dynamic Velocity Profiling, Semantic Segmentation  
- Architected a dual-simulation framework using ROS2/Gazebo and CARLA for behavioral planning—handling lane tracking, deceleration, stopping, and resumption with obstacle avoidance.  
- Developed a spiral-trajectory module with custom functions and circle-based collision detection for safety.  
- Computed adaptive velocity profiles for varying traffic/environmental conditions.  
- Integrated semantic segmentation to refine drivable-space estimation and improve 2D detection filtering via sensor fusion. :contentReference[oaicite:30]{index=30}

### Autonomous UAV Surveillance System (2024)  
**Skills:** UAV Design, ORB-SLAM, Sensor Fusion, Real-Time Image Processing, MPC, Photogrammetry, Georeferencing (GDAL), Python, OpenCV, ROS2  
- Designed a UAV platform with ORB-SLAM and live image processing, plus a georeferencing pipeline converting image to global frames via Python/OpenCV/GDAL.  
- Built an MPC framework coupled with SLAM localization for precise trajectory tracking in dynamic conditions.  
- Applied photogrammetry to map 2D images to real-world coordinates using camera intrinsics/extrinsics and geospatial transforms. :contentReference[oaicite:31]{index=31}

### Advanced Robot Car Localization & Mapping: Adaptive MCL, SLAM & Twist Mux Control (2024)  
**Skills:** ROS2, SLAM, Nav Stack, Lifecycle Management, Python, Sensor Fusion, Voxel Mapping  
- Created a localization framework combining Adaptive Monte Carlo Localization with SLAM for high-resolution voxel maps.  
- Deployed ROS2 Nav Stack and Twist Mux for priority-based velocity commands and joystick teleop.  
- Developed a detailed URDF and integrated wheel odometry + LiDAR for fidelity.  
- Leveraged ROS2 Lifecycle Nodes for seamless mode transitions. :contentReference[oaicite:32]{index=32}

### Advanced 3-D Multi-Object Detection: PointPillars & TANet (2024)  
**Skills:** LiDAR Processing, 3D Detection, KITTI & nuScenes, Preprocessing, Hyperparameter Tuning, Loss Optimization  
- Integrated PointPillars and TANet on KITTI/nuScenes, encoding LiDAR for spatial feature extraction.  
- Tuned hyperparameters and loss functions for accuracy and robustness.  
- Built a preprocessing pipeline to structure LiDAR data, accelerating inference.  
- Deployed evaluation using mAP & IoU metrics. :contentReference[oaicite:33]{index=33}

### 3-DOF Robotic Arm: Voice-Controlled Trajectory & Simulation (2023)  
**Skills:** Kinematics, Newton-Euler Dynamics, LQR, Kalman Filtering, ROS2, HIL, MoveIt  
- Simulated a 3-DOF arm in MATLAB with forward/inverse kinematics and dynamic modeling.  
- Developed LQR + Kalman filters for stability and transient response.  
- Integrated MoveIt for collision-free planning; added Flask/Alexa voice control for hands-free pick-and-place. :contentReference[oaicite:34]{index=34}

### Collaborative Multi-Robot Warehouse Navigation: DARP & A* (2023)  
**Skills:** Multi-Robot Coordination, Auction-Based Path Planning, Client-Server Architecture, Real-Time Task Allocation, Python, ROS  
- Built a client-server system to coordinate e-puck robots in a warehouse, validated in Webots.  
- Combined DARP with A* for dynamic shortest-path planning—improving efficiency by 30% and reducing navigation errors by 40%.  
- Modeled kinematics via cyclic coordinate descent for area division and path planning. :contentReference[oaicite:35]{index=35}

### Optimal MPC for Autonomous Vehicle Trajectory Tracking (2023)  
**Skills:** Bicycle Model, LPV-MPC, Nonlinear Dynamics, QP Optimization, Python, CARLA, Control Design  
- Developed a nonlinear bicycle model for trajectory planning and steering control.  
- Designed an LPV-MPC framework handling dynamic constraints in state-space.  
- Optimized QP cost function to under 5% tracking error.  
- Validated via 3D CARLA animations and extended to UAV trajectory tracking. :contentReference[oaicite:36]{index=36}

## Publications, Conferences & Hackathons  
- **Design and Optimization of Lug Bracket Assembly**, *Bulletin of INCAS*, Vol. 13, Issue 1. [View Publication](https://bulletin.incas.ro/files/gowtham__shiva-sam-kumar__aasa-dara__vol_13_iss_1.pdf)  
  Presented an FEA-based topology and shape optimization framework for a lightweight lug bracket assembly, reducing stress and weight. :contentReference[oaicite:37]{index=37}  

- **Design & Analysis of Aluminium Matrix Composite Spur Gear**, *Advances in Materials and Processing*. [DOI Link](https://www.tandfonline.com/doi/full/10.1080/2374068X.2020.1814983)  
  Developed a fly ash–reinforced aluminium composite spur gear, enhancing load-bearing performance and reducing weight. :contentReference[oaicite:38]{index=38}  

- **Design And Analysis Of Aluminum Matrix Composite Piston**, *IOP Conference Series: Materials Science* [ICDAC:2020]  
  Performed thermal and structural analysis of an A2024 alloy piston reinforced with fly ash, demonstrating improved resilience. :contentReference[oaicite:39]{index=39}  

- **Ropal: Robot Assistant**, Developed during a 3-day hackathon. [View Project](https://devpost.com/software/ropal-u4y8ej)  
  Built a real-time IoT-connected autonomous assistant with sensor fusion and advanced control. :contentReference[oaicite:40]{index=40}  

## Related Coursework  

**Master’s Courses**  
- EGR 598: Machine Learning and A.I.  
- MAE 547: Modeling and Control of Robots  
- EGR 546: Robotic Systems II  
- MFG 598: Engineering Computing with Python  
- MAE 506: Systems Modeling, Dynamics, and Control  
- MAE 598: Multi-Robot Systems  
- CSE 598: Perception in Robotics :contentReference[oaicite:41]{index=41}  

**Bachelor’s Courses**  
- MA 104: Transforms & Partial Differential Equations  
- AE 213: Numerical Methods using MATLAB  
- AE 106: Linear System Analysis and Control  
- AE 215: Aircraft Structural Mechanics  
- AE 109: Airplane Performance  
- AE 112: Aircraft Stability and Control  
- AE 246: Aircraft Component Design :contentReference[oaicite:42]{index=42}  
