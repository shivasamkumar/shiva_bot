# Hexapod Kinematics Simulator

## Introduction
- This project, **Hexapod Kinematics Simulator**, models and controls the movement of a six-legged robot using forward and inverse kinematics to demonstrate efficient leg coordination and body stability across roll, pitch, yaw, and translation motions. 
- Developed as Team project for the Modeling and Control of Robots (MAE547) course at Wichita State University by Team 21: Ezhilan Veluchami, Kirthik Roshan Nagaraj, Shiva Sam Kumar, Suriya Prakash Murugan, and Jyothsna Suresh. 
- Implements forward kinematic computations using Denavit–Hartenberg parameters and homogeneous transformation matrices to calculate each leg’s end-effector position from joint angles, and inverse kinematic algorithms to solve for joint angles required to reach desired foot placements while respecting constraints like ground clearance and joint limits. 
- Applies body kinematics transformations using rotation matrices (Rx, Rz, Ry) to adjust leg-base coordinates for roll, pitch, yaw, and translations, enabling realistic simulation of complex maneuvers. 
- Integrates a stability checker that early-exits unstable poses when coxa points fall below ground, joint angles exceed allowable ranges, or support polygons become invalid due to excessive airborne legs. 
- Delivered as a cross-platform ReactJS web application with Plotty for 3D visualization, accessible at https://hexapod-mae547.web.app/ without local software installation. 

## Procedure
1. **Forward Kinematics**  
   - Defined Denavit–Hartenberg parameters for each leg’s coxa, femur, and tibia link lengths.  
   - Constructed homogeneous transformation matrices to compute the position of each foot (end effector) given a set of joint angles. 

2. **Inverse Kinematics – Leg**  
   - Computed leg length: \\(\text{LegLength} = \sqrt{X^2 + Z^2}\\) and intermediate distance HF from link geometry.  
   - Derived joint angles via trigonometric relations:  
     1. \\(A1 = \arctan\bigl((\text{LegLength} - \text{CoxaLength}) / Y\bigr)\\)  
     2. \\(A2 = \arccos\bigl((TLength^2 - FLength^2 - HF^2)/(-2\,FLength\,HF)\bigr)\\)  
     3. \\(F.\text{Angle} = 90° - A1 + A2\\)  
     4. \\(B1 = \arccos\bigl((HF^2 - TLength^2 - FLength^2)/(-2\,FLength\,TLength)\bigr)\\)  
     5. \\(T.\text{Angle} = 90° - B1\\)  
     6. \\(C.\text{Angle} = \arctan(Z/X)\\) 

3. **Inverse Kinematics – Body**  
   - Computed relative foot coordinates after applying rotation matrices around X (Rx), Z (Rz), and Y (Ry) axes.  
   - Combined into a single rotation matrix \\(R = Rx \times Rz \times Ry\\) to transform foot positions for body motions (roll, pitch, yaw, translations).
4. **Stability Checking**  
   - Early-exited when any coxa point fell below ground level or computed joint angles lay outside allowable ranges.  
   - Evaluated support-polygon validity, ensuring no more than three legs were airborne at once. 

5. **Web Application**  
   - Built a ReactJS single-page app using Plotty for interactive 3D rendering of the hexapod links.  
   - Provided simple setup: run `npm install` then `npm start` to launch at `http://localhost:3000/`. 

## Challenges Faced
- **Analytical Complexity**  
  Deriving robust inverse-kinematics formulas under constraints (ground clearance, joint limits, leg reachability) required extensive trigonometric validation.  
- **Stability Constraints**  
  Guaranteeing a valid support polygon during uneven leg lifts necessitated additional logic to detect and reject unstable poses in real time.
- **Cross-Platform Visualization**  
  Integrating high-performance 3D rendering in a browser while synchronizing with live kinematic computations posed performance-tuning challenges in the ReactJS environment.

## Contributions
- **Team Composition**  
  Ezhilan Veluchami (20%), Kirthik Roshan Nagaraj (20%), Shiva Sam Kumar (20%), Suriya Prakash Murugan (20%), Jyothsna Suresh (20%). 

- **My Role (Shiva Sam Kumar)**  
  - Computed Denavit–Hartenberg parameters and implemented forward-kinematics algorithms for each leg. 
  - Developed inverse-kinematics solvers for individual legs and body transformations, ensuring solutions respect ground-clearance, joint-limit, and balance constraints. 
  - Contributed to the ReactJS & Plotty-based web application for real-time 3D visualization of kinematic outputs. 

## Results
- Delivered a fully functional kinematics simulator capable of modeling forward and inverse movements of a hexapod in an interactive web interface. 
- Deployed the web app at https://hexapod-mae547.web.app/, enabling cross-platform demonstrations without additional software. 
- Validated stability and accuracy of all kinematic algorithms across roll, pitch, yaw, and translations through simulation scenarios. 