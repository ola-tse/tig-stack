import time
import numpy as np
import paho.mqtt.client as mqtt

broker_url = "tig-stack-mosquitto-1"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
   print(f"Connected With Result Code {rc}")

def on_message(client, userdata, message):
   print("Msg: "+message.payload.decode())

def get_sin(t):
   return np.sin(t)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_url, broker_port)

while 1:
   time_seed = time.time()
   
   for i in range(1, 10):
      topic = f"values/sinus{i}"
      payload = get_sin(time_seed/i)
      client.publish(topic=topic, payload=payload, qos=0, retain=False)

   time.sleep(0.01)
