# ⚡ EV Charger Intelligent Fault Diagnosis System

<p align="center">

<img src="https://img.shields.io/badge/Platform-STM32-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/Language-Embedded%20C-orange?style=for-the-badge&logo=c&logoColor=white">
<img src="https://img.shields.io/badge/ML-Random%20Forest-red?style=for-the-badge">
<img src="https://img.shields.io/badge/Communication-RS--485-purple?style=for-the-badge">
<img src="https://img.shields.io/badge/GUI-Python%20%7C%20PyQt5-yellow?style=for-the-badge&logo=python&logoColor=white">
</p>


## 🚀 Overview

> **An intelligent real-time embedded diagnostic system for Electric Vehicle (EV) charging modules.**

This project performs **pulse-based electrical diagnostics** using an **STM32 Nucleo-L476RG** and classifies charger health using an embedded **Random Forest Machine Learning model**.

The predicted fault is transmitted over **RS-485 industrial communication** and visualized on a **Python GUI dashboard**, enabling **predictive maintenance** and early fault detection.

---

## ✨ Key Features

| 🚀 Feature | Description |
|:----------|:------------|
| ⚡ **Pulse-Based Diagnostics** | Generates controlled current pulses to capture unique electrical fault signatures. |
| 🤖 **Embedded AI** | Random Forest classifier predicts the health state in real time. |
| 📡 **Industrial Communication** | Reliable RS-485 communication for noisy electrical environments. |
| 📊 **Live Monitoring Dashboard** | Python GUI displays voltage, current, capacitor voltage and fault status. |
| 💾 **Data Logging** | Stores diagnostic results for analysis and maintenance history. |

---

## 🚦 Fault Detection Logic

The embedded ML model classifies the charger into **five operating conditions**.

| Status | Fault Condition |
|:------:|----------------|
| ✅ | Normal Operation |
| 🔌 | Connector Open |
| ⚠️ | Connector Degraded |
| ❌ | MOSFET Open Fault |
| 🔥 | MOSFET Degradation *(RDS(on) Drift)* |

---

## 🛠 Hardware Used

| Component | Description |
|-----------|-------------|
| 🖥 **Controller** | STM32 Nucleo-L476RG |
| ⚡ **Current Sensor** | ACS712 Hall Effect Sensor |
| 🔋 **Voltage Measurement** | Voltage Divider Circuit |
| 🔀 **Switching Device** | IRF540N MOSFET |
| 🔧 **Driver** | BC547 NPN Transistor |
| 📡 **Communication** | MAX13487 RS-485 Transceiver |

---

## 💻 Software Stack

| Software | Purpose |
|----------|---------|
| 🧩 STM32CubeIDE | Embedded Firmware Development |
| 🐍 Python | Desktop Application |
| 🖥 PyQt5 | GUI Development |
| 📊 Pandas & NumPy | Data Processing |
| 🤖 Scikit-learn | Machine Learning |

---


## 🔧 Getting Started

### ① Flash Firmware

Open the firmware project in **STM32CubeIDE** and flash it to the **STM32 Nucleo-L476RG**.

---

### ② Hardware Connections

Connect

- ACS712 Current Sensor
- Voltage Divider
- IRF540N MOSFET
- BC547 Driver
- MAX13487 RS-485 Module

according to the project schematic.

---

### ③ Install Python Dependencies

```bash
pip install pyqt5 pyserial pandas numpy scikit-learn
```

---

### ④ Run Dashboard

```bash
python gui.py
```

---

## 📈 Project Highlights

✨ Embedded Machine Learning

⚡ Pulse-Based Fault Diagnosis

📡 Industrial RS-485 Communication

💻 Professional Python Dashboard

📊 Live Telemetry

📝 Fault Logging

---

## 👨‍💻 Researchers

- **Anora Sharon Tessie S**
- **Kalimalla Arshad**

---

## 🎓 Internship

**Summer Internship – 2026**

**Department of Electrical Engineering**

**National Institute of Technology Calicut**

**Supervisor**

**Dr. Jagadanand G.**

Professor & Head

Department of Electrical Engineering

National Institute of Technology Calicut

---

<p align="center">

### ⭐ If you found this project useful, consider giving it a Star ⭐

</p>
