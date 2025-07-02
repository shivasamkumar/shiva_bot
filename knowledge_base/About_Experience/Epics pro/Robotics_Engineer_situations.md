# EPICS Pro – Knowledge Base Scenarios

**Employer:** EPICS Pro, Arizona State University  
**Client:** Rainier Labs, IT core Foundation 
**Title:** Robotics Engineer
**Duration:** July 2024 – July 2025  

Below are general “if you ask” scenarios capturing how Shiva tackled key robotics challenges at EPICS Pro. Use these to quickly explain “how X was done.”

---

## Sub-Centimeter AGV Localization  
**Context:** The AGV’s localization error exceeded 10 cm RMSE, insufficient for precision tasks.  
**Resolution:** Shiva integrated a LiDAR + vision SLAM stack and tuned sensor parameters to feed an ROS 2-based localization pipeline.  
**Outcome:** Achieved under 5 cm RMSE, enabling centimeter-scale waypoint following.

---

## Digital-Twin-Driven Path-Planning Optimization  
**Context:** Real-world AGV testing was costly and slow.  
**Resolution:** Shiva created a digital twin in NVIDIA Isaac Sim, replicating the vehicle’s kinematics and sensor noise. He iterated path-planning algorithms offline to reduce computational overhead.  
**Outcome:** Reduced live testing costs by 40% and cut trajectory-computation latency by 30% in production.

---

## Automated Robotic-Arm Palletizing  
**Context:** Manual palletizing with ABB IRB 2600s was slow and error-prone.  
**Resolution:** Shiva programmed the arms via ROS-Industrial and MoveIt, integrated EtherCAT with Beckhoff PLCs, and wrote pick-and-place routines.  
**Outcome:** Cycle times dropped by 25%, boosting throughput and consistency.

---

## Smooth Motion for Voice-Controlled Manipulation  
**Context:** Voice-activated pick-and-place suffered from jerky trajectories and low success rates.  
**Resolution:** Shiva tuned CHOMP and STOMP planners, smoothing trajectory profiles and adding dynamic collision checks in MoveIt.  
**Outcome:** Reduced motion jerk by 30%, increased grasp success by 30%, and cut execution time by 25%.

---

## High-Throughput Vision & Chat Integration  
**Context:** Field surveys needed rapid disease detection plus agronomic advice.  
**Resolution:** Shiva deployed a YOLO v12 detector on the rover for 25 FPS inference, then wrapped detections in a LangChain RAG pipeline with GPT API calls.  
**Outcome:** Achieved 98% detection accuracy, cut survey time by 60%, and sustained 99.9% chat-app uptime.

---

## Efficient UAV-Frame Prototyping  
**Context:** Off-the-shelf UAV frames were too heavy for long-duration missions.  
**Resolution:** Shiva prototyped carbon-fiber PETG frames on an Ultimaker S5, validated designs in CATIA V5 and Ansys for 5G-load tolerance.  
**Outcome:** Frame weight dropped by 25% without compromising structural integrity.

---

## Autonomous UAV Mapping & Localization  
**Context:** The VTOL drone lacked reliable onboard mapping for surveillance.  
**Resolution:** Shiva integrated ORB-SLAM and fused IMU + camera data in ROS 2/Gazebo, streaming real-time maps to the ground station.  
**Outcome:** Enabled robust in-flight mapping and accurate pose estimation in unknown environments.

---

## GPS-Denied Swarm Coordination  
**Context:** Hexacopter swarm tasks failed in GPS-denied areas.  
**Resolution:** Shiva ported PX4 firmware to ROS 2, implemented MAVLink-based swarm protocols, and incorporated onboard SLAM for relative positioning.  
**Outcome:** Achieved 95% mission success in GPS-denied agricultural monitoring flights.

---
## Scenario: Robot Dog Collapse & Torso Redesign  
**Context:** During a live demo to an investor consultant, the quadruped robot dog collapsed due to erratic reinforcement-learning (RL) behavior. Shiva was on site as the nearest engineer.  
**Resolution:**  
1. **Algorithmic Issue:** Shiva identified that the RL reward function lacked a penalty for excessive torso tilt, causing unstable gait policies under real-world disturbances.  
2. **Collaboration:** He informed the RL team of the bug so they could adjust the reward shaping and stability constraints.  
3. **Mechanical Fix:** Meanwhile, Shiva redesigned the dog’s torso structure to withstand higher dynamic loads, performed stress-point analysis, and ran ANSYS static and fatigue simulations under varied gait scenarios.  
4. **Deployment Prep:** While the RL team prepared the updated policy, Shiva secured a temporary leash-and-walker rig to prevent further damage.  
**Outcome:** Within two weeks, the new torso passed simulation validation, the RL team deployed a stable gait, and the demo to the consultant succeeded without incident—highlighting the team’s rapid response and interdisciplinary coordination.

---

## Scenario: Environment Understanding & 4D Database Pipeline  
**Context:** A project required the robot dog to autonomously map and understand its surroundings by reconstructing a 3D environment from two synchronized video streams.  
**Resolution:**  
1. **3D Reconstruction:** Shiva integrated COLMAP for stereo-video processing to generate dense point clouds and mesh models of the environment.  
2. **Feature Matching:** He extracted SIFT features from each frame, built a feature dataset, and matched them across adjacent images to produce a JSON mapping of frame correspondences.  
3. **Pose Extraction & Trajectory Plotting:** Camera poses were computed, timestamped, and exported as JSON; Shiva plotted the robot’s path over the reconstructed map.  
4. **4D Semantic Database:** He extended the pipeline to invoke multimodal models—custom object detectors, CLIP, and an LLM (and later PaLiGemma 2 in v2)—to tag objects per scene, producing a time-indexed JSON “4D” database.  
5. **Web App Development:** Shiva built a Gradio-style web interface that ingests the COLMAP output ZIP and supports two modes:  
   - **Surveillance:** Clicking on frame pairs displays semantic descriptions.  
   - **Chatbot:** Users ask questions about the scene via GPT-powered Q&A.  
6. **Manager-Requested Pivot:** To expedite funding demos, the manager requested replacing the multimodal pipeline with a direct GPT API integration. Shiva prototyped the GPT-only approach, integrated it into the existing web app, and delivered a streamlined demo.  
**Outcome:** The completed pipeline and web app demonstrated 3D mapping, semantic indexing, and interactive Q&A—securing initial project funding and laying groundwork for the full multimodal solution.




