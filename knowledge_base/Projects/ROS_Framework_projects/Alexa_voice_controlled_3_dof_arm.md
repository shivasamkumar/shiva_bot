# 3-DOF Robot Arm with Voice Control from Alexa

## Introduction
This project implements a three-degree-of-freedom robotic arm that can execute hands-free pick-and-place operations in simulation by interpreting Amazon Alexa voice commands such as “pick,” “place,” and “home.” A Flask-Ask–based Python web service handles Alexa intents and forwards structured commands to ROS 2 Humble nodes, which use MoveIt for collision-aware trajectory planning and Gazebo for realistic physics simulation of the digital twin. The same commands are transmitted via USB serial (using `pyserial` and `libserial-dev`) to an Arduino microcontroller that actuates three servos corresponding to the arm’s base, shoulder, and elbow joints. The URDF model mirrors the physical arm, enabling thorough testing and parameter tuning in RViz before any hardware deployment, and the modular architecture supports keyboard or RViz GUI teleoperation as well as future extensions.   

## Procedure
1. **Environment Setup & Installation**  
   - Install Ubuntu 22.04 LTS, ROS 2 Humble, Gazebo, and required ROS 2 control packages (`ros-humble-ros2-control`, controllers, `xacro`, `ros-gz-*`, `joint-state-publisher-gui`, `tf-transformations`, MoveIt).  
   - Install Python packages for Alexa integration: `flask-ask-sdk`, `ask-sdk`, `pyserial`, and `python3-transforms3d`.  
   - Install `libserial-dev` for Arduino–ROS 2 serial communication.   

2. **Alexa Voice Interface**  
   - Define Alexa intents using Flask-Ask that map spoken commands to ROS 2 service calls.  
   - Relay motion commands via `pyserial` over USB to an Arduino microcontroller running low-level servo controllers.   

3. **Trajectory Planning & Execution**  
   - Configure MoveIt for the 3-DOF arm’s URDF and joint limits.  
   - Implement ROS 2 action clients to send pick-and-place goals to MoveIt and monitor execution feedback.  
   - Validate and visualize planned trajectories in RViz and Gazebo before execution.  

4. **GUI & Manual Control**  
   - Provide keyboard teleoperation via ROS 2 topics for direct joint control.  
   - Display planned paths and robot state in RViz for interactive trajectory adjustments.  

## Challenges Faced
- **Voice-Command Reliability**  
  Ensuring consistent mapping of varied spoken phrases to Alexa intents required careful intent-slot design and extensive local testing of Flask-Ask handlers.  
- **Serial Communication Robustness**  
  Maintaining reliable, bidirectional USB serial communication between the ROS 2 node and Arduino demanded retry logic and error handling to prevent dropped commands.  
- **Simulation-to-Hardware Consistency**  
  Tuning controller gains and MoveIt planning parameters so Gazebo behaviors matched real-world expectations involved iterative parameter sweeps and detailed visualization in RViz.  

## Contributions
_All work was performed solely by Shiva Sam Kumar Govindan._  
- Designed the ROS 2 package structure and URDF model for the 3-DOF arm.  
- Implemented the Flask-Ask Alexa skill and integrated it with ROS 2 service and action servers.  
- Configured MoveIt trajectory planning and authored launch files to bring up Gazebo, MoveIt, and voice-control nodes.  
- Developed Python serial-communication handlers for interfacing with the Arduino controller.  

## Results
- Demonstrated successful pick-and-place operations in Gazebo driven entirely by Alexa voice commands, with trajectories planned and visualized in MoveIt.  
- Validated manual teleoperation via keyboard and RViz, confirming the system’s adaptability for interactive control and future expansion to physical hardware.   
