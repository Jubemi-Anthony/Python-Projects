import requests
import schedule
import time
mobile_number = "08120210738"

def sendMessage():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': "Hi Jubemi, This is from Python. I chose you because you're number 1",
        'key': 'textbelt',
    })
    print(resp.json())

# schedule.every().day.at('06:00').do(sendMessage)
schedule.every(10).seconds.do(sendMessage)

while True:
    schedule.run_pending()
    time.sleep(1)