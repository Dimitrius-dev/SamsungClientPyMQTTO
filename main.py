import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("user/dima12/your/temp")

def on_message(client, userdata, msg):
     print("Message: " + str(msg.payload.decode()))
     print("Topic: " + str(msg.topic) + "\n")

if __name__ == '__main__':

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("mqtt.by", 1883, 60)

    #client.publish("localhost", 1)

    client.loop_start()

    while True:
        #time.sleep(1)

        message = input("Your")
        if(message != ""):
            client.publish("user/dima12/your/temp", message)

    client.loop_stop()