# MPI-CNC: Cyber-Attack Detection in CNC-Based CPMS

This project implements **MPI-CNC**, an intrusion detection approach for cyber–physical manufacturing systems (CPMS), based on machining process invariants extracted from CNC machining code.

> 📄 IEEE Paper: *Detecting Cyber-Attacks Against Cyber-Physical Manufacturing System: A Machining Process Invariant Approach*

---

## 📌 Project Overview

With the rise of Industrial IoT, CNC systems have become a core target for cyber-attacks. Existing detection systems are highly specific and require significant retraining for new scenarios. MPI-CNC addresses these challenges by:

- Automatically extracting detection rules from CNC G-code.
- Actively monitoring CNC systems at runtime.
- Providing high-accuracy attack detection with minimal interference.

---

## 🏗️ Project Structure
. ├── simulator.py # Generates random CNC data with anomaly injection ├── detect_anomalies.py # Detects and classifies anomalies based on rules ├── cnc_utils.py # CNC parsing and communication helper functions ├── data/ # Sample CNC G-code and parameters ├── results/ # Experiment results and logs ├── README.md └── requirements.txt
