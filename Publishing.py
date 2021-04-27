#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import time
from paho.mqtt import client as mqtt_client
import hashlib, binascii, os
import ldap3
from ldap3.core.exceptions import LDAPException

broker="192.168.198.128"
port =1883
topic = "/python/mqtt"
ldap_server = " "
ldap_username = "chamodi"
ldap_password = "London123"

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

# password hashing
def hash_password(hash_password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

print(hash_password(password))

# ldap_login Auth
def ldap_auth(username, password):
    try:
        with ldap3.Connection(ldap_server, user=username, password=hash_password(password)) as conn:
            print(conn.result["description"]) # "success" if bind is ok
            return True
    except LDAPException:
        print('Unable to connect to LDAP server')
        return False
    
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    ldap_status = ldap_auth(ldap_username, ldap_password)
    if(ldap_status):
        publish(client)
    else:
        print("LDAP server - User name and password do not match");


if __name__ == '__main__':
    run()


# In[ ]:




