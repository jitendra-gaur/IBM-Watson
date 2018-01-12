# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 12:27:09 2017

@author: Jitendra Gaur
"""

import csv
import os
import json
import codecs
import pandas as pd
import numpy as np
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator
import requests



df = pd.read_excel(open('C:\Users\Documents\Manoj_Part Center Cdty Code_uniqe.xlsx','rb'), sheetname='Without Duplicates')
df1 = pd.read_excel(open('C:\Users\Documents\Manoj_Part Center Cdty Code_uniqe.xlsx','rb'), sheetname='Without Duplicates')
#%%
d = {'S.No.' : range(0,20000)}
df_text_new = pd.DataFrame(d)
df_text_new['Product_Itemcode'] = ''
df_text_new['Product_Desc_English'] = ''
df_text_new['Product_Desc_French'] = ''
df_text_new['Product_Desc_Spanish'] = ''
df_text_new['Product_Desc_German'] = ''
#df_text_new['Product_Desc_German'] = ''
#df_text_new['Product_Name_Chinese'] = ''
#df_text_new['Product_Desc_Chinese'] = ''
       

#%%
language_translator = LanguageTranslator(username='username', password='password')
#%%
for i in range(0,10000):
    df.drop([i], inplace= True)
#%%
df = df.reset_index()
#%%
product_desc_fr = []
product_desc_esp = []
product_desc_ger = []
#product_desc_ger = []
#product_name_chi = []
#product_desc_chi = []
#%%
i=0
skipped = []
for i in range(0,10000):
    try:
        translation = language_translator.translate(
                text = df['Product_Details'][i],
                source='en',
                target='de')
        product_desc_ger.append(translation)
        print i
    except:
        skipped.append(i)
        df.drop([i], inplace= True)
        pass
        



#%%
# Writing details to data frame
# Writing details to data frame

j = 0
for j in range(0,10000):
    try:
        df_text_new['Product_Itemcode'][j] = df['ITEM_CODE(Assumption)'][j]
        df_text_new['Product_Desc_English'][j] = df['Product_Details'][j]

        #df_text_new['Product_Desc_French'][j] = product_desc_fr[j]
        #df_text_new['Product_Desc_Spanish'][j] = product_desc_esp[j]
        df_text_new['Product_Desc_German'][j] = product_desc_ger[j]
#        df_text_new['Product_Desc_German'][j] = product_desc_ger[j]
#        df_text_new['Product_Name_Chinese'][j] = product_name_chi[j]
#        df_text_new['Product_Desc_Chinese'][j] = product_desc_chi[j]
    except:
        pass
#%%        
#Writing data frame to CSV
df_text_new.to_csv('translation_German_2.csv', encoding='utf-8')
df1.to_csv('skipped2.csv', encoding='utf-8')
#%%
# Open File
resultFyle = open("C:/Users/Desktop/translation1.csv",'wb')

# Create Writer Object
wr = csv.writer(resultFyle, dialect='excel')

# Write Data to File
for item in df_text_new.index:
    resultFyle.write(item.encode('utf-8') + "\n")
resultFyle.close()
        

