import requests
import random
from time import sleep
from essential_generators import DocumentGenerator
channel_id='CHANNEL ID'
channel_id1='CHANNEL ID 1'
channel_id2='CHANNEL ID 2'
channel_id3='CHANNEL ID 3'
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

    
    sleep(random.randint(360,750))

def sendMessage1(token, channel_id1, message):
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id1)
    data = {"content": message}
    header = {"authorization": token}

    r = requests.post(url, data=data, headers=header)
    if r.status_code == 200:
        print("random message sent")
    else:
        print(r.status_code)

    
    sleep(random.randint(360,750))
    

def sendMessage2(token, channel_id2, message):
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id2)
    data = {"content": message}
    header = {"authorization": token}

    r = requests.post(url, data=data, headers=header)
    if r.status_code == 200:
        print("random message sent")
    else:
        print(r.status_code)

    
    sleep(random.randint(360,750))


def sendMessage3(token, channel_id3, message):
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id3)
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
        sendMessage(token,channel_id1,random.choice(message))
        sendMessage(token,channel_id2,random.choice(message))
        sendMessage(token,channel_id3,random.choice(message))
    except Exception as e:
        sleep(360)
        print(e)
    
