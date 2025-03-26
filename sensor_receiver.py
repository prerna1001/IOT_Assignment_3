# sensor_receiver.py

import paho.mqtt.client as mqtt
import json

# MQTT Broker and Topic - must match your virtual_sensor.py
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iotassignment/station1"

# This is the ID of the environmental station you want to filter by
TARGET_STATION_ID = "station_01"

# Called when connection to broker is successful
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT broker.")
        client.subscribe(TOPIC)
    else:
        print("❌ Failed to connect. Return code:", rc)

# Called when a new MQTT message is received
def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    try:
        data = json.loads(payload)
        if data["station_id"] == TARGET_STATION_ID:
            print("\n📥 Latest Sensor Data from", TARGET_STATION_ID)
            print(f"Timestamp:   {data['timestamp']}")
            print(f"Temperature: {data['temperature']} °C")
            print(f"Humidity:    {data['humidity']} %")
            print(f"CO₂:         {data['co2']} ppm")
    except Exception as e:
        print("⚠️ Error processing message:", e)

# Set up MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
client.loop_forever()
