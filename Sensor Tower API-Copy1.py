#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import requests
import json
import pygsheets
import ipywidgets as widgets
from datetime import date


# In[ ]:


#pip install ipywidgets


# In[45]:

#this generate the widgets for date star and end

today = date.today()

start_date=widgets.Text(
    value=today.strftime("%Y-%m-%d"),
    placeholder='Type something',
    description='Start Date:',
    disabled=False
)
start_date


# In[46]:

#this generate the widgets for date star and end

end_date=widgets.Text(
    value=today.strftime("%Y-%m-%d"),
    placeholder='Type something',
    description='end_date:',
    disabled=False
)
end_date


# In[57]:
#you should generate an API token in sensor tower (this shows how to do it https://help.sensortower.com/hc/en-us/articles/7335038067611-Generate-an-API-Token) and add it to this url

#this is fixed for this GO apps codes: com.dreamgames.royalmatch, com.gamegos.mobile.manorcafe,com.matchington.mansion
#and for this countries: AE,CAO,CAR,CAT,CAU,CAZ,CBB,CBE,CBG,CBH,CBM,CBO,CBR,CBY,CCA,CCH,CCL,CCO,CCR,CCY,CCZ,CDE,CDK,CDO,CDZ,CEC,CEE,CEG,CES,CFI,CFR,CGB,CGE,CGH,CGR,CGT,CHK,CHR,CHU,CID,CIE,CIL,CIN,CIT,CJP,CKE,CKH,CKR,CKW,CKZ,CLB,CLK,CLT,CLU,CLV,CMG,CMO,CMT,CMX,CMY,CNG,CNI,CNL,CNO,CNZ,COM,CPA,CPE,CPH,CPK,CPL,CPT,CPY,CQA,CRO,CRS,CRU,CSA,CSE,CSG,CSI,CSK,CSV,CTH,CTN,CTR,CTW,CUA,CUS,CUY,CUZ,CVE,CVN,CZA

APP_ANDROID_INFO = 'https://api.sensortower.com/v1/android/sales_report_estimates?app_ids=com.dreamgames.royalmatch                    %2Ccom.gamegos.mobile.manorcafe%2Ccom.matchington.                    mansion&countries=AE%2CAO%2CAR%2CAT%2CAU%2CAZ%2CBB%2CBE%2CBG%2CBH%2CBM%2CBO%2CBR%2CBY%2CCA%2CCH%2CCL%2CCO%2CCR%2CCY%2CCZ%2CDE%2CDK%2CDO%2CDZ%2CEC%2CEE%2CEG%2CES%2CFI%2CFR%2CGB%2CGE%2CGH%2CGR%2CGT%2CHK%2CHR%2CHU%2CID%2CIE%2CIL%2CIN%2CIT%2CJP%2CKE%2CKH%2CKR%2CKW%2CKZ%2CLB%2CLK%2CLT%2CLU%2CLV%2CMG%2CMO%2CMT%2CMX%2CMY%2CNG%2CNI%2CNL%2CNO%2CNZ%2COM%2CPA%2CPE%2CPH%2CPK%2CPL%2CPT%2CPY%2CQA%2CRO%2CRS%2CRU%2CSA%2CSE%2CSG%2CSI%2CSK%2CSV%2CTH%2CTN%2CTR%2CTW%2CUA%2CUS%2CUY%2CUZ%2CVE%2CVN%2CZA&date                    _granularity=daily&start_date='+start_date.value+'&end_date='+end_date.value+'&auth_token=here_goes_your_api_token'


# In[58]:
#you should generate an API token in sensor tower and add it to this url

