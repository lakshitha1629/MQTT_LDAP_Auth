#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import ldap3
from ldap3.core.exceptions import LDAPException

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

