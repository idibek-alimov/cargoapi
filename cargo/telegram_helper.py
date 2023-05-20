from django.conf import settings
import telegram
import requests

class Telegram():
    # def send_massage(message):
    #     telegram_settings = settings.TELEGRAM
    #     # bot = telegram.Bot(token=telegram_settings['bot_token'])
    #     # bot.send_message(chat_id="@%s" % telegram_settings['channel_name'],
    #     #              text=message_html, parse_mode=telegram.ParseMode.HTML)    
    #     bot = telegram.Bot(token=telegram_settings["bot_token"])
    #     bot.send_message(chat_id="@%s" % telegram_settings["channel_name"],text=message)#,parse_mode=telegram.ParseMode.HTML)

    def send_massage(message):
        telegram_settings = settings.TELEGRAM
        token = telegram_settings["bot_token"]
        chat_id = telegram_settings["chat_id"]

        #url = f"https://api.telegram.org/bot{token}/getUpdates"
        #url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        ##message = "stupid ass fart saving carpet store motherfucker.Move"
        #message = "I am piccle Riiick"
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        #print(requests.get(url).json)
        requests.get(url).json()

# TOKEN = '5878843070:AAElCdzYOVjGlplNWNKgi_OTiL6W1dJu2PQ'
# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# print(requests.get(url).json())