
# coding: utf-8

# In[1]:


import threading
import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[2]:


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('realace2018-firebase-adminsdk-r7gk1-121be5edaf.json')

# Initialize the app with a service account, granting admin privileges
app=firebase_admin.initialize_app(cred, {
   'databaseURL': 'https://realace2018.firebaseio.com/'
})
ref=db.reference()


# In[3]:


serviceKey='F%2FxP1NfaTBhw0giVbsH7HTUMMnbJF6p9LhD9p8mJ4HpucMsVcxUzoTw4RxZDFdnRP3NgWj0IwJke%2FOzfe5VxhA%3D%3D'
numOfRows=[25, 16, 8, 9, 5, 5, 5, 31, 6, 7, 14, 12, 9, 1, 9, 9, 3]
sidoName=['서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '세종', '경북', '경남', '제주']


# In[33]:


def func():
    timer=threading.Timer(3600,func)
    
    for number in range(0,17):
        url='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?serviceKey='+str(serviceKey)+'&numOfRows='+str(numOfRows[number])+'&pageSize=10&pageNo=1&startPage=1&sidoName='+str(sidoName[number])+'&searchCondition=DAILY'
        html=requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
    
        citylist=[]
        pm10list=[]
        timelist=[]
        so2list=[]
        colist=[]
        o3list=[]
        no2list=[]
        

        datatime=soup.find_all('datatime')
        cityname=soup.find_all('cityname')
        so2value=soup.find_all('so2value')
        covalue=soup.find_all('covalue')
        o3value=soup.find_all('o3value')
        no2value=soup.find_all('no2value')
        pm10vale=soup.find_all('pm10value')
        

        for code in datatime:
            timelist.append(code.text)
        for code in cityname:
            citylist.append(code.text)
        for code in pm10vale:
            pm10list.append(code.text)
        for code in so2value:
            so2list.append(code.text)
        for code in covalue:
            colist.append(code.text)
        for code in o3value:
            o3list.append(code.text)
        for code in no2value:
            no2list.append(code.text)
            
    
    
    
        numb=numOfRows[number]
    
        for num in range(0,numb):
            users_ref= ref.child('air')
            users_ref.push({'sidoname':sidoName[number],'cityname':citylist[int(num)],'pm10vale':pm10list[int(num)], 
                            'so2value':so2list[int(num)], 'covalue':colist[int(num)], 'o3value':o3list[int(num)], 'no2value':no2list[int(num)], 'datatime':timelist[int(num)]})
    
    timer.start()

func()

