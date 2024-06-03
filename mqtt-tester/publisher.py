# python 3.11

import random
import time
import json
import paho.mqtt.client as mqtt_client # Version 2.1


broker = '127.0.0.1'
port = 1883
topic = "python/mqtt"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc, properties):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
        client.subscribe("$SYS/#")

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 1
    json_msg = {
       'influx_name'        : 'machine_temp',
       'influx_cid'         : 'sajkfh3',
       'influx_sensortype'  : 'temperature',
       'influx_unit'        : 'celsius',
       'machine_pct'        : random.randint(30,120)
    }
    while True:
        time.sleep(1)
        #with open('output_mock_sensor.json', 'a') as output_file:
        #    output_file.write(f'{json.dumps(json_msg)}\n')
        json_msg['machine_pct'] = random.randint(30,120)
        result = client.publish(topic, f'{json.dumps(json_msg)}\n')
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send a msg to topic `{topic}`")
            print("About", json_msg['machine_pct'])
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > 100:
            break


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == '__main__':
    run()

