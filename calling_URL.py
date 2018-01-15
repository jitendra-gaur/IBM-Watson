# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:44:32 2018

@author: Jitendra Gaur
"""

import urllib2
import time
#%%
i=0
for i in range(0,365):
    urllib2.urlopen("https://abc.com/start").read()
    time.sleep(120)
    
#%%
