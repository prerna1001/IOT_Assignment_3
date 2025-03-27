import paho.mqtt.client as mqtt
import random
import time

# ✅ ThingSpeak MQTT Configuration
MQTT_BROKER = "mqtt3.thingspeak.com"
PORT = 1883
CHANNEL_ID = "2894353"
MQTT_USERNAME = "LCQFLiYFLBIDMC4TKx0UHAE"
MQTT_PASSWORD = "yZUs2Gy0sw2cW0Y+0SyqsLRK"
WRITE_API_KEY = "FT5B9K5UDO6AOSUU"

TOPIC = f"channels/{CHANNEL_ID}/publish/{WRITE_API_KEY}"

# ✅ Generate random sensor values
def generate_sensor_data():
    temp = round(random.uniform(-50, 50), 2)
    hum = round(random.uniform(0, 100), 2)
    co2 = round(random.uniform(300, 2000), 2)
    return temp, hum, co2

try:
    while True:
        temp, hum, co2 = generate_sensor_data()
        payload = f"field1={temp}&field2={hum}&field3={co2}"

        # ✅ New MQTT connection for each publish
        client = mqtt.Client()
        client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        client.connect(MQTT_BROKER, PORT)

        result = client.publish(TOPIC, payload)
        status = result[0]
        if status == 0:
            print(f"✅ Sent `{payload}` to topic `{TOPIC}`")
        else:
            print(f"❌ Failed to send message to topic {TOPIC}")

        client.disconnect()
        time.sleep(20)  # Give enough delay to avoid rate limit issues

except KeyboardInterrupt:
    print("🛑 Publishing stopped by user.")
