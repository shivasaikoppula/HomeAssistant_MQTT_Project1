import paho.mqtt.client as mqtt
import random
import time

student_name = "Shiva Sai Koppula"
unique_id = "42110655"

broker = "192.168.1.14"
port = 1883

client = mqtt.Client()
client.connect(broker, port)

while True:
    temperature = round(random.uniform(20, 35), 2)
    humidity = round(random.uniform(40, 80), 2)
    light = random.randint(100, 900)

    topic_prefix = "home/shivasai-42110655/sensor"

    client.publish(f"{topic_prefix}/temperature", temperature)
    client.publish(f"{topic_prefix}/humidity", humidity)
    client.publish(f"{topic_prefix}/light", light)

    print("Published:", temperature, humidity, light)
    time.sleep(5)
