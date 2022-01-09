import requests 
from bs4 import BeautifulSoup
import json
url = 'https://www.aweb.tpin.idv.tw/COVID-19/vaccine.php'
r = requests.get(url)#抓出網頁代碼
sp = BeautifulSoup(r.text,'lxml')#轉換格式
first_vaccinated=sp.select("body table")#取出所需資料

ele = first_vaccinated[6]
ele2 = str(ele)
temp = ele2.split('#32af1e')#將資料進行處理，成為串列
AZ0 = temp[13].split('<td>')[-1]#找出串列中所需資料的位置進行加工
AZ = int(AZ0.replace('<br/><span style="color:','').replace(',',''))
MD0 = temp[14].split('<td>')[-1]
MD = int(MD0.replace('<br/><span style="color:','').replace(',',''))
BT0 = temp[15].split('<td>')[-1]
BT = int(BT0.replace('<br/><span style="color:','').replace(',',''))
MV0 = temp[16].split('<td>')[-1]
MV = int(MV0.replace('<br/><span style="color:','').replace(',',''))
ALL = AZ + MD + BT + MV
#本程式僅為參考用，與專案架構無關