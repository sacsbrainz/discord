import requests
import random
from time import sleep
channel_id='CHANNEL ID'
token='YOUR ACCOUNT TOKEN'
message=['who dey zuzu','whats up guys', 'spap nice one', 'comrades how far', 'happy sunday', 'whats poping']


def sendMessage(token, channel_id, message):
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
    data = {"content": message}
    header = {"authorization": token}

    r = requests.post(url, data=data, headers=header)
    if r.status_code == 200:
        print("random message sent")
    else:
        print(r.status_code)

    
    sleep(random.randint(360,750))
    

while True:
    try:
        sendMessage(token,channel_id,random.choice(message))
    except Exception as e:
        sleep(360)
        print(e)
    