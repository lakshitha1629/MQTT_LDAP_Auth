#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
import time
import paho.mqtt.client as mqtt_client
import hashlib, binascii, os
import ldap3
from ldap3.core.exceptions import LDAPException

# Buffer Value get userName and pwd
def bufferReg(bufferValue):
    string =bufferValue.decode('utf-8', 'ignore')
    source= ''.join(e for e in string if e.isalnum())
    result=[]
    tmpUser=source.split('authdatausername')
    tmpPwd=source.split('password', 1)
    for par in tmpUser:
        if 'password' in par:
            result.append(par.split('password')[0])
    return result[0],tmpPwd[1]

# Check hashed password validity
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
#     pwdhash = hashlib.pbkdf2_hmac('sha512',
#                                   provided_password.encode('utf-8'),
#                                   salt.encode('ascii'),
#                                   100000)
#     pwdhash = binascii.hexlify(pwdhash).decode('ascii')
#     print(pwdhash, stored_password, provided_password)
    return provided_password == stored_password
        
# ldap_login Auth
def ldap_auth(ldap_server, username, password):
    try:
#         with ldap3.Connection(ldap_server, user=username, password=hash_password(password)) as conn:
        with ldap3.Connection(ldap_server, user=username, password=password, auto_bind = True) as conn:
            print(conn.result["description"]) # "success" if bind is ok
            return True
    except LDAPException:
        print('Unable to connect to LDAP server')
        return False


# In[ ]:




