'''

zebot v0.2c [Discord BOT by zeborg]

GitHub/zeborg  |  Discord: zeborg#4589

OAuth2 : https://discordapp.com/oauth2/authorize?client_id=565886681165594624&permissions=2080619729&scope=bot

'''

import discord
import os
from random import randint as die
from random import randint as clrs
from datetime import datetime


# THE TOKEN IS HOSTED AS AN ENVIRONMENT VARIABLE
token = os.environ.get('BOT_TOKEN')

client = discord.Client()

server_start_date = datetime.now().strftime("%x")
server_start_time = datetime.now().strftime("%X")

verinfo = 'zebot v0.2c' # ZEBOT CURRENT VERSION
b_t = 'zeb' # ZEBOT COMMAND TRIGGER


@client.event
async def on_ready():
    ''' CHANGE CLIENT PRESENCE AT BOT START UP, PRINT LIST OF SERVERS CONNECTED DURING START UP IN BOT CONSOLE '''

    await client.change_presence(activity=discord.Game(name = 'GitHub/zeborg | zeb help'))
    print('\nConnected to ' + str(len(client.guilds)) + f' servers after recent reboot at {datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC.')
    for i in range(len(client.guilds)): print(f'{i+1}. {client.guilds[i]} | ID: {client.guilds[i].id} | Owner: {client.guilds[i].owner} | Members: {len(client.guilds[i].members)}')
    print('')


@client.event
async def on_guild_join(guild):
    ''' LOGGING GUILD CONNECTION '''

    logging_server = discord.utils.get(client.guilds, name='zebot dev')
    channel_log_console = discord.utils.get(logging_server.text_channels, name = 'console-logs')

    await channel_log_console.send(f'**CONNECTED** : ` {guild.name} ` | **ID** : ` {guild.id} ` | **OWNER** : ` {guild.owner} ` | **MEMBERS** : ` {len(guild.members)} `')
    print(f'CONNECTED : {guild.name} | ID : {guild.id} | OWNER : {guild.owner}') # LOGGING TO BOT SYSTEM CONSOLE


@client.event
async def on_guild_remove(guild):
    ''' LOGGING GUILD DISCONNECTION '''

    logging_server = discord.utils.get(client.guilds, name='zebot dev')
    channel_log_console = discord.utils.get(logging_server.text_channels, name = 'console-logs')

    await channel_log_console.send(f'**DISCONNECTED** : ` {guild.name} ` | **ID** : ` {guild.id} ` | **OWNER** : ` {guild.owner} | **MEMBERS** : {len(guild.members)} `')
    print(f'DISCONNECTED : {guild.name} | ID : {guild.id} | OWNER : {guild.owner} | MEMBERS : {len(guild.members)}') # LOGGING TO BOT SYSTEM CONSOLE


