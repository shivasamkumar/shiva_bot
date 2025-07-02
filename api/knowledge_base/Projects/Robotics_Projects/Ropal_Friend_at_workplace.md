# RoPal – Your Friend at the Workplace

## Introduction
- Workplace stress is at alarming rates due to global events such as the war between Russia and Ukraine, the COVID-19 pandemic, and rising prices, contributing to psychological and physiological disorders. 
- RoPal autonomously detects stress in office employees through real-time facial emotion recognition using an integrated webcam, navigates to the stressed individual’s desk, and sprays essential oils for aromatherapy-based stress relief. 
- Developed in a 48-hour Robotech 2023 Hackathon at Georgia Tech University by a five-member interdisciplinary team, RoPal leverages expertise in robotics, computer vision, and hardware prototyping. 
- The system employs an ESP32 camera module for facial capture, a MobileNet-based deep learning model running on a host PC, and a ROS 2-controlled differential-drive robot equipped with a 4-DoF servo arm for precise aromatherapy delivery. 

## Procedure
1. **Emotion Detection**  
   - Mounted an ESP32 camera module on RoPal’s head to capture real-time facial images.  
   - Trained a facial-emotion classifier using a pre-trained MobileNet model to recognize stress-related expressions.  
   - Ran the classifier continuously on a host PC; if a stress emotion persisted for more than 20 seconds, the PC sent a signal via wireless link to the robot’s Arduino microcontroller to initiate navigation. 
2. **Robot Navigation & Control**  
   - Built the robot base in ROS 2 using a differential-drive controller package.  
   - Developed control logic to receive the “stressed” pulse and autonomously navigate to the employee’s desk using lidar-based obstacle avoidance and SLAM for path planning. 
   - Created a digital twin of the robot base in Gazebo to test navigation algorithms before deploying on hardware. 
3. **Aromatherapy Delivery**  
   - Integrated a 4-DoF servo-driven arm on RoPal’s chassis to hold an essential-oil dispenser.  
   - Upon arrival at the target location, triggered the arm to spray a fine mist of essential oils directed toward the employee for stress relief. 

## Challenges Faced
- **Hardware-Software Integration**  
  Wireless communication between the PC-based emotion detector and the Arduino microcontroller required extensive debugging to ensure low-latency, reliable command signals.  
- **Component Constraints**  
  Some desired sensors and actuators were unavailable in the inventory; the team sourced alternative parts and redesigned mechanical fixtures on the fly to maintain functionality. 

## Contributions
- **Team Composition**  
  RoPal was built by a five-member interdisciplinary team: Suriya Prakash, Mohan Raj Babu, Shiva Sam Kumar Govindan, Jyothsna S., and one additional member. 
- **My Role (Shiva Sam Kumar Govindan)**  
  - Designed the 3D CAD model of the robot, optimizing form factor and ergonomics for office navigation.
  - Implemented the ROS 2 differential-drive controller and developed navigation logic, integrating SLAM and obstacle avoidance.  
  - Created a digital twin of the robot base in Gazebo for realistic control testing and rapid iteration. 

## Results
- Delivered a **partially functional prototype** capable of detecting sustained stress expressions, autonomously navigating to a user, and spraying essential oils for aromatherapy-based stress relief.  
- Demonstrated feasibility of combining real-time deep-learning inference, ROS 2 navigation, and rapid prototyping under hackathon time constraints. 
