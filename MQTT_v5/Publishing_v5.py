#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import time
import paho.mqtt.client as mqtt_client
import hashlib, binascii, os
import ldap3
from ldap3.core.exceptions import LDAPException

broker="broker.emqx.io"
port =1883
topic = "/python/mqtt"
ldap_server = "ldap.forumsys.com"
ldap_username = "cn=read-only-admin,dc=example,dc=com"
ldap_password = "password"

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

# password hashing
def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

# print(hash_password(ldap_password))

# ldap_login Auth
def ldap_auth(username, password):
    try:
#         with ldap3.Connection(ldap_server, user=username, password=hash_password(password)) as conn:
        with ldap3.Connection(ldap_server, user=username, password=password, auto_bind = True) as conn:
            print(conn.result["description"]) # "success" if bind is ok
            return True
    except LDAPException:
        print('Unable to connect to LDAP server')
        return False
    
def connect_mqtt():
    def on_connect(client, userdata, flags, reasonCode, properties=None):
        if reasonCode == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", reasonCode)

    client = mqtt_client.Client(client_id, protocol=mqtt_client.MQTTv5)
    client.on_connect = on_connect
    client.connect(broker, port, keepalive=60, bind_address="", bind_port=0, clean_start=mqtt_client.MQTT_CLEAN_START_FIRST_ONLY, properties=None)
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
#     publish(client)
    ldap_status = ldap_auth(ldap_username, ldap_password)
    if(ldap_status):
        print("LDAP server - Authenticated successfully. ");
        publish(client)
    else:
        print("LDAP server - User name and password do not match");


if __name__ == '__main__':
    run()


# In[ ]:




