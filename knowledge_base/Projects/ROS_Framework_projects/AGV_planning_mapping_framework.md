# Robot Car: Localization & Mapping

## Introduction
The Robot Car: Localization & Mapping project transforms a basic differential-drive AGV into a fully autonomous, map-aware robot by combining real-time SLAM, probabilistic localization, and goal-driven navigation under ROS 2 Humble on Ubuntu 22.04. During **mapping mode**, the robot is teleoperated with a joystick while the `slam_toolbox` package incrementally builds a 2D occupancy grid of the environment in Gazebo; once exploration is complete, that map is saved to disk. In **localization mode**, the saved map is loaded and the Adaptive Monte Carlo Localization (AMCL) node fuses wheel-odometry and laser scans to maintain an accurate, real-time pose estimate within the map. That pose is then fed into the ROS 2 Navigation2 stack, which plans and executes collision-free paths to user-specified waypoints read from a YAML file by a custom Waypoint Navigator node. At every step, the `twist_mux` package arbitrates between joystick inputs and autonomous velocity commands, allowing seamless manual overrides without disrupting the navigation pipeline. A ROS 2 Lifecycle Manager oversees clean transitions between mapping, localization, and planning states, ensuring that only the appropriate nodes and parameters are active at any time. This end-to-end workflow has been validated across multiple Gazebo worlds—including an AWS model house, a warehouse scenario, and user-defined custom maps—demonstrating robust mapping quality, reliable AMCL-based pose estimation, and smooth waypoint navigation with real-time operator intervention.  

## Challenges Faced 

- **AMCL Parameter Tuning**

Balancing particle count and noise covariances for accurate localization without excessive compute load.

- **Map Quality & Consistency**

Ensuring SLAM-generated maps maintained clear obstacle boundaries and minimal drift across environments.

- **Twist Mux Arbitration**

Configuring priorities to prevent conflicts between joystick inputs and autonomous velocity commands.

- **Lifecycle Transitions**

Implementing seamless, error-free state transitions between mapping, localization, and planning modes using the ROS 2 lifecycle API.

## Results

- Generated high-fidelity occupancy maps in multiple Gazebo worlds (AWS house, warehouse, custom).

- Achieved robust AMCL-based localization with pose errors within acceptable bounds.

- Demonstrated autonomous waypoint navigation and dynamic obstacle avoidance via the ROS 2 Nav Stack.

- Enabled real-time joystick overrides through twist_mux without destabilizing autonomous behaviors.

- Packaged the system as reproducible ROS 2 launch files and lifecycle configurations for deployment in both simulated and hardware environments.