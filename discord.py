import requests
import random
from time import sleep
channel_id='CHANNEL ID'
token='YOUR ACCOUNT TOKEN'

def sendMessage(token, channel_id, message):
    try:
        url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
        data = {"content": message}
        header = {"authorization": token}

        r = requests.post(url, data=data, headers=header)
        if r.status_code == 200:
            print(f'quote sent: {message} \n')
        else:
            print(r.status_code)
    except Exception as e:
        print(e)

    
    sleep(random.randint(360,650))


while True:
    try:
        response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
        if response.status_code == 200:
            json_data = response.json()
            data = json_data['data']
            message=data[0]['quoteText']
        else:
            message=['who dey zuzu','whats up guys', 'spap nice one', 'comrades how far', 'happy sunday', 'whats poping']
        sendMessage(token,channel_id,message)
    except Exception as e:
        sleep(360)
        print(e)
    
