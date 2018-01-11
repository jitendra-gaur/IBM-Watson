# -*- coding: utf-8 -*
"""
Created on Thu Jul 27 12:40:31 2017

@author: IBM_ADMIN
"""

import datetime
d = datetime.datetime.utcnow() # <-- get time in UTC
print (d.isoformat("T") + "Z")
#print d.isoformat("T") 
#%%

username='arunava.saha@in.ibm.com'
password='Oracle123'
#%%
# Calling Oracle REST API to fetch the product details.
import requests

response = requests.get('https://ecnp-test.scm.us2.oraclecloud.com/productManagementCommonApi/resources/11.12.1.0/items', auth=('ARUNAVA.SAHA', 'Oracle123'))

#response = requests.get('https://edrx-test.scm.us2.oraclecloud.com:443/egpItems/ItemServiceV2', auth=('arunava.saha@in.ibm.com', 'Oracle123'))

data = response.json()

#%%
from collections import OrderedDict

mydict = o

def listRecursive (d, key):
    for k, v in d.items ():
        if isinstance (v, OrderedDict):
            for found in listRecursive (v, key):
                yield found
        if k == key:
            yield v

for found in listRecursive (mydict, '@xsi:type'):
    print (found)
    
    

