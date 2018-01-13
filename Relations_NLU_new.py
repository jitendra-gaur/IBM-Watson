# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 22:47:50 2016

@author: Jitendra Gaur
"""

projectPath = 'C:/Users/Documents/copy txt files/copy txt files'
import os
#import time
#import json
import pandas as pd
from fuzzywuzzy import fuzz

import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 \
  as Features
#%%
os.chdir(projectPath)
natural_language_understanding = NaturalLanguageUnderstandingV1(
  username="username",
  password="password",
  version="2017-02-27")
#%%
doc_text = pd.read_csv("C:/Users/IBM_ADMIN/Documents/Project/First American/copy txt files/copy txt files/harsh_remainingfiles_torunforrelations.csv")
df_text = pd.DataFrame(doc_text)
d = {'Tracker' : range(0,800000)}
df_ents = pd.DataFrame(d)
df_ents['Filename'] = ''
df_ents['Subject'] = ''
df_ents['Action'] = ''
df_ents['Object'] = ''
df_ents['Sentence'] = ''

ptr = 0
ctr = 0

#%%

for i in range(0,5):
    doc_file = open("C:/Users/IBM_ADMIN/Documents/Project/First American/copy txt files/copy txt files/" + str(df_text.Filename[i])).read()
    demo_text = doc_file   
        
    print i
    response = natural_language_understanding.analyze(text = demo_text, features=[Features.Relations(), Features.SemanticRoles()])
    
       # time.sleep(2)
    ctr = ctr + 1
        #if j==2:
    #   time.sleep(5)

    for relation in response['semantic_roles']:
        df_ents.Filename[ptr] = df_text.Filename[i]
                
        relation_list = relation.keys()
        if any("subject" in s for s in relation_list):
            df_ents.Subject[ptr] = relation['subject']['text'].encode('utf-8')
        else: 
            df_ents.Subject[ptr] = ""
        if any("action" in s for s in relation_list):
            df_ents.Action[ptr] = relation['action']['text'].encode('utf-8')
        else: 
            df_ents.Action[ptr] = ""
        if any("object" in s for s in relation_list):
            df_ents.Object[ptr] = relation['object']['text'].encode('utf-8')
        else: 
            df_ents.Object[ptr] = ""
        #if any("sentence" in s for s in relation_list):
        #    df_ents.Sentence[ptr] = relation['sentence']['text'].encode('utf-8')
        #else: 
        #    df_ents.Sentence[ptr] = ""
            
            
        #df_ents.Subject[ptr] = relation['subject']['text'].encode('utf-8')
        #df_ents.Action[ptr] = relation['action']['text'].encode('utf-8')
        #df_ents.Object[ptr] = relation['object']['text'].encode('utf-8')
        df_ents.Sentence[ptr] = relation['sentence'].encode('utf-8')
                
        ptr = ptr+1
#%%
   

     
#%%
df_ents.to_csv('Alchemy_entities_allrelations_firstbatch2_30Nov_harshremainingfiles.csv')
#%%    
'''
#Keyword Extraction 

response = alchemyapi.keywords('text', demo_text, {'sentiment': 1})
if response['status'] == 'OK':
    for keyword in response['keywords']:
        Keyword = keyword['text'].encode('utf-8')
        KW_Relevance = keyword['relevance']
        Sentiment = keyword['sentiment']['type']
        if 'score' in keyword['sentiment']:
            SentiScore = keyword['sentiment']['score']


#Relation Extraction Example 
#%%
response = alchemyapi.relations('text', demo_text)
if response['status'] == 'OK':
    for relation in response['relations']:
        if 'subject' in relation:
            Subject = relation['subject']['text'].encode('utf-8')

        if 'action' in relation:
            Action =  relation['action']['text'].encode('utf-8')

        if 'object' in relation:
            Object = relation['object']['text'].encode('utf-8')
'''
