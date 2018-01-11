


projectPath = 'C:/Users/IBM_ADMIN/Downloads/curl_7_53_1_openssl_nghttp2_x64'
import os
#import time
#import json
import pandas as pd

import json

#%%
os.chdir(projectPath)
doc_text = open("C:/Users/IBM_ADMIN/Downloads/curl_7_53_1_openssl_nghttp2_x64/Vacations.txt").read()
doc_text1 = json.loads(doc_text)

#df_text = pd.DataFrame(doc_text)
d = {'Tracker' : range(0,200)}
df_ents = pd.DataFrame(d)
df_ents['Transcript'] = ''



#%%

for i in range(0, 121):
    df_ents['Transcript'][i] = doc_text1['results'][i]['alternatives'][0]['transcript']
    print i
#%%
df_ents.to_csv('vacations.csv')
