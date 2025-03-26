# IoT Assignment 3 – Virtual Environmental Monitoring System

This project simulates an IoT system that collects environmental data from virtual sensors and sends it to a cloud-based MQTT broker. The system is built using Python and uses the `paho-mqtt` library for MQTT communication.

## Project Overview

The system has three main parts:

1. **Virtual Sensor** – A Python script that randomly generates temperature, humidity, and CO₂ values every 10 seconds and publishes them to an MQTT topic.
2. **Sensor Receiver** – A subscriber script that listens to the topic and displays the latest sensor values received from a specific station.
3. **Data Storage** – A script that stores incoming data into a JSON file and allows the user to view the last 5 hours of values for a chosen sensor (e.g., humidity).

The system uses the public MQTT broker `test.mosquitto.org`.

## Files in This Project

- `virtual_sensor.py` – Publishes sensor data every 10 seconds
- `sensor_receiver.py` – Receives and displays the latest values
- `data_storage.py` – Stores sensor data and retrieves last 5 hours of a specified sensor
- `requirements.txt` – List of Python packages used
- `README.md` – This file
- `screenshots/` – Screenshots of working outputs (for report submission)

## How to Run the Project

1. Create and activate a virtual environment (if not already set up):
   ```bash
   python3 -m venv iot-env
   source iot-env/bin/activate
