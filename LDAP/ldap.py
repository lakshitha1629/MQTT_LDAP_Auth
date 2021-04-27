#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ldap3
from ldap3.core.exceptions import LDAPException


def _ldap_login(username, password):
    try:
        with ldap3.Connection('enter_server', user=username, password=password) as conn:
            print(conn.result["description"]) # "success" if bind is ok
            return True
    except LDAPException:
        print('Unable to connect to LDAP server')
        return False

_ldap_login("enter_username", "enter_password")


# In[ ]:





# In[ ]:




