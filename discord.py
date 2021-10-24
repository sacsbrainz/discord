import requests
import random
from time import sleep
from essential_generators import DocumentGenerator
channel_id='CHANNEL ID'
token='YOUR ACCOUNT TOKEN'
gen = DocumentGenerator()
message=gen.sentence()

def sendMessage(token, channel_id, message):
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
    data = {"content": message}
    header = {"authorization": token}

    r = requests.post(url, data=data, headers=header)
    if r.status_code == 200:
        print("random message sent")
    else:
        print(r.status_code)

    
    sleep(random.randint(360,650))

    


while True:
    try:
        sendMessage(token,channel_id,message)
    except Exception as e:
        sleep(360)
        print(e)
    
