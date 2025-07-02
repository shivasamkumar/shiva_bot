# Launchtrax – Knowledge Base Scenarios

**Employer:** Launchtrax Pvt. Limited, Bangalore, India  
**Title:** Robotics Application Engineer
**Clients:** DRDO & Hindustan Aeronautics Limited  
**Duration:** February 2020 – July 2024  

Below are general “if you ask” scenarios capturing how Shiva addressed key challenges at Launchtrax Pvt. Limited for DRDO & HAL projects. Use these to quickly explain “how X was done.”

---

## Client Priority Conflict  
**Context:** One day before the Preliminary Design Review (PDR) demo of the “Mission Planning and Debriefing System,” Shiva—lead QA analyst—discovered several minor bugs in the MVP. The Product Manager, however, insisted on showcasing an additional feature outside the PDR scope.  
**Resolution:** Shiva took ownership of all flagged bugs, coordinated with junior developers overnight to implement fixes, and reran full regression tests against the PDR requirements. He then delivered the final, tested build immediately before the demo.  
**Outcome:** The PDR demo ran flawlessly; when the client requested the extra feature, they saw the updated, bug-free functionality live—earning positive feedback with zero critical issues.

---

## On-Site Validation & Feedback  
**Context:** During system testing, Shiva traveled to the client site to validate the trajectory-estimation feature using actual black-box flight-recorder data.  
**Resolution:** He ran exhaustive on-site tests across all flight scenarios, cross-referenced outputs with black-box logs, and negotiated a small scope of pilot-requested enhancements (e.g., terrain-depth awareness for low-altitude flight).  
**Outcome:** Incremental updates were delivered on site that satisfied both contractual PDR criteria and pilot UX requests, securing client sign-off ahead of schedule.

---

## Geo-Pointing Interface Development  
**Context:** A minimal GUI was needed to convert live video from an aircraft-mounted gimbal into accurate world-coordinate targets for surveillance.  
**Resolution:** Shiva designed and coded the image → ROS 2 frame → lat/lon transform pipeline, calibrated camera intrinsics and gimbal offsets in simulation and on hardware, and built a lightweight UI.  
**Outcome:** A stable geo-pointing tool with sub-meter precision was deployed and approved for integration into the client’s avionics suite.

---

## UAV Deployment & Live-Data Fusion  
**Context:** After delivering the geo-pointing UI, Shiva deployed and tested the full system on a UAV, fusing live IMU, INS, and gimbal data—and observed occasional pointing deviations.  
**Resolution:** He logged in-flight accuracy metrics, collaborated with firmware and network teams to refine calibration parameters and retry logic, and re-verified performance in subsequent flights.  
**Outcome:** All deviations were resolved, stabilizing geo-pointing performance and gaining final client acceptance for production deployment.

---

## Real-Time Control via Ethernet/IP  
**Context:** The ground-station GUI needed to send sub-second pitch/yaw commands over Ethernet/IP to the gimbal controller.  
**Resolution:** Shiva configured IP addressing and polling rates; packaged commands in JSON; prioritized the sending process in the OS scheduler; implemented acknowledgment-and-retry logic; and enabled QoS on the network switch.  
**Outcome:** Sub-second alignment was achieved with zero missed commands under normal load.

---

## Sensor Integration via Modbus  
**Context:** The aircraft’s INS/GPU exposed position data over Modbus registers, which the GUI had to consume for accurate geo-pointing.  
**Resolution:** He embedded a Modbus master to poll at 100 ms intervals; parsed and converted registers to WGS84 doubles; timestamp-aligned INS data with camera frames; and displayed stale-data warnings with buffered timeouts.  
**Outcome:** Sub-meter geo-pointing accuracy was enabled, even under intermittent INS delays.

---

## Latency Troubleshooting  
**Context:** Operators reported a 2–3 s lag between GUI selections and gimbal response during flight tests.  
**Resolution:** Shiva used Wireshark to confirm low network RTT; profiled the GUI to identify blocking coordinate transforms; offloaded heavy math to background threads; and verified gimbal firmware latency.  
**Outcome:** End-to-end latency was reduced to under 1 s, meeting real-time requirements.

---

## Control Stability Under Aggressive Maneuvers  
**Context:** High-G turns caused gimbal jitter and intermittent Modbus dropouts.  
**Resolution:** He applied complementary/Kalman filters to smooth feedback; slowed command rates during extreme maneuvers; gated out stale Modbus data; and validated the solution in hardware-in-the-loop simulations.  
**Outcome:** Stable gimbal control with minimal overshoot was maintained, even under harsh flight profiles.

---

## Network Packet Integrity  
**Context:** Corrupted Ethernet/IP packets during flight tests triggered unexpected gimbal resets.  
**Resolution:** Shiva monitored radio-link logs to identify packet fragmentation; added CRC checks and sequence counters; and increased receive buffer sizes.  
**Outcome:** Mid-flight resets were eliminated, ensuring reliable command delivery.

---

## Geo-Pointing Offset Calibration  
**Context:** Initial flights showed consistent geo-pointing offsets of tens of meters.  
**Resolution:** He logged pixel→lat/lon vs. ground-truth targets; discovered a 150 ms timestamp skew; implemented a central timestamp server with interpolation; and corrected barometric vs. geoid altitude calculations.  
**Outcome:** Offsets were reduced to single-digit meters, meeting client specifications.

---

## Gimbal Overload Management  
**Context:** During high-wind tests, the gimbal occasionally overloaded or stalled mid-rotation.  
**Resolution:** Shiva added real-time current sensing via Modbus; implemented software rate limiters on extreme input changes; coordinated firmware PID-gain updates; and conducted stress-test flights.  
**Outcome:** No further stalls occurred, and the gimbal handled surge commands without overload after tuning.

