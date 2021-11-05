import requests
import random
from time import sleep
import discum
from discum.gateway.session import guild
channel_id='DISCORD_CHANNEL_ID'
# token='YOUR_TOKEN'
email='YOUR_DISCORD_EMAIL'
password='YOUR_DISCORD_PASSWORD'


#to login in using you token 
# bot = discum.Client(token=token, log=False)

#to log in using your email and password
bot = discum.Client(email=email, password=password)

def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()

def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession()
    return bot.gateway.session.guild(guild_id).members

print('fetching member list please wait....')
members = get_members('THE_DISCORD_SERVER_ID', 'DISCORD_CHANNEL_ID')
memberslist = []

for memberID in members:
    memberslist.append(memberID)

def send_message(channel_id, message):
    bot.sendMessage(channel_id, message)
    sleep(random.randint(200,490))



LIST=[]

while True:
    try:
        response = requests.get("https://api.quotable.io/random?tags=technology|trading|trade|cryptocurrency|crypto|money|business")
        if response.status_code == 200:
            json_data = response.json()
            message = json_data['content']
        else:
            print('something went wrong using alternative quotes \n')
            message=['who dey zuzu','whats up guys', 'spap nice one', 'comrades how far', 'happy sunday', 'whats poping']

        for line in memberslist:
            for word in line.split():
                LIST.append(word)
        answer = random.choice(LIST)
        answer=int(answer)
        userid= f'<@!{answer}>'
        taguser=userid+message

        
        send_message(channel_id, taguser)
    except Exception as e:
        sleep(150)
        print(e)
    
