# Robot Car: IMU Sensors and Extended Kalman Filter
## Introduction
This repository implements an autonomous ground vehicle (AGV) platform using ROS 2 Humble on Ubuntu 22.04 that integrates a differential-drive controller with an Extended Kalman Filter (EKF) based on the package for robust sensor fusion of IMU and wheel-odometry data :contentReference. A separate node runs a linear Kalman filter to facilitate comparative benchmarking of fusion algorithms. The AGV’s mechanical and kinematic model is defined via a URDF and simulated in Gazebo, creating a digital twin that allows developers to test vehicle dynamics, characterize sensor noise, and observe filter convergence under realistic conditions. Real-time data streams—including raw odometry, IMU measurements, and EKF outputs—are visualized in PlotJuggler with a custom JSON layout, enabling rapid tuning of process and measurement noise covariances and validation of state-estimation performance. The launch system uses ROS 2 launch files with parameters to toggle between simple differential-drive control and EKF-driven commands, and supports teleoperation via keyboard or joystick. Built on standard ROS interfaces and leveraging serial communication abstractions, this architecture can be deployed unchanged to hardware platforms such as a Raspberry Pi connected to motor controllers for real-world AGV applications. 


## Challenges Faced
- **Sensor Noise & Drift**  
  Tuning EKF process and measurement noise covariance matrices to balance responsiveness against robustness under noisy IMU data required extensive trial-and-error and empirical validation.  
- **Digital Twin Fidelity**  
  Ensuring Gazebo dynamics accurately reflected real differential-drive behavior mandated careful tuning of friction, inertia, and motor-controller parameters.  
- **Software–Hardware Integration**  
  Structuring serial communication between ROS 2 nodes and an Arduino-based motor controller demanded robust error handling to prevent command loss during hardware deployment.

## Contributions
All aspects of this project—from ROS 2 launch-file design and differential-drive controller setup, through EKF and linear-KF node implementations, to Gazebo world creation and PlotJuggler configuration—were developed and authored solely by Shiva Sam Kumar Govindan.

## Results
- Achieved accurate pose estimation in simulation, with the EKF effectively filtering IMU noise and maintaining state-estimation error within acceptable bounds for autonomous navigation.  
- Demonstrated modularity by toggling between EKF-driven control and a simple diffusion controller, verifying robustness of both frameworks.  
- Produced comprehensive demo videos and Gazebo snapshots showcasing filter convergence and reliable differential-drive behavior, paving the way for future hardware integration.  
