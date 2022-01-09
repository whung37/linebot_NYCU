from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

import requests 
from bs4 import BeautifulSoup
import json
#11-45行作用為爬蟲，詳見help內的檔案
urlvac1 = 'https://covid-19.nchc.org.tw/dt_002-csse_covid_19_daily_reports_vaccine_city2.php'
urlvac2 = 'https://www.aweb.tpin.idv.tw/COVID-19/vaccine.php' 
urltwn = 'https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=4001&limited=TWN'
urlwrl = 'https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=3001&limited=OWID_WRL'

rvac1 = requests.get(urlvac1)
spvac1 = BeautifulSoup(rvac1.text,'lxml')
first_vaccinated_vac1=str(spvac1.select("body div div div small"))
tempvac1=first_vaccinated_vac1.replace("<small>","").replace("</small>"," ").split("<br/>")

rvac2 = requests.get(urlvac2)
spvac2 = BeautifulSoup(rvac2.text,'lxml')
first_vaccinated_vac2=spvac2.select("body table")
ele = first_vaccinated_vac2[6]
ele2 = str(ele)
tempvac2 = ele2.split('#32af1e')
AZ0 = tempvac2[13].split('<td>')[-1]
AZ = int(AZ0.replace('<br/><span style="color:','').replace(',',''))
MD0 = tempvac2[14].split('<td>')[-1]
MD = int(MD0.replace('<br/><span style="color:','').replace(',',''))
BT0 = tempvac2[15].split('<td>')[-1]
BT = int(BT0.replace('<br/><span style="color:','').replace(',',''))
MV0 = tempvac2[16].split('<td>')[-1]
MV = int(MV0.replace('<br/><span style="color:','').replace(',',''))
ALL = AZ + MD + BT + MV

strvaccine = str('疫苗覆蓋率：\n'+(tempvac1[0].replace("[% , ",""))+'\n'+(tempvac1[1])+'\nAZ疫苗剩餘量：'+format(AZ, ',d')+'\n莫德納疫苗剩餘量：'+format(MD, ',d')+'\nBNT疫苗剩餘量：'+format(BT, ',d')+'\n高端疫苗剩餘量：'+format(MV, ',d')+'\n總計疫苗剩餘量：'+format(ALL, ',d'))

rtwn = requests.get(urltwn)
dictwn=json.loads(rtwn.text)   
strtwn = '全台總計確診數：\n'+(format(int(dictwn[0]['a05']), ',d'))+'\n當日新增確診數：\n'+(format(int(dictwn[0]['a06']), ',d'))+'\n全台總計死亡數：\n'+(format(int(dictwn[0]['a08']), ',d'))+'\n當日新增死亡數：\n'+(format(int(dictwn[0]['a09']), ',d'))

rwrl = requests.get(urlwrl)
dicwrl=json.loads(rwrl.text)   
strwrl = '全球總計確診數：\n'+(format(int(dicwrl[0]['a05']), ',d'))+'\n當日新增確診數：\n'+(format(int(dicwrl[0]['a06']), ',d'))+'\n全球總計死亡數：\n'+(format(int(dicwrl[0]['a08']), ',d'))+'\n當日新增死亡數：\n'+(format(int(dicwrl[0]['a09']), ',d'))

def vaccine(event):  #傳送'@疫苗資訊'會進入
    try:
        message = TextSendMessage(  
            text = strvaccine
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def twnnum(event):  #傳送'@台灣疫情'會進入
    try:
        message = TextSendMessage(  
            text = strtwn
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def wrlnum(event):  #傳送'@世界疫情'會進入
    try:
        message = TextSendMessage(  
            text = strwrl
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def news(event):  #傳送'@新聞'會進入
    try:
        message = TextSendMessage(  
            text = 'https://www.google.com.tw/search?sxsrf=AOaemvL3HodLbx4QIz3Gz91u1eSPQu6FVQ:1641617003194&source=lnms&tbm=nws&q=COVID-19&sa=X&ved=2ahUKEwjAgdTyq6H1AhUuyYsBHXctAAgQ_AUoAXoECAIQAw&biw=1201&bih=541&dpr=1.6'
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def vac2(event):  #傳送'@各類疫苗剩餘量'會進入
    try:
        message = TextSendMessage(  
            text = 'https://www.aweb.tpin.idv.tw/COVID-19/vaccine_buy.php'
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def qr(event):  #傳送'@qrcode'會進入，該網址可以開啟line自身的掃描功能
    try:
        message = TextSendMessage(  
            text = 'https://line.me/R/nv/QRCodeReader'
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def soapp(event):  #傳送'@台灣社交距離app'會進入
    try:
        message = TextSendMessage(  
            text = 'https://play.google.com/store/apps/details?id=tw.gov.cdc.exposurenotifications&hl=zh_TW&gl=US'
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendQuickreply(event):  #傳送其他文字訊息時會進入，開啟快速選單
    try:
        message = TextSendMessage(
            text='等待專人回覆，或請選擇下列選項',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="新聞", text="@新聞")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="各類疫苗剩餘", text="@各類疫苗剩餘量")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="防疫實聯制", text="@qrcode")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="台灣社交距離app下載", text="@台灣社交距離app")
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
