'''

zebot v0.1c [Discord BOT by zeborg]

GitHub/zeborg  |  Discord: zeborg#4589

OAuth2 : https://discordapp.com/oauth2/authorize?client_id=565886681165594624&permissions=2080619729&scope=bot

'''

import discord
import os
from random import randint as die
from datetime import datetime


# THE TOKEN IS HOSTED AS AN ENVIRONMENT VARIABLE
token = os.environ.get('BOT_TOKEN')

client = discord.Client()

server_start_date = datetime.now().strftime("%x")
server_start_time = datetime.now().strftime("%X")

b_t = 'zeb' # ZEBOT COMMAND TRIGGER


@client.event
async def on_guild_join(guild):
    ''' LOGGING GUILD CONNECTION '''

    logging_server = discord.utils.get(client.guilds, name='zebot dev')
    channel_log_console = discord.utils.get(logging_server.text_channels, name='console-logs')

    await channel_log_console.send(f'**CONNECTED** : ` {guild.name} ` | **ID** : ` {guild.id} ` | **OWNER** : ` {guild.owner} ` | **MEMBERS** : ` {len(guild.members)} `')
    print(f'CONNECTED : {guild.name} | ID : {guild.id} | OWNER : {guild.owner}') # LOGGING TO BOT SYSTEM CONSOLE

@client.event
async def on_guild_remove(guild):
    ''' LOGGING GUILD DISCONNECTION '''

    logging_server = discord.utils.get(client.guilds, name='zebot dev')
    channel_log_console = discord.utils.get(logging_server.text_channels, name='console-logs')

    await channel_log_console.send(f'**DISCONNECTED** : ` {guild.name} ` | **ID** : ` {guild.id} ` | **OWNER** : ` {guild.owner} | **MEMBERS** : {len(guild.members)} `')
    print(f'DISCONNECTED : {guild.name} | ID : {guild.id} | OWNER : {guild.owner} | MEMBERS : {len(guild.members)}') # LOGGING TO BOT SYSTEM CONSOLE


@client.event
async def on_ready():
    ''' CHANGE CLIENT PRESENCE AT BOT START UP, PRINT LIST OF SERVERS CONNECTED DURING START UP IN BOT CONSOLE '''

    await client.change_presence(activity=discord.Game(name="GitHub/zeborg | zeb help"))
    print('\nConnected to ' + str(len(client.guilds)) + f' servers after recent reboot at {datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC.')
    for i in range(len(client.guilds)): print(f'{i+1}. {client.guilds[i]} | ID: {client.guilds[i].id} | Owner: {client.guilds[i].owner} | Members: {len(client.guilds[i].members)}')
    print('')
          

@client.event
async def on_guild_join(guild):
    ''' LOGGING GUILD CONNECTION '''

    logging_server = discord.utils.get(client.guilds, name='zebot dev')
    channel_log_console = discord.utils.get(logging_server.text_channels, name='console-logs')

    await channel_log_console.send(f'**CONNECTED** : ` {guild.name} ` | **ID** : ` {guild.id} ` | **OWNER** : ` {guild.owner} ` | **MEMBERS** : ` {len(guild.members)} `')
    print(f'CONNECTED : {guild.name} | ID : {guild.id} | OWNER : {guild.owner}')  # LOGGING TO BOT SYSTEM CONSOLE


@client.event
async def on_guild_remove(guild):
    ''' LOGGING GUILD DISCONNECTION '''

    logging_server = discord.utils.get(client.guilds, name='zebot dev')
    channel_log_console = discord.utils.get(logging_server.text_channels, name='console-logs')

    await channel_log_console.send(f'**DISCONNECTED** : ` {guild.name} ` | **ID** : ` {guild.id} ` | **OWNER** : ` {guild.owner} | **MEMBERS** : {len(guild.members)} `')
    print(f'DISCONNECTED : {guild.name} | ID : {guild.id} | OWNER : {guild.owner} | MEMBERS : {len(guild.members)}')  # LOGGING TO BOT SYSTEM CONSOLE

