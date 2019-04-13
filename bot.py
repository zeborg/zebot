'''

zebot v0.1 [Discord BOT by zeborg]

GitHub/zeborg

OAuth2 : https://discordapp.com/oauth2/authorize?client_id=565886681165594624&permissions=2080619729&scope=bot

'''

import discord
import os
from random import randint as dice
from datetime import datetime


# THE TOKEN IS HOSTED AS AN ENVIRONMENT VARIABLE
token = os.environ.get('BOT_TOKEN')

client = discord.Client()

server_start_date = datetime.now().strftime("%x")
server_start_time = datetime.now().strftime("%X")


@client.event
async def on_ready():
    print('heroku')

@client.event
async def on_message():
    if message.author != client.user:
        await message.channel.send('active on heroku')
    
client.run(token)