@client.event
async def on_message(message):
    ''' GUILD TEXT MESSAGE RESPONSES '''

    # DECLARING LOGGING SERVER AND CHANNELS
    logging_server = discord.utils.get(client.guilds, name='zebot dev')
    channel_log_server = discord.utils.get(logging_server.text_channels, name='server-logs')
    channel_log_server_bots = discord.utils.get(logging_server.text_channels, name='server-bots-logs')
    channel_log_zebdm = discord.utils.get(logging_server.text_channels, name='zebot-dm-logs')

    def random_colors():
        ''' RANDOM STOCK COLOUR GENERATOR '''
        pick_clr = {
            1: discord.Colour.teal(),
            2: discord.Colour.dark_teal(),
            3: discord.Colour.green(),
            4: discord.Colour.dark_green(),
            5: discord.Colour.blue(),
            6: discord.Colour.dark_blue(),
            7: discord.Colour.purple(),
            8: discord.Colour.dark_purple(),
            9: discord.Colour.magenta(),
            10: discord.Colour.dark_magenta(),
            11: discord.Colour.gold(),
            12: discord.Colour.dark_gold(),
            13: discord.Colour.orange(),
            14: discord.Colour.dark_orange(),
            15: discord.Colour.red(),
            16: discord.Colour.dark_red(),
            17: discord.Colour.lighter_grey(),
            18: discord.Colour.light_grey(),
            19: discord.Colour.dark_grey(),
            20: discord.Colour.darker_grey(),
            21: discord.Colour.blurple(),
            22: discord.Colour.greyple()
        }
        return pick_clr[clrs(1,22)]


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

    # COMMANDS LIST
    if message.content.lower() == f'{b_t} help': await message.channel.send(f'**AVAILABLE COMMANDS** `last updated: {server_start_date} {server_start_time} UTC`\n\n` {b_t} help ` : lists all the commands available since last update\n` {b_t} greet <@user1> <@user2> ... ` : greet people by mentioning them\n` {b_t} rtd ` : rolls a die\n` {b_t} guilds ` :  lists servers currently running {client.user.mention}\n` {b_t} slap <@user1> <@user2> ... ` : hurt others\' emotions\n` {b_t} server roles ` : info about every role in the server\n` {b_t} avatar <@user> ` : displays the profile picture of mentioned user\n` {b_t} userinfo <@user> ` : view someone\'s/your userinfo\n\n:thought_balloon: If you want to share some ideas regarding this bot, just DM me @ my Discord `zeborg#4589` :thought_balloon:')

    # DISPLAY CURRENTLY CONNECTED GUILDS
    if message.content.lower() == f'{b_t} guilds':
        conn_guilds_list=""
        for i in range(len(client.guilds)): conn_guilds_list=conn_guilds_list+(f'{i+1}. {client.guilds[i]} | Owner: {client.guilds[i].owner} | Members: {len(client.guilds[i].members)}\n')
        await message.channel.send(f'Currently connected to **{len(client.guilds)}** servers at `{datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC`\n\n```javascript\n{conn_guilds_list}```')

    # VARIABLE TO STORE MESSAGE CONTENT FOR LOGGING TO ZEBOT DISCORD DEV SERVER
    display_message_content = f'```{message.content}```' if len(message.content) > 0 else '`No content`'

    # LOGGING TEXTS FROM CONNECTED GUILDS
    if message.type == discord.MessageType.default:
        if message.guild != None: # LOGGING TEXTS RECEIVED IN GUILD CHANNELS
            if not message.author.bot: await channel_log_server.send((f'**{message.author}** logged text (*{datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC*) in **{message.author.guild}** `#{message.channel}`:\n\nAttachment: `{get_attached_file_url(message)}`\n\nContent: {display_message_content}'))
            elif message.author.bot and message.author != client.user: await channel_log_server_bots.send((f'**{message.author}** logged text (*{datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC*) in **{message.author.guild}** `#{message.channel}`:\n\nAttachment: `{get_attached_file_url(message)}`\n\nContent: {display_message_content}'))
        elif message.guild == None: # LOGGING TEXTS RECEIVED IN ZEBOT DM
            if not message.author.bot: await channel_log_zebdm.send((f'**{message.author}** logged text (*{datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC*) in `{message.channel}`:\n\nAttachment: `{get_attached_file_url(message)}`\n\nContent: {display_message_content}'))
            elif message.author.bot and message.author != client.user: await channel_log_zebdm.send((f'**{message.author}** *__[BOT]__* logged text (*{datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC*) in `{message.channel}``:\n\nAttachment: `{get_attached_file_url(message)}`\n\nContent: {display_message_content}'))

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

    # SHOW AVATAR
    if message.content.startswith(f'{b_t} avatar'):
        passed = False
        if len(message.mentions) == 1:
            passed = True
            requested_uinfo = message.mentions[0]
        elif message.content.lower() == f'{b_t} avatar':
            passed = True
            requested_uinfo = message.author

        if passed:
            ava_embed = discord.Embed(title = f'{requested_uinfo.name}\'s Avatar', url = f'{requested_uinfo.avatar_url}', colour = random_colors())
            ava_embed.set_image(url = f'{requested_uinfo.avatar_url}')
            ava_embed.set_footer(text = f'{verinfo}', icon_url = f'{client.user.avatar_url}')
            await message.channel.send(embed = ava_embed)
        else: await message.channel.send('To show someone\'s avatar by mentioning them, type `zeb avatar <@User>`\nTo show your own avatar, type `zeb avatar`')

    # VIEW USER INFO
    if message.guild != None:
        passed = False
        if message.content.startswith(f'{b_t} userinfo'):
            if len(message.mentions) == 1:
                requested_uinfo = message.mentions[0]
                passed = True
            elif message.content.lower() == f'{b_t} userinfo':
                requested_uinfo = message.author
                passed = True

            if passed:
                user_embed = discord.Embed(title = f'{requested_uinfo.name}\'s User Information', colour = message.author.color)
                user_embed.set_thumbnail(url = f'{requested_uinfo.avatar_url}')
                user_embed.add_field(name = 'Username', value = f'{requested_uinfo.name}')
                user_embed.add_field(name = 'Discriminator', value = f'{requested_uinfo.discriminator}')
                user_embed.add_field(name = 'User ID', value = f'{requested_uinfo.id}')
                user_embed.add_field(name = 'Current Status', value = f'{str(requested_uinfo.status).upper()}')
                user_embed.add_field(name = 'Server Nickname', value = f'{requested_uinfo.nick}')
                user_embed.add_field(name = 'Highest Role', value = 'OWNER' if requested_uinfo.id == message.guild.owner_id else f'{requested_uinfo.top_role}')
                user_embed.add_field(name = 'Joined Discord', value = f'{requested_uinfo.created_at}')
                user_embed.add_field(name = 'Joined Server', value = f'{requested_uinfo.joined_at}')
                user_embed.set_footer(text = f'{verinfo}', icon_url = f'{client.user.avatar_url}')
                await message.channel.send(embed = user_embed)
            else: await message.channel.send(f'To view someone\'s userinfo by mentioning them, type `{b_t} userinfo <@user>`\nTo view your own userinfo, type `{b_t} userinfo`')


client.run(token)