@client.event
async def on_message(message):
    ''' GUILD TEXT MESSAGE RESPONSES '''

    try:
        def get_attached_file_url(given_message):
            ''' RETURNS URL OF FILE ATTACHED IN A MESSAGE, RETURNS STRING 'None' IF THERE'S NO ATTACHMENT '''

            if len(given_message.attachments) == 1: return given_message.attachments[0].url
            else: return 'None'

        def get_server_roles_list():
            ''' RETURNS AN ARRAY OF ALL THE ROLES PRESENT IN THE GUILD EXCEPT THE '@everyone' ROLE
                INDICES :  0 => NAME (str)  //  1 => ROLE COLOUR (object)  //  2 => ROLE ID (int) //  3 => NO. OF MEMBERS IN THAT ROLE (int)
            '''
            
            server_roles_list = []
            for i in message.guild.roles:
                if i.name != '@everyone':
                    temp = []
                    temp.append(i.name)
                    temp.append(discord.Colour.to_rgb(i.color))
                    temp.append(i.id)
                    temp.append(len(i.members))
                    server_roles_list.append(temp)
            return server_roles_list

        def multi_mentions():
            ''' RETURNS A MENTION STRING FROM A MESSAGE, EVERY OTHER MENTION SEPARATED BY A COMMA '''

            mult_mentions = ""
            for k in range(len(message.mentions)): multi_mentions = multi_mentions + message.mentions[k].mention + ', ' if k < len(message.mentions) - 1 else multi_mentions + message.mentions[k].mention
            return multi_mentions

    # DISPLAY LIST OF USABLE COMMANDS
        if message.content.lower() == f'{b_t} help': await message.channel.send(f'**AVAILABLE COMMANDS** `last updated: {server_start_date} {server_start_time} UTC`\n\n` zeb help ` : lists all the commands available since last update\n` zeb greet <@user1> <@user2> ... ` : greet people by mentioning them\n` zeb rtd ` : rolls a die\n` zeb guilds ` :  lists servers currently running {client.user.mention}\n`zeb slap <@user1> <@user2> ...` : hurt others\' emotions\n`zeb server roles` : info about every role in the server\n\n:thought_balloon: If you want to share some ideas regarding this bot, just DM me @ my discord `zeborg#4589` :thought_balloon:')

    # DISPLAY CURRENTLY CONNECTED GUILDS
        if message.content.lower() == f'{b_t} guilds':
            conn_guilds_list=""
            for i in range(len(client.guilds)): conn_guilds_list=conn_guilds_list+(f'{i+1}. {client.guilds[i]} | Owner: {client.guilds[i].owner} | Members: {len(client.guilds[i].members)}\n')
            await message.channel.send(f'Currently connected to **{len(client.guilds)}** servers at `{datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC`\n\n```javascript\n{conn_guilds_list}```')

    # VARIABLE TO STORE MESSAGE CONTENT FOR LOGGING TO ZEBOT DISCORD DEV SERVER
        display_message_content = f'```{message.content}```' if len(message.content) > 0 else '`No content`'

    # LOGGING TEXTS FROM CONNECTED GUILDS
        logging_server = discord.utils.get(client.guilds, name = 'zebot dev')
        channel_log_server = discord.utils.get(logging_server.text_channels, name = 'server-logs')
        channel_log_server_bots = discord.utils.get(logging_server.text_channels, name = 'server-bots-logs')

        if message.type == discord.MessageType.default:
            if not message.author.bot: await channel_log_server.send((f'**{message.author}** logged text (*{datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC*) in **{message.author.guild}** `#{message.channel}`:\n\nAttachment: `{get_attached_file_url(message)}`\n\nContent: {display_message_content}'))
            elif message.author.bot and message.author != client.user: await channel_log_server_bots.send((f'**{message.author}** logged text (*{datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC*) in **{message.author.guild}** `#{message.channel}`:\n\nAttachment: `{get_attached_file_url(message)}`\n\nContent: {display_message_content}'))

    # GREET A USER
        if message.content.startswith(f'{b_t} greet') and '@everyone' in message.content: await message.channel.send(f':bouquet: Hey **everyone**! Greetings from {message.author.mention} :bouquet:')
        elif message.content.startswith(f'{b_t} greet') and ((len(message.mentions) > 1 and '@everyone' not in message.content)): await message.channel.send(f':bouquet: Hey {multi_mentions()}! Greetings from {message.author.mention}! :bouquet:')
        elif message.content.startswith(f'{b_t} greet') and (len(message.mentions) == 0 or (len(message.mentions) == 1 and message.mentions[0].mention == message.author.mention)): await message.channel.send(':bouquet: Hello there, ' + message.author.mention + '! Greetings from **' + client.user.display_name + '**! :bouquet:')
        elif message.content.startswith(f'{b_t} greet') and len(message.mentions) == 1: await message.channel.send(':bouquet: Hello there, ' + str(message.mentions[0].mention) + '! Greetings from ' + message.author.mention + '! :bouquet:')
        elif message.content.startswith(f'{b_t} greet') and ((len(message.mentions) > 1 or '@everyone' in message.content)): await message.channel.send('Sorry, you cannot greet everyone at once! :bouquet:')

    # ROLL THE DIE
        if message.content.lower() == f'{b_t} rtd':
            await message.channel.send(f':game_die: **{message.author.display_name}** just rolled **{die(1, 6)}** :game_die:')

    # SLAP
        if message.content.startswith(f'{b_t} slap'):
            if '@everyone' in message.content: await message.channel.send(f":clap: {message.author.mention} just slapped **EVERYONE**! :clap: WE'VE GOT A BADASS OVER HERE! :eyes:")
            elif len(message.mentions) > 1 and '@everyone' not in message.content: await message.channel.send(f':clap: {message.author.mention} just slapped {multi_mentions()}! :clap: GET REKT KIDS! :nerd:')
            elif len(message.mentions) == 0 or (len(message.mentions) == 1 and message.mentions[0].mention == message.author.mention): await message.channel.send(f':clap: {message.author.mention} just slapped themself! :clap: Make sure you mention someone ||*other than you*|| to avoid slapping yourself. :robot:')
            elif len(message.mentions) == 1: await message.channel.send(f':clap: {message.author.mention} just slapped {message.mentions[0].mention}! :clap: GET REKT KID! :nerd: ')

    # GUILD ROLES INFO
        if message.content.lower() == f'{b_t} server roles':
            role_str = ''
            for role in get_server_roles_list():
                role_str = f'Name: `{role[0]}` // Colour: `{role[1]}` // Members: `{role[3]}`' if get_server_roles_list().index(role) == 0 else role_str + f'\nName: `{role[0]}` // Colour: `{role[1]}` // Members: `{role[3]}`'
            await message.channel.send(f'**__SERVER ROLES__**:\n\n{role_str}')

    # USER AVATAR
        if message.content.lower() == f'{b_t} avatar':
            pass

    # TEXT CHANNELS IN THE GUILD
        if message.content.lower() == f'{b_t} textchannels':
            pass #await channel_log_console ==

    except:
        logging_server = discord.utils.get(client.guilds, name='zebot dev')
        channel_log_zebdm = discord.utils.get(logging_server.text_channels, name='zebot-dm-logs')

        if not message.author.bot: await channel_log_zebdm.send((f'**{message.author}** logged text (*{datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC*) in **{message.channel}**:\n\nAttachment: `{get_attached_file_url(message)}`\n\nContent: {display_message_content}'))
        elif message.author.bot and message.author != client.user: await channel_log_zebdm.send((f'**{message.author}** *__[BOT]__* logged text (*{datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC*) in **{message.channel}**:\n\nAttachment: `{get_attached_file_url(message)}`\n\nContent: {display_message_content}'))

client.run(token)
