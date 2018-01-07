# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 14:23:07 2017

@author: Jitendra Gaur
"""
import requests
import datetime



# Inserting current timestamp
d = datetime.datetime.utcnow() # <-- get time in UTC
timestamp = d.isoformat("T") + "Z"

translation = 'Esto es solo párá practicar'
# Inserting URL and headers(its common for all the operations)
url="https://edrx-test.scm.us2.oraclecloud.com:443/egpItems/ItemServiceV2"
headers = {'content-type': 'text/xml'}


                
body = """<?xml version="1.0" encoding="UTF-8"?>
         <soapenv:Envelope xmlns:cat="http://xmlns.oracle.com/apps/scm/productCatalogManagement/advancedItems/flex/egoItemEff/itemSupplier/categories/" xmlns:cat1="http://xmlns.oracle.com/apps/scm/productCatalogManagement/advancedItems/flex/egoItemEff/itemRevision/categories/" xmlns:cat2="http://xmlns.oracle.com/apps/scm/productCatalogManagement/advancedItems/flex/egoItemEff/item/categories/" xmlns:item="http://xmlns.oracle.com/apps/scm/productModel/items/itemServiceV2/" xmlns:item1="http://xmlns.oracle.com/apps/scm/productModel/items/flex/itemRevision/" xmlns:item2="http://xmlns.oracle.com/apps/scm/productModel/items/flex/item/" xmlns:item3="http://xmlns.oracle.com/apps/scm/productModel/items/flex/itemGdf/" xmlns:mod="http://xmlns.oracle.com/apps/flex/fnd/applcore/attachments/model/" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:typ="http://xmlns.oracle.com/apps/scm/productModel/items/itemServiceV2/types/">
   <soapenv:Header>
      <wsse:Security soapenv:mustUnderstand="1" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
         <wsse:UsernameToken wsu:Id="UsernameToken-1767AEF7A6DA79525B15012351006126">
            <wsse:Username>Username</wsse:Username>
            <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">Password</wsse:Password>
            <wsse:Nonce EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">lwS3jzwrhY8hVnNd7dLHzg==</wsse:Nonce>
            <wsu:Created>"""+str(timestamp)+"""</wsu:Created>
         </wsse:UsernameToken>
         <wsu:Timestamp wsu:Id="TS-1767AEF7A6DA79525B15012351006125">
            <wsu:Created>"""+str(timestamp)+"""</wsu:Created>
            <wsu:Expires>"""+str(timestamp)+"""</wsu:Expires>
         </wsu:Timestamp>
      </wsse:Security>
   </soapenv:Header>
   <soapenv:Body>
       <typ:updateItem>
         <typ:item>
            <item:ItemId>300000008187139</item:ItemId>
            <item:OrganizationId>300000001645066</item:OrganizationId><!--Optional:-->
           <!--Zero or more repetitions:-->
            <item:ItemTranslation>
               <item:ItemDescription>"""+translation+"""</item:ItemDescription>
               <!--Optional:-->
               <item:LongDescription>"""+translation+"""</item:LongDescription>
               <!--Optional:-->
               <item:HTMLLongDescription>"""+translation+"""</item:HTMLLongDescription>
               <!--Optional:-->
               <item:Language>E</item:Language>
               <!--Optional:-->
               <item:SourceLanguage>US</item:SourceLanguage>
              </item:ItemTranslation>
            
         </typ:item>
      </typ:updateItem>
   </soapenv:Body>
</soapenv:Envelope>"""

response = requests.post(url,data=body,headers=headers)
print (response)
obj = response.content
#%%
