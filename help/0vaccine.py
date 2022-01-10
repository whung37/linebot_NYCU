import requests 
from bs4 import BeautifulSoup
url = 'https://covid-19.nchc.org.tw/dt_002-csse_covid_19_daily_reports_vaccine_city2.php'
r = requests.get(url)#抓出網頁代碼
sp = BeautifulSoup(r.text,'lxml')#轉換格式

first_vaccinated=str(sp.select("body div div div small"))#取出所需資料
temp=first_vaccinated.replace("<small>","").replace("</small>"," ").split("<br/>")#將資料進行處理，成為串列
strvaccine = str('疫苗覆蓋率：\n'+(temp[0].replace("[% , ",""))+'\n'+(temp[1]))#找出串列中所需資料的位置進行加工
print(strvaccine)
#本程式僅為參考用，與專案架構無關