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
    await client.change_presence(activity=discord.Game(name="GitHub/zeborg | zebot help"))
    print('\nConnected to ' + str(len(client.guilds)) + f' servers after recent reboot at {datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC.')
    for i in range(len(client.guilds)): print(f'{i+1}. {client.guilds[i]} | ID: {client.guilds[i].id} | Owner: {client.guilds[i].owner} | Members: {len(client.guilds[i].members)}')
    print('')


@client.event
# LOGGING GUILD CONNECTION
async def on_guild_join(guild):
    logging_server = discord.utils.get(client.guilds, name='zebot dev')
    channel_log_console = discord.utils.get(logging_server.text_channels, name='console-logs')

    await channel_log_console.send(f'**CONNECTED** : ` {guild.name} ` | **ID** : ` {guild.id} ` | **OWNER** : ` {guild.owner} | **MEMBERS** : {len(guild.members)} `')
    print(f'CONNECTED : {guild.name} | ID : {guild.id} | OWNER : {guild.owner}')


@client.event
# LOGGING GUILD DISCONNECTION
async def on_guild_remove(guild):
    logging_server = discord.utils.get(client.guilds, name='zebot dev')
    channel_log_console = discord.utils.get(logging_server.text_channels, name='console-logs')

    await channel_log_console.send(f'**DISCONNECTED** : ` {guild.name} ` | **ID** : ` {guild.id} ` | **OWNER** : ` {guild.owner} | **MEMBERS** : {len(guild.members)} `')
    print(f'DISCONNECTED : {guild.name} | ID : {guild.id} | OWNER : {guild.owner} | MEMBERS : {len(guild.members)}')


@client.event
async def on_message(message):
# DISPLAY LIST OF USABLE COMMANDS
    if message.content.lower() == 'zebot help':
        await message.channel.send(f'**AVAILABLE COMMANDS** `last updated: {server_start_date} {server_start_time} UTC`\n\n` zebot help ` : lists all the commands available since last update\n` zebot greet <@User1> <@User2> ... ` : greet people by mentioning them; greets you if no one is mentioned\n` zebot rtd ` : rolls a die\n` zebot guilds ` :  lists servers currently running {client.user.mention}')

# DISPLAY CURRENTLY CONNECTED GUILDS
    if message.content.lower() == 'zebot guilds':
        conn_guilds_list=""
        for i in range(len(client.guilds)): conn_guilds_list=conn_guilds_list+(f'{i+1}. {client.guilds[i]} | Owner: {client.guilds[i].owner} | Members: {len(client.guilds[i].members)}\n')
        await message.channel.send(f'Currently connected to **{len(client.guilds)}** servers at `{datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC`\n\n```javascript\n{conn_guilds_list}```')

# LOGGING TEXTS FROM CONNECTED GUILDS
    logging_server = discord.utils.get(client.guilds, name='zebot dev')
    channel_log_server = discord.utils.get(logging_server.text_channels, name='server-logs')
    if message.author != client.user:
        await channel_log_server.send((f'**{message.author}** logged text (*{datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC*) in **{message.author.guild}** `#{message.channel}`:\n```{message.content}```'))

# GREET A USER
    if message.content.startswith('zebot greet') and '@everyone' in message.content: await message.channel.send(f':bouquet: Hey **everyone**! Greetings from {message.author.mention} :bouquet:')
    elif message.content.startswith('zebot greet') and ((len(message.mentions) > 1 and '@everyone' not in message.content)):
        multi_greet_mentions = ""
        for k in range(len(message.mentions)): multi_greet_mentions = multi_greet_mentions + message.mentions[k].mention + ', ' if k < len(message.mentions)-1 else multi_greet_mentions + message.mentions[k].mention
        await message.channel.send(f':bouquet: Hey {multi_greet_mentions}! Greetings from {message.author.mention}! :bouquet:')
    elif message.content.startswith('zebot greet') and (len(message.mentions) == 0 or (len(message.mentions) == 1 and message.mentions[0].mention == message.author.mention)): await message.channel.send(':bouquet: Hello there, ' + message.author.mention + '! Greetings from **' + client.user.display_name + '**! :bouquet:')
    elif message.content.startswith('zebot greet') and len(message.mentions) == 1: await message.channel.send(':bouquet: Hello there, ' + str(message.mentions[0].mention) + '! Greetings from ' + message.author.mention + '! :bouquet:')
    elif message.content.startswith('zebot greet') and ((len(message.mentions) > 1 or '@everyone' in message.content)): await message.channel.send('Sorry, you cannot greet everyone at once! :bouquet:')

# ROLL THE DIE
    if message.content.lower() == 'zebot rtd':
        await message.channel.send(f':game_die: **{message.author.display_name}** just rolled **{dice(1, 6)}** :game_die:')

# SLAP
    if message.content.startswith('zebot slap'):
        if '@everyone' in message.content: await message.channel.send(f":clap: {message.author.mention} just slapped **EVERYONE**! :clap: WE'VE GOT A BADASS OVER HERE! :eyes:")
        elif len(message.mentions) > 1 and '@everyone' not in message.content:
            multi_slap_mentions = ""
            for l in range(len(message.mentions)): multi_slap_mentions = multi_slap_mentions + message.mentions[l].mention + ', ' if l < len(message.mentions) - 1 else multi_slap_mentions + message.mentions[l].mention
            await message.channel.send(f':clap: {message.author.mention} just slapped {multi_slap_mentions}! :clap: GET REKT KIDS! :nerd:')
        elif len(message.mentions) == 1: await message.channel.send(f':clap: {message.author.mention} just slapped {message.mentions[0].mention}! :clap: GET REKT KID! :nerd: ')
        elif len(message.mentions) == 0: await message.channel.send(f':clap: {message.author.mention} just slapped themself! :clap: Make sure you mention someone to avoid slapping yourself. :robot:')

client.run(token)