#this is fixed for this iOS apps codes: 1195621598,1216575026,1228655110,1358742711,201482155847,201570403223
#and for this countries: AE,AO,AR,AT,AU,AZ,BB,BE,BG,BM,BO,BR,BY,CA,CH,CL,CN,CO,CR,CZ,DE,DK,DO,DZ,EC,EE,EG,ES,FI,FR,GB,GH,GR,GT,HK,HR,HU,ID,IE,IL,IN,IT,JP,KE,KH,KR,KW,KZ,LB,LK,LT,LU,LV,MG,MO,MX,MY,NG,NI,NL,NO,NZ,OM,PA,PE,PH,PK,PL,PT,PY,QA,RO,RU,SA,SE,SG,SI,SK,SV,TH,TN,TR,TW,UA,US,UY,UZ,VE,VN,ZA,BH,CY,GE,MT,RS,WW

APP_IOS_INFO ='https://api.sensortower.com/v1/ios/sales_report_estimates?app_ids=                1195621598%2C1216575026%2C1228655110%2C1358742711%2C%201482155847%2C%201570403223%2C&countries                =AE%2CAO%2CAR%2CAT%2CAU%2CAZ%2CBB%2CBE%2CBG%2CBM%2CBO%2CBR%2CBY%2CCA%2CCH%2CCL%2CCN%2CCO%2CCR%2CCZ%2CDE%2CDK%2CDO%2CDZ%2CEC%2CEE%2CEG%2CES%2CFI%2CFR%2CGB%2CGH%2CGR%2CGT%2CHK%2CHR%2CHU%2CID%2CIE%2CIL%2CIN%2CIT%2CJP%2CKE%2CKH%2CKR%2CKW%2CKZ%2CLB%2CLK%2CLT%2CLU%2CLV%2CMG%2CMO%2CMX%2CMY%2CNG%2CNI%2CNL%2CNO%2CNZ%2COM%2CPA%2CPE%2CPH%2CPK%2CPL%2CPT%2CPY%2CQA%2CRO%2CRU%2CSA%2CSE%2CSG%2CSI%2CSK%2CSV%2CTH%2CTN%2CTR%2CTW%2CUA%2CUS%2CUY%2CUZ%2CVE%2CVN%2CZA%2CBH%2CCY%2CGE%2CMT%2CRS%2CWW%2C&date                _granularity=daily&start_date='+start_date.value+'&end_date='+end_date.value+'&auth_token=here_goes_your_api_token'


# In[59]:


#request GO
response_API_go = requests.get(APP_ANDROID_INFO)

#request iOS
response_API_ios = requests.get(APP_IOS_INFO)


# In[60]:


#test API connection (code 200 means connection is OK)
print(response_API_go.status_code)


# In[61]:


#test API connection (code 200 means connection is OK)
print(response_API_ios.status_code)


# In[62]:


go_data=response_API_go.json()

go_data_df=pd.DataFrame(go_data[0], index=[0])


# In[63]:


for i in range(1,len(go_data)):
    df=pd.DataFrame(go_data[i], index=[0])
    go_data_df=go_data_df.append(df,ignore_index=True)
    
    
go_data_df.columns = ['App_id', 'Country', 'Date', 'Downloads', 'Revenue']


# In[64]:


go_data_df


# In[65]:


ios_data=response_API_ios.json()

ios_data_df=pd.DataFrame(ios_data[0], index=[0])


# In[66]:


for i in range(1,len(ios_data)):
    df=pd.DataFrame(ios_data[i], index=[0])
    ios_data_df=ios_data_df.append(df,ignore_index=True)


ios_data_df.columns = ['App_id', 'Country', 'Date', 'iPad Downloads', 'iPad Revenue', 'iPhone Downloads', 'iPhone Revenue']


# In[67]:


ios_data_df


# In[68]:


#google sheets API authorization 
#you need to generate the credentials for google drive API following this ttutorial https://erikrood.com/Posts/py_gsheets.html
gc = pygsheets.authorize(service_file='/Users/SMRB1/Documents/28. TicToc Games/st_credentials.json')


# In[71]:


#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('Sensor Tower Data')

#select the first sheet 
wks = sh[0]

#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(go_data_df,(1,1))


# In[70]:


#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('Sensor Tower Data')

#select the first sheet 
wks = sh[1]

#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(ios_data_df,(1,1))
