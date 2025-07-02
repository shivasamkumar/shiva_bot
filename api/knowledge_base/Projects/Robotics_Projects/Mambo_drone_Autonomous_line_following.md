# Mambo Drone – Autonomous Line-Following and Control Systems Design

## Introduction
Mambo Drone project developed low-level software architecture for the Parrot Mambo mini drone, integrating control systems, sensor fusion, and computer vision to enable precise autonomous line-following while maintaining stable flight dynamics and responsiveness during operations. 

## Procedure
1. **Software Architecture & Control Algorithms**  
   Designed and implemented a modular control architecture in MATLAB/Simulink, including PID-based controllers to stabilize attitude and guide the drone along detected line paths. 
2. **Sensor Fusion**  
   Combined Inertial Measurement Unit (IMU) data with camera measurements using filtering techniques (e.g., complementary and Kalman filters) to accurately estimate orientation and position. 
3. **Computer Vision Pipeline**  
   Processed the onboard camera feed through grayscale conversion, filtering, edge detection, and feature extraction to detect and track ground line markings for navigation. 
4. **Hardware Deployment & Testing**  
   Deployed the generated control and vision code onto the Mambo drone and conducted flight tests to validate line-following capability under varying environmental conditions.

## Challenges Faced
- **IMU Noise & Drift**  
  Managing noisy and drifting inertial measurements required careful tuning of filtering parameters to maintain reliable orientation estimates.  
- **Variable Line Visibility**  
  Adapting image-processing thresholds to handle changes in lighting and line contrast for robust detection.  
- **Computational Constraints**  
  Optimizing real-time vision and control algorithms to run within the limited processing resources of the drone’s onboard systems.  

## Contributions
- **Solo Project**  
  All aspects of the project—software architecture, control-system design, sensor fusion, computer-vision pipeline, and flight testing—were developed and executed individually by the project lead.  

## Results
- Demonstrated stable autonomous line-following in real-world flight tests, successfully maintaining high path adherence and flight stability.
- Validated integration of control, sensor fusion, and vision modules, showcasing a cohesive system capable of responsive and accurate navigation.   

- youtube link: [video]("https://youtu.be/x3VUQv1mS-Y")   