# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 12:27:09 2017

@author: Jitendra Gaur
"""
#importing required python libraries
import pandas as pd
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator

#Reading data from excel file
df = pd.read_excel(open('C:\Users\IBM_ADMIN\Documents\Project\OTIS\Manoj_Part Center Cdty Code_uniqe.xlsx','rb'), sheetname='Without Duplicates')
#%%
#Creating dataframe
d = {'S.No.' : range(0,20000)}
df_text_new = pd.DataFrame(d)
df_text_new['Product_Itemcode'] = ''
df_text_new['Product_Desc_English'] = ''
df_text_new['Product_Desc_French'] = ''
       

#%%
#Authentication for WLT API

language_translator = LanguageTranslator(username='f86aed4d-a3ce-4b36-aa7a-7ded4ba8a4f8', password='cFxxnNuVRbX1')
#%%

product_desc_fr = []
product_desc_esp = []
product_desc_ger = []
#product_desc_ger = []
#product_name_chi = []
#product_desc_chi = []
i=0
#Running the loop to read from excel and translating using WLT for 20K product description
for i in range(0,20000):
    translation = language_translator.translate(
        text = df['Product_Details'][i],
        source='en',
        target='fr')
    product_desc_fr.append(translation)
    print i


#%%
# Writing details to data frame
for j in range(0,20000):
    df_text_new['Product_Itemcode'][j] = df['ITEM_CODE(Assumption)'][j]
    df_text_new['Product_Desc_English'][j] = df['Product_Details'][j]
    df_text_new['Product_Desc_French'][j] = product_desc_fr[j]
    
#%%        
#Writing data frame to CSV
df_text_new.to_csv('translation_French20000.csv', encoding='utf-8')

        

