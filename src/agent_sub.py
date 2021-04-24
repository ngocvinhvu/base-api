import paho.mqtt.client as mqtt
import argparse 


class Mqtt:
    def __init__(self, client_id, username, password):
        self.client_id = client_id
        self.client = mqtt.Client(client_id, clean_session=True)
        self.client.username_pw_set(username, password)
        self.client.on_message = self.__on_message
        self.client.on_connect = self.__on_connect
        self.client.will_set("World".format(self.client_id), payload='{"status": "OFFLINE"}', qos=0, retain=True)
        self.client.on_subscribe = self.__on_subscribe

    def __on_connect(self, mqttc, obj, flags, rc):
        if rc == 0:
            self.client.publish("World".format(self.client_id), payload='{"status": "ONLINE"}', qos=0, retain=True)
            self.client.subscribe("agent/default", 1)
            self.client.subscribe("World".format(self.client_id), 1)
        else:
            self.client.disconnect()
        print("rc: " + str(rc))


    def __on_message(self, mqttc, obj, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


    def __on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))


    def __on_log(self, mqttc, obj, level, string):
        print(string)

    def start(self):
        self.client.loop_forever()

    def connect(self, host, port):
        self.client.connect(host, port, 60)


def main():
    msg = "Adding description"
    
    parser = argparse.ArgumentParser() 
    
    parser.add_argument('-c', '--client_id', dest='client_id', required=True, help='Client id to connect mqtt')
    parser.add_argument('-u', '--username', dest='username', help='username')
    parser.add_argument('-p', '--password', dest='password', help='password')
    args = parser.parse_args()
    
    client_id = args.client_id
    username = args.username
    password = args.password
    
    if not username:
        username = 'admin'
    if not password:
        password = 'VMQpassword'

    vernmq = Mqtt(client_id, username, password)
    host = 'localhost'
    vernmq.connect(host, 1883)
    vernmq.start()

if __name__ == '__main__':
    main()
    
