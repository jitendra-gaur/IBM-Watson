# -*- coding: utf-8 -*-
"""
Created on Sun Oct 01 10:07:25 2017

@author: IBM_ADMIN
"""

import pandas as pd
import ibm_db
ibm_db_conn = ibm_db.connect("DATABASE="+"BLUDB"+";HOSTNAME="+"awh-yp-small02.services.dal.bluemix.net"+";PORT="+"50000"+";PROTOCOL=TCPIP;UID="+"dash111407"+";PWD="+"z_AOy_v0H5Ja"+";", "","")
import ibm_db_dbi
conn = ibm_db_dbi.Connection(ibm_db_conn)

df = pd.read_csv('C:/Users/IBM_ADMIN/Documents/Project/CAI Offering/testing1.csv')
#df = pd.read_csv('C:/Users/IBM_ADMIN/Documents/Project/CAI Offering/test.csv')
#df=pd.read_sql("SELECT * FROM ACCOUNT_LEADERS",conn)
#df = pd.read_csv('C:/Users/IBM_ADMIN/Documents/Project/CAI Offering/CAI_Pipeline_28Sep17.csv')

#%%
query = "Delete from TEST1"
#query = "Delete from TEST"
print query
stmt = ibm_db.exec_immediate(ibm_db_conn, query)
print stmt
#%%

for i in xrange(0,len(df)):
    query = "INSERT INTO TEST1 (EMAILID, TIMESTAMP, OFFERING1, OFFERING2, OFFERING3, OS, LOCATION, DOCUMENT, MOB) VALUES('"+str(df.EMAILID[i])+"','"+str(df.TIMESTAMP[i])+"','"+str(df.OFFERING1[i])+"','"+str(df.OFFERING2[i])+"','"+str(df.OFFERING3[i])+"','"+str(df.OS[i])+"','"+str(df.LOCATION[i])+"','"+str(df.DOCUMENT[i])+"','"+str(df.MobileNumber[i])+"')"
    #query = "INSERT INTO TEST (EMAILID, TIMESTAMP, OFFERING1, OFFERING2, OFFERING3, OS, LOCATION, DOCUMENT) VALUES('"+df.EMAILID[i]+"','"+df.TIMESTAMP[i]+"','"+df.OFFERING1[i]+"','"+df.OFFERING2[i]+"','"+df.OFFERING3[i]+"','"+df.OS[i]+"','"+df.LOCATION[i]+"','"+df.DOCUMENT[i]+"')"
    
    print query
    stmt = ibm_db.exec_immediate(ibm_db_conn, query)
    #print stmt

#%%
for i in xrange(0,len(df)):
    query = "INSERT INTO CAI_PIPELINE_TMP (Opp No, Dom Client ID, Geo, Market, Level 20, Report Unit Code, Customer, ISU/GB Segment, Opp Name, Rev/Signings Value ($M), Sales Stage Name, SSM Step Name, Fcst/Dec Period, Fcst/Dec Date, Industry, Top Opp RANK, Cov Type ID, Customer Set, Level 20 Description, Category Code List, Level 30 Desc, Opp Owner User Name, OI Emp User Name, Country Name, Curr Cov ID, PPV ($M), BP ID, BP Company, Archive Reason, Campaign List, Level 30, Level 30 Description, CMR Sector, CMR ISU Code, Deal Size, Decision Date, Fcst/Dec Qtr, Contract Duration, Segment, Subsegment, Tier, Line item owner Notes ID, ISU, ISU Sector, ISU Group, Opp Create Date, Elapsed Days in S/S, Bill Date, RM Status, OI Source, Global Buying Group ID, GBS Top Account, Account Type, Level 17, Contract Type, Contract Type Code, Contract Booking, Contract Booking Code, Odds) VALUES('"+str(df.OppNo[i])+"','"+str(df.DomClientID[i])+"','"+str(df.Geo[i])+"','"+str(df.Market[i])+"','"+str(df.Level20[i])+"','"+str(df.ReportUnitCode[i])+"','"+str(df.Customer[i])+"','"+str(df.ISU_GBSegment[i])+"','"+str(df.OppName[i])+"','"+str(df.Rev_SigningsValue[i])+"','"+str(df.SalesStageName[i])+"','"+str(df.SSMStepName[i])+"','"+str(df.Fcst_DecPeriod[i])+"','"+str(df.Fcst_DecDate[i])+"','"+str(df.Industry[i])+"','"+str(df.TopOppRANK[i])+"','"+str(df.CovTypeID[i])+"','"+str(df.CustomerSet[i])+"','"+str(df.Level20Description[i])+"','"+str(df.CategoryCodeList[i])+"','"+str(df.Level30Desc[i])+"','"+str(df.OppOwnerUserName[i])+"','"+str(df.OIEmpUserName[i])+"','"+str(df.CountryName[i])+"','"+str(df.CurrCovID[i])+"','"+str(df.PPV[i])+"','"+str(df.BPID[i])+"','"+str(df.BPCompany[i])+"','"+str(df.ArchiveReason[i])+"','"+str(df.CampaignList[i])+"','"+str(df.Level30[i])+"','"+str(df.Level30Description[i])+"','"+str(df.CMRSector[i])+"','"+str(df.CMRISUCode[i])+"','"+str(df.DealSize[i])+"','"+str(df.DecisionDate[i])+"','"+str(df.Fcst_DecQtr[i])+"','"+str(df.ContractDuration[i])+"','"+str(df.Segment[i])+"','"+str(df.Subsegment[i])+"','"+str(df.Tier[i])+"','"+str(df.LineitemownerNotesID[i])+"','"+str(df.ISU[i])+"','"+str(df.ISUSector[i])+"','"+str(df.ISUGroup[i])+"','"+str(df.OppCreateDate[i])+"','"+str(df.ElapsedDaysinS_S[i])+"','"+str(df.BillDate[i])+"','"+str(df.RMStatus[i])+"','"+str(df.OISource[i])+"','"+str(df.GlobalBuyingGroupID[i])+"','"+str(df.GBSTopAccount[i])+"','"+str(df.AccountType[i])+"','"+str(df.Level17[i])+"','"+str(df.ContractType[i])+"','"+str(df.ContractTypeCode[i])+"','"+str(df.ContractBooking[i])+"','"+str(df.ContractBookingCode[i])+"','"+str(df.Odds[i])+"')"
    print query
    stmt = ibm_db.exec_immediate(ibm_db_conn, query)
    #print stmt

#%%
df.to_sql(name='TEST_TABLE', con=conn, flavor=None, schema='SCHEMA1', if_exists='append', index=True, index_label=None, chunksize=None, dtype=None)