# data_storage.py

import paho.mqtt.client as mqtt
import json
import os
from datetime import datetime, timedelta

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iotassignment/station1"
DATA_FILE = "sensor_data.json"

# Called when connected to broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT broker.")
        client.subscribe(TOPIC)
    else:
        print("❌ Connection failed with code", rc)

# Called when a message is received
def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    try:
        data = json.loads(payload)

        # Save data to file
        save_sensor_data(data)

        print(f"💾 Stored data from {data['station_id']} at {data['timestamp']}")

    except Exception as e:
        print("⚠️ Error processing message:", e)

# Save new data into a JSON file (append)
def save_sensor_data(data):
    existing = []

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                existing = json.load(f)
            except:
                pass

    existing.append(data)

    with open(DATA_FILE, "w") as f:
        json.dump(existing, f, indent=2)

# Run this to display last 5 hours of a specified sensor
def show_last_5_hours(sensor_type):
    if not os.path.exists(DATA_FILE):
        print("⚠️ No data file found.")
        return

    now = datetime.utcnow()
    cutoff = now - timedelta(hours=5)

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    print(f"\n📊 {sensor_type.capitalize()} values from the last 5 hours:\n")

    for entry in data:
        timestamp = datetime.fromisoformat(entry["timestamp"])
        if timestamp >= cutoff:
            print(f"{timestamp} | {entry['station_id']} | {sensor_type}: {entry[sensor_type]}")

# MAIN FUNCTION
if __name__ == "__main__":
    mode = input("Enter 'listen' to store data or 'show' to view last 5 hours: ").strip().lower()

    if mode == "listen":
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(BROKER, PORT)
        client.loop_forever()

    elif mode == "show":
        sensor = input("Which sensor? (temperature / humidity / co2): ").strip().lower()
        if sensor in ["temperature", "humidity", "co2"]:
            show_last_5_hours(sensor)
        else:
            print("❌ Invalid sensor type.")
