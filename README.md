# 🌐 IoT Assignment 3 – Environmental Monitoring with ThingSpeak

This project demonstrates an IoT system that simulates an environmental monitoring station using **ThingSpeak**, **MQTT**, and **MATLAB Visualizations**. It was developed as part of **CIS600 Assignment 3**.

---

## 📦 Project Overview

- Sensor data (Temperature, Humidity, CO₂) is **simulated and published via MQTT** to a ThingSpeak channel.
- The **ThingSpeak dashboard** displays real-time data using numeric and chart widgets.
- **MATLAB Visualizations** are used to display historical data for the last 5 hours from a specified sensor.

---

## 📁 Contents

| File | Description |
|------|-------------|
| `mqtt_publisher.py` | Python script that simulates sensor data and publishes it to ThingSpeak using MQTT |
| `report.md` or `report.pdf` | Detailed explanation of implementation steps |
| `temperature_plot.png` | Screenshot of MATLAB plot showing the last 5 hours of temperature data |
| `dashboard_view.png` | Screenshot of the ThingSpeak channel dashboard with real-time values |
| `README.md` | This file |

---

## 💡 Features

- 📡 **MQTT Protocol** used for lightweight sensor data transmission
- 📊 Real-time updates using **ThingSpeak Widgets**
- 📈 Historical data plotted using **MATLAB code** inside ThingSpeak
- 🧪 Fully simulated – no physical sensors required

---

## 🔧 Technologies Used

- **ThingSpeak** (for cloud-based IoT storage & visualization)
- **paho-mqtt** (Python MQTT client library)
- **MATLAB (ThingSpeak App)** (for custom visualizations)
- **Python** (for data publishing script)

---

## 📷 Screenshots

### ThingSpeak Dashboard:
![Dashboard View](https://thingspeak.mathworks.com/channels/2894353)
https://thingspeak.mathworks.com/apps/matlab_visualizations/612903

---

## ⚠️ Note

ThingSpeak does not currently allow public viewing of **MATLAB Visualizations**. As a result, a screenshot of the output plot has been provided in this repo for reference.

---

## 📚 Report Summary

The full explanation of how the IoT system was developed — including channel setup, MQTT configuration, real-time updates, and data visualization — can be found in the `report.md` or `report.pdf` file.

---

## ✅ How to Run the MQTT Publisher

1. Install dependencies:
   ```bash
   pip install paho-mqtt
