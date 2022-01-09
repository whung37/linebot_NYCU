from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage
from module import func

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)#取得官方帳號的CHANNEL ACCESS TOKEN
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)#取得官方帳號的CHANNEL SECRET

@csrf_exempt
def callback(request):#進行回應(函式用在urls檔)
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:#按照順序處理全部事件
            if isinstance(event, MessageEvent):#檢查是否是訊息事件
                if isinstance(event.message, TextMessage):#檢查是否是文字訊息
                    mtext = event.message.text
                    if mtext == '@疫苗資訊':#判斷是否屬於以下關鍵字，開始執行所屬函式
                        func.vaccine(event)
    
                    elif mtext == '@台灣疫情':
                        func.twnnum(event)
    
                    elif mtext == '@世界疫情':
                        func.wrlnum(event)

                    elif mtext == '@新聞':
                        func.news(event)
                    
                    elif mtext == '@各類疫苗剩餘量':
                        func.vac2(event)

                    elif mtext == '@qrcode':
                        func.qr(event)
                    
                    elif mtext == '@台灣社交距離app':
                        func.soapp(event)
    
                    else :
                        func.sendQuickreply(event)
    
        return HttpResponse()

    else:
        return HttpResponseBadRequest()
