---
layout: project
type: project
image: img/hvacsim.png
title: "HVACSim - MITRE Caldera for OT Capstone"
date: 2025
published: true
labels:
  - Python
  - Linux
  - BACnet/IP
  - BACpypes
  - Matplotlib
  - MITRE Caldera for OT
summary: "A software-only server-room HVAC simulator built with MITRE's OT Cybersecurity Engineering team for BACnet/IP red/blue-team and cyber-physical testing."
---

<img src="../img/hvacsim.png" alt="Caldera logo with a stylized mountain and circuit traces on a black background" width="800">

## Capstone with MITRE

From September to December 2025, I collaborated directly with MITRE's OT Cybersecurity Engineering team to build HVACSim, a software-only server-room HVAC simulator. The project provides a BACnet/IP environment for red/blue-team exercises and cyber-physical testing with MITRE Caldera for OT, without requiring physical industrial hardware.

## Simulating the control system

I implemented writable BACnet control points for the temperature setpoint, intake and exhaust fans, and emergency stop using Python and BACpypes. The simulation models room temperature and chiller dynamics with a proportional-integral (PI) control loop, sensor noise, and actuator lag. Emergency-stop behavior brings the simulated fans and chiller to a stop.

## Observing and validating changes

I built a real-time human-machine interface (HMI) with Matplotlib, including temperature and equipment trend charts, sliders, and an emergency-stop control. This makes it possible to observe how local controls and BACnet overrides affect the simulated system. I developed and validated the integration in Linux virtual machines.

[View the source code on GitHub](https://github.com/jaked332/MITRE_SimEnv).
