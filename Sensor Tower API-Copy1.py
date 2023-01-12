#!/usr/bin/env python
# coding: utf-8

# In[101]:


import argparse
import time
import datetime
import os.path
import pandas as pd
import requests
import json

# if not os.path.exists('results'):
#     os.mkdir('results')

# def date(string):
#     time.strptime(string, "%Y-%m")
#     return string
# print()
# parser = argparse.ArgumentParser(description='Sensor Tower utility script. Query estimated app downloads and revenue.\nPut your api token inside the token.txt file')
# parser.add_argument('--date', type=date, help='yyyy-mm. The month of the required app statistics. Defaults to last month.')
# parser.add_argument('--category', default='6014', help='string. The app category')
# parser.add_argument('--min-download', default=300000, type=int, help='integer. The minimum number of downloads. Defaults to 300000')
# parser.add_argument('--min-contribution', default=0.5, type=float, help='(0,1). The minimum contribution ratio. Defaults to 0.5')
# args = parser.parse_args()


# In[151]:


APP_ANDROID_INFO = 'https://api.sensortower.com/v1/android/sales_report_estimates?app_ids=com.dreamgames.royalmatch                    %2Ccom.gamegos.mobile.manorcafe%2Ccom.matchington.                    mansion&countries=AE%2CAO%2CAR%2CAT%2CAU%2CAZ%2CBB%2CBE%2CBG%2CBH%2CBM%2CBO%2CBR%2CBY%2CCA%2CCH%2CCL%2CCO%2CCR%2CCY%2CCZ%2CDE%2CDK%2CDO%2CDZ%2CEC%2CEE%2CEG%2CES%2CFI%2CFR%2CGB%2CGE%2CGH%2CGR%2CGT%2CHK%2CHR%2CHU%2CID%2CIE%2CIL%2CIN%2CIT%2CJP%2CKE%2CKH%2CKR%2CKW%2CKZ%2CLB%2CLK%2CLT%2CLU%2CLV%2CMG%2CMO%2CMT%2CMX%2CMY%2CNG%2CNI%2CNL%2CNO%2CNZ%2COM%2CPA%2CPE%2CPH%2CPK%2CPL%2CPT%2CPY%2CQA%2CRO%2CRS%2CRU%2CSA%2CSE%2CSG%2CSI%2CSK%2CSV%2CTH%2CTN%2CTR%2CTW%2CUA%2CUS%2CUY%2CUZ%2CVE%2CVN%2CZA&date                    _granularity=daily&start_date=2023-01-05&end_date=2023-01-11&auth_token=ST0_csRybKRh_Jpx4TNtK2yZ7ei'


# In[236]:


APP_IOS_INFO ='https://api.sensortower.com/v1/ios/sales_report_estimates?app_ids=                1195621598%2C1216575026%2C1228655110%2C1358742711%2C%201482155847%2C%201570403223%2C&countries                =AE%2CAO%2CAR%2CAT%2CAU%2CAZ%2CBB%2CBE%2CBG%2CBM%2CBO%2CBR%2CBY%2CCA%2CCH%2CCL%2CCN%2CCO%2CCR%2CCZ%2CDE%2CDK%2CDO%2CDZ%2CEC%2CEE%2CEG%2CES%2CFI%2CFR%2CGB%2CGH%2CGR%2CGT%2CHK%2CHR%2CHU%2CID%2CIE%2CIL%2CIN%2CIT%2CJP%2CKE%2CKH%2CKR%2CKW%2CKZ%2CLB%2CLK%2CLT%2CLU%2CLV%2CMG%2CMO%2CMX%2CMY%2CNG%2CNI%2CNL%2CNO%2CNZ%2COM%2CPA%2CPE%2CPH%2CPK%2CPL%2CPT%2CPY%2CQA%2CRO%2CRU%2CSA%2CSE%2CSG%2CSI%2CSK%2CSV%2CTH%2CTN%2CTR%2CTW%2CUA%2CUS%2CUY%2CUZ%2CVE%2CVN%2CZA%2CBH%2CCY%2CGE%2CMT%2CRS%2CWW%2C&date                _granularity=daily&start_date=2023-01-05&end_date=2023-01-11&auth_token=ST0_csRybKRh_Jpx4TNtK2yZ7ei'


# In[ ]:


#test API connection (code 200 means connection is OK)
print(response_API_go.status_code)


# In[ ]:


#test API connection (code 200 means connection is OK)
print(response_API_ios.status_code)


# In[152]:


response_API_go = requests.get(APP_ANDROID_INFO)

go_data=response_API_go.json()

go_data_df=pd.DataFrame(go_data[0], index=[0])


# In[ ]:


for i in range(1,len(go_data)):
    df=pd.DataFrame(go_data[i], index=[0])
    go_data_df=go_data_df.append(df,ignore_index=True)


# In[298]:


go_data_df


# In[295]:


response_API_ios = requests.get(APP_IOS_INFO)

ios_data=response_API_ios.json()

ios_data_df=pd.DataFrame(ios_data[0], index=[0])


# In[296]:


for i in range(1,len(ios_data)):
    df=pd.DataFrame(ios_data[i], index=[0])
    ios_data_df=ios_data_df.append(df,ignore_index=True)


# In[297]:


ios_data_df

