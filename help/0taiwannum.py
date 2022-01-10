import requests
import json
r=requests.get('https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=4001&limited=TWN')
#抓出網頁代碼
dic=json.loads(r.text)   
#轉換格式
twnnum = '全台總計確診數：'+dic[0]['a05']+'\n當日新增確診數：'+dic[0]['a06']+'\n全台總計死亡數：'+dic[0]['a08']+'\n當日新增死亡數：'+dic[0]['a09']#取出所需資料

print(twnnum)
#本程式僅為參考用，與專案架構無關