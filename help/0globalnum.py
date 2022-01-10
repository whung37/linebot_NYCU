import requests 
import json
url = 'https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=3001&limited=OWID_WRL'
r = requests.get(url)#抓出網頁代碼
dic=json.loads(r.text)#轉換格式
allinf = dic[0]['a05']#取出所需資料
dayinf = dic[0]['a06']
alldie = dic[0]['a08']
daydie = dic[0]['a09']

glonum = '全球總計確診數：'+dic[0]['a05']+'\n當日新增確診數：'+dic[0]['a06']+'\n全球總計死亡數：'+dic[0]['a08']+'\n當日新增死亡數：'+dic[0]['a09']

print(glonum)
#本程式僅為參考用，與專案架構無關