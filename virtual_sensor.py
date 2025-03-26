# virtual_sensor.py

import random
import time
import json
import datetime
import paho.mqtt.client as mqtt

# MQTT settings (we'll move these to mqtt_config.py later)
BROKER = "test.mosquitto.org"  # For testing, replace with ThingSpeak/AWS later
PORT = 1883
TOPIC = "iotassignment/station1"  # Customize your topic

# Generate random sensor values
def generate_sensor_data():
    return {
        "station_id": "station_01",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "temperature": round(random.uniform(-50, 50), 2),
        "humidity": round(random.uniform(0, 100), 2),
        "co2": round(random.uniform(300, 2000), 2)
    }

# MQTT Publish Function
def publish_data(client):
    sensor_data = generate_sensor_data()
    payload = json.dumps(sensor_data)
    result = client.publish(TOPIC, payload)
    status = result[0]
    if status == 0:
        print(f"✅ Sent `{payload}` to topic `{TOPIC}`")
    else:
        print(f"❌ Failed to send message to topic {TOPIC}")

# Setup MQTT client
client = mqtt.Client()
client.connect(BROKER, PORT)

# Publish every 10 seconds
try:
    while True:
        publish_data(client)
        time.sleep(10)
except KeyboardInterrupt:
    print("🚨 Stopped by user")
