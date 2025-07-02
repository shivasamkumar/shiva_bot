# LPV-MPC Controller for Autonomous Vehicle: Trajectory Tracking and Dynamic Control

## Introduction
The LPV-MPC Controller for Autonomous Vehicle project aims to develop a robust control system that allows an autonomous vehicle to follow predetermined trajectories with high precision. Autonomous vehicles operate in dynamic environments, where accurate trajectory tracking is crucial for safety and efficiency. This project uses a Model Predictive Controller (MPC) with a Linear Parameter-Varying (LPV) approach to handle the inherent nonlinearities of vehicle dynamics. 

The LPV-MPC framework is particularly suited for autonomous vehicles because it dynamically adjusts the control strategy based on the vehicle’s current operating conditions. By approximating nonlinear behaviors with a set of linear models, the LPV-MPC effectively manages changes in vehicle dynamics, allowing for stable control even under varying conditions. The controller uses a bicycle model for simplified representation of vehicle kinematics, balancing accuracy and computational efficiency. The control inputs for the system are the steering angle and applied acceleration, which are optimized through a cost function that minimizes deviations from the desired trajectory.

The controller’s effectiveness was tested in simulations across three distinct driving scenarios, each with unique trajectory complexities to evaluate performance. In these simulations, the LPV-MPC demonstrated its ability to maintain trajectory adherence, manage dynamic vehicle responses, and respect constraints on control inputs and states. The project’s success highlights the potential of LPV-MPC to enhance the reliability of autonomous vehicle control, making it a promising foundation for further advancements in autonomous driving technologies.

## Procedure
1. **Vehicle Modeling**  
   - Represented the vehicle with a simplified bicycle model to capture key kinematic and dynamic behaviors.  
2. **LPV Approximation**  
   - Linearized the nonlinear bicycle model around multiple operating points to form a parameter-varying representation.  
3. **MPC Formulation**  
   - Defined a cost function that penalizes deviations from the reference trajectory and control effort, subject to constraints on steering angle, acceleration, and state bounds.  
4. **Solver Implementation**  
   - Implemented the MPC optimization in Python using CVXOPT as the underlying QP solver (`Main_MPC.py` and `support_files.py`).  
5. **Simulation & Testing**  
   - Integrated the controller into the CARLA simulator and evaluated its performance across three distinct driving scenarios, each with unique trajectory complexities.

## Challenges Faced
- **Nonlinear Dynamics Approximation**  
  Choosing appropriate linearization points to ensure the LPV model remained accurate across all operating conditions.  
- **Real-Time Computation**  
  Achieving sufficient solver speed with a Python-based QP implementation to close the control loop in simulation.  
- **Simulator Integration**  
  Synchronizing controller outputs with the CARLA API and handling coordinate-frame conversions for seamless testing.

## Contributions
- **Algorithm & Code**  
  Wrote the core MPC logic and QP setup in `Main_MPC.py`, with supporting utilities in `support_files.py`.  
- **Interactive Analysis**  
  Developed `proj.ipynb` for offline tuning of cost-function weights and visualization of tracking performance.  
- **Simulation Integration**  
  Hooked the LPV-MPC controller into CARLA to run end-to-end tests in realistic driving environments. 

## Results
- **Trajectory Tracking**  
  Demonstrated that the LPV-MPC controller could maintain close adherence to reference paths in all three simulated scenarios, respecting both input and state constraints.  
- **Dynamic Adaptation**  
  Showed effective adjustment of control strategy under varying vehicle speeds and trajectory curvatures, validating the LPV approach’s ability to handle nonlinearities. 
