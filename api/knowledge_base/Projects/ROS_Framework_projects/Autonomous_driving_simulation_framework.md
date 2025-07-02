# Self-Driving Car Project

## Introduction
This Self-Driving Car Project demonstrates autonomous driving capabilities across two simulation environments: the main ROS 2/Gazebo branch for real-time vehicle‐dynamics testing and the Carla Simulator branch implemented in Python for high-fidelity urban scenario evaluation. The system integrates several core modules—lane tracking using centerline detection, static and dynamic obstacle avoidance via circle-based collision checking, and a state-machine behavioral planner that manages transitions between lane following, stop-sign approach and halt, and resume behaviors. Path generation is accomplished with spiral-path functions and objective-function–based path selection, while the velocity profile generator adapts speed commands to scenario constraints. Additionally, the project incorporates semantic-segmentation neural-network outputs to refine drivable-space and lane estimation and to filter object-detection errors for precise obstacle-distance measurements, enabling robust and efficient autonomous navigation across both platforms. 


## Procedure
1. **Environment Setup & Launch**  
   - Main branch: install ROS 2 and Gazebo, build with `colcon`, source the workspace, and launch `world_gazebo.launch.py`.  
   - Carla branch: start the CARLA server (`CarlaUE4.exe … –carla-server`) and run `module_7.py` for Python-based testing.  
2. **Lane Tracking Module**  
   - Implemented lane-detection algorithms to follow road centerlines within Gazebo and CARLA.  
3. **Obstacle Avoidance**  
   - Developed static and dynamic obstacle handlers using circle-based collision checking (`collision_check()`) and dynamic updates for moving objects.  
4. **Behavioral Planning**  
   - Designed a state machine to manage transitions between lane following, deceleration on stop-sign approach, full stop, and lane-resume behaviors.  
5. **Path Generation & Selection**  
   - Generated candidate trajectories via spiral-path functions (`get_goal_state_set()`, `thetaf()`, `optimize_spiral()`, `sample_spiral()`).  
   - Selected the optimal path by evaluating an objective function balancing safety and centerline alignment.  
6. **Velocity Profile Computation**  
   - Computed scenario-aware speed profiles (`compute_velocity_profile()`) to handle stop signs, dynamic obstacles, and maintain lane speed.  
7. **Semantic Segmentation Integration**  
   - Fused neural-network segmentation outputs to refine drivable-space and lane estimates and filter 2D object-detection errors for accurate obstacle distances.  
8. **Simulation Testing & Validation**  
   - Ran end-to-end tests in both Gazebo and CARLA, capturing demo screenshots and videos to verify autonomous behaviors. 

## Challenges Faced
- Synchronizing ROS 2/Gazebo and Python/CARLA workflows, including coordinate-frame alignment and launch configurations.  
- Achieving robust lane tracking under varied simulated road geometries and lighting conditions.  
- Ensuring reliable static and dynamic obstacle avoidance with efficient, real-time collision checks.  
- Tuning spiral-path generation and objective-function parameters to balance path optimality and safety.  
- Integrating semantic segmentation outputs and filtering detection errors for precise obstacle-distance estimates.  
- Maintaining real-time performance in both simulation environments under compute constraints. 
## Contributions
All development—environment setup, ROS 2/Gazebo and CARLA configuration, lane-tracking, obstacle-avoidance, behavioral-planning modules, spiral-path generation, collision checking, velocity profiling, semantic-segmentation integration, and demo capture—was performed by Shiva Sam Kumar Govindan. 

## Results
- Demonstrated accurate lane following, dynamic and static obstacle avoidance, and stop-sign handling in ROS 2/Gazebo.  
- Validated autonomous behaviors in CARLA, including spiral path execution and dynamic obstacle negotiation.  
- Improved drivable-space and lane estimation via semantic-segmentation integration, reducing object-detection errors.  
- Produced demo screenshots and video showcasing system capabilities in both simulation platforms.
