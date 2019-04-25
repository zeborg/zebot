"""

zebot v0.4 [Discord BOT by zeborg]

GitHub/zeborg  |  Discord: zeborg#4589

OAuth2 : https://discordapp.com/oauth2/authorize?client_id=565886681165594624&permissions=2080619729&scope=bot

"""

import discord
import psycopg2
import feedparser
import asyncio
from os import environ as envar
from random import randint as die
from random import randint as clrs
from random import randint as roul
from datetime import datetime


# BOT TOKEN
token = envar.get('BOT_TOKEN')

# DATABASE SETUP
dbhost, dbuser, dbpw, dbdb = envar.get('DB_HOST'), envar.get('DB_USER'), envar.get('DB_PW'), envar.get('DB_DB')

# CLIENT ACTIVATION
client = discord.Client()

server_start_date = datetime.now().strftime("%x")
server_start_time = datetime.now().strftime("%X")

verinfo = 'zebot v0.4'  # ZEBOT CURRENT VERSION
b_t = 'zeb'  # ZEBOT COMMAND TRIGGER


@client.event
async def on_ready():
    """ CHANGE CLIENT PRESENCE AT BOT START UP, PRINT LIST OF SERVERS CONNECTED DURING START UP IN BOT CONSOLE """

    await client.change_presence(activity=discord.Game(name=f'GitHub/zeborg | {b_t} help'))
    print('\nConnected to ' + str(len(client.guilds)) + f' servers after recent reboot at {datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC.')
    for i in range(len(client.guilds)):
        print(f'{i+1}. {client.guilds[i]} | ID: {client.guilds[i].id} | Owner: {client.guilds[i].owner} | Members: {len(client.guilds[i].members)}')
    print('')


@client.event
async def on_guild_join(guild):
    """ LOGGING GUILD CONNECTION """

    logging_server = discord.utils.get(client.guilds, name='zebot dev')
    channel_log_console = discord.utils.get(logging_server.text_channels, name='console-logs')

    await channel_log_console.send(f'**CONNECTED** : ` {guild.name} ` | **ID** : ` {guild.id} ` | **OWNER** : ` {guild.owner} ` | **MEMBERS** : ` {len(guild.members)} `')
    print(f'CONNECTED : {guild.name} | ID : {guild.id} | OWNER : {guild.owner}')  # LOGGING TO BOT SYSTEM CONSOLE


@client.event
async def on_guild_remove(guild):
    """ LOGGING GUILD DISCONNECTION """

    logging_server = discord.utils.get(client.guilds, name='zebot dev')
    channel_log_console = discord.utils.get(logging_server.text_channels, name='console-logs')

    await channel_log_console.send(f'**DISCONNECTED** : ` {guild.name} ` | **ID** : ` {guild.id} ` | **OWNER** : ` {guild.owner} | **MEMBERS** : {len(guild.members)} `')
    print(f'DISCONNECTED : {guild.name} | ID : {guild.id} | OWNER : {guild.owner} | MEMBERS : {len(guild.members)}')  # LOGGING TO BOT SYSTEM CONSOLE


@client.event
async def on_message(message):
    """ GUILD TEXT MESSAGE RESPONSES """

    # DECLARING LOGGING SERVER AND CHANNELS
    logging_server = discord.utils.get(client.guilds, name='zebot dev')
    channel_log_server = discord.utils.get(logging_server.text_channels, name='server-logs')
    channel_log_server_bots = discord.utils.get(logging_server.text_channels, name='server-bots-logs')
    channel_log_zebdm = discord.utils.get(logging_server.text_channels, name='zebot-dm-logs')

    def random_colors():
        """ RANDOM STOCK COLOUR GENERATOR """

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
        return pick_clr[clrs(1, 22)]

    def roul_num_img_gen(num):
        """ IMAGE GENERATOR FOR ROULETTE NUMBER ROLLS """

        img_dict = {
            -14: 'http://www.mediafire.com/convkey/c12e/0cw6hkp2pod0yy6zg.jpg',
            -13: 'http://www.mediafire.com/convkey/10de/4o81cmczjws68tzzg.jpg',
            -12: 'http://www.mediafire.com/convkey/40cf/7f47s4x8t30djb0zg.jpg',
            -11: 'http://www.mediafire.com/convkey/7c18/ue9v1bde0aywfq3zg.jpg',
            -10: 'http://www.mediafire.com/convkey/74a3/4ocfvwaefuuvyyizg.jpg',
            -9: 'http://www.mediafire.com/convkey/0bcb/499zbt3babz3kwezg.jpg',
            -8: 'http://www.mediafire.com/convkey/5a7a/8cpenbkojc62xdlzg.jpg',
            -7: 'http://www.mediafire.com/convkey/190c/e2sn3y8xutznoaxzg.jpg',
            -6: 'http://www.mediafire.com/convkey/7491/p57d3jq1d68g2j0zg.jpg',
            -5: 'http://www.mediafire.com/convkey/351d/85blchu5ntq46jwzg.jpg',
            -4: 'http://www.mediafire.com/convkey/56da/v4lonhz4njl69izzg.jpg',
            -3: 'http://www.mediafire.com/convkey/8d24/xabmuxpu9lt8a50zg.jpg',
            -2: 'http://www.mediafire.com/convkey/985b/zshtmaopscm3ndazg.jpg',
            -1: 'http://www.mediafire.com/convkey/830a/hudhe5ofiqbv1snzg.jpg',
            0: 'http://www.mediafire.com/convkey/4bc9/o3kv4h1umdozqfczg.jpg',
            1: 'http://www.mediafire.com/convkey/3db6/r13bj0b0v47mr51zg.jpg',
            2: 'http://www.mediafire.com/convkey/e4fa/d4hqi0hryeyqswlzg.jpg',
            3: 'http://www.mediafire.com/convkey/b12c/81w66govrhf1o1yzg.jpg',
            4: 'http://www.mediafire.com/convkey/72a0/o344i6xvfsctn0tzg.jpg',
            5: 'http://www.mediafire.com/convkey/51a5/abn485v7f5bb0m9zg.jpg',
            6: 'http://www.mediafire.com/convkey/6475/pgv36tfjsk9ukpxzg.jpg',
            7: 'http://www.mediafire.com/convkey/6cbd/e93zx4z9fe76hehzg.jpg',
            8: 'http://www.mediafire.com/convkey/bbb0/1azy4oclsl2ydnmzg.jpg',
            9: 'http://www.mediafire.com/convkey/a863/39h7l2cr3m2tzwvzg.jpg',
            10: 'http://www.mediafire.com/convkey/f23d/s6ntjmw2d1vjjb4zg.jpg',
            11: 'http://www.mediafire.com/convkey/0b8a/1ihskwj9w91yjuvzg.jpg',
            12: 'http://www.mediafire.com/convkey/dcb4/k9jzmonsdx4f3hjzg.jpg',
            13: 'http://www.mediafire.com/convkey/92b3/30u2xxuiaj6r1xkzg.jpg',
            14: 'http://www.mediafire.com/convkey/d788/ivhz3biicee63dizg.jpg'
        }
        return img_dict[num]

    def get_attached_file_url(given_message):
        """ RETURNS URL OF FILE ATTACHED IN A MESSAGE, RETURNS STRING 'None' IF THERE'S NO ATTACHMENT """

        if len(given_message.attachments) == 1:
            return given_message.attachments[0].url
        else:
            return 'None'

    def get_server_roles_list():
        """ RETURNS AN ARRAY OF ALL THE ROLES PRESENT IN THE GUILD EXCEPT THE '@everyone' ROLE
            INDICES :  0 => NAME (str)  //  1 => ROLE COLOUR (object)  //  2 => ROLE ID (int) //  3 => NO. OF MEMBERS IN THAT ROLE (int) """

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
        """ RETURNS A MENTION STRING FROM A MESSAGE, EVERY OTHER MENTION SEPARATED BY A COMMA """

        multi_mentions = ""
        for k in range(len(message.mentions)):
            multi_mentions = multi_mentions + message.mentions[k].mention + ', ' if k < len(message.mentions) - 1 else multi_mentions + message.mentions[k].mention
        return multi_mentions

    # COMMANDS LIST
    if message.content.lower() == f'{b_t} help':
        await message.channel.send(f'**AVAILABLE COMMANDS** `last updated: {server_start_date} {server_start_time} UTC`\n\n` {b_t} help ` : lists all the commands available since last update\n` {b_t} greet <@user1> <@user2> ... ` : greet people by mentioning them\n` {b_t} rtd ` : rolls a die\n` {b_t} guilds ` :  lists servers currently running {client.user.mention}\n` {b_t} slap <@user1> <@user2> ... ` : hurt others\' emotions\n` {b_t} server roles ` : info about every role in the server\n` {b_t} avatar <@user> ` : displays the profile picture of mentioned user\n` {b_t} userinfo <@user> ` : view someone\'s/your userinfo\n` {b_t} aninews ` : view 5 recent anime news stories\n\n:thought_balloon: If you want to share some ideas regarding this bot, just DM me @ my Discord `zeborg#4589` :thought_balloon:')

    # DISPLAY CURRENTLY CONNECTED GUILDS
    if message.content.lower() == f'{b_t} guilds':
        conn_guilds_list = ""
        for i in range(len(client.guilds)):
            conn_guilds_list = conn_guilds_list + f'{i+1}. {client.guilds[i]} | Owner: {client.guilds[i].owner} | Members: {len(client.guilds[i].members)}\n'
        await message.channel.send(f'Currently connected to **{len(client.guilds)}** servers at `{datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC`\n\n```javascript\n{conn_guilds_list}```')

    # VARIABLE TO STORE MESSAGE CONTENT FOR LOGGING TO ZEBOT DISCORD DEV SERVER
    display_message_content = f'```{message.content}```' if len(message.content) > 0 else '`No content`'

    # LOGGING TEXTS FROM CONNECTED GUILDS
    if message.type == discord.MessageType.default:
        if message.guild is not None:  # LOGGING TEXTS RECEIVED IN GUILD CHANNELS
            if not message.author.bot:
                await channel_log_server.send(f'**{message.author}** logged text (*{datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC*) in **{message.author.guild}** `#{message.channel}`:\n\nAttachment: `{get_attached_file_url(message)}`\n\nContent: {display_message_content}')
            elif message.author.bot and message.author != client.user:
                await channel_log_server_bots.send(f'**{message.author}** logged text (*{datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC*) in **{message.author.guild}** `#{message.channel}`:\n\nAttachment: `{get_attached_file_url(message)}`\n\nContent: {display_message_content}')
        elif message.guild is None:  # LOGGING TEXTS RECEIVED IN ZEBOT DM
            if not message.author.bot:
                await channel_log_zebdm.send(f'**{message.author}** logged text (*{datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC*) in `{message.channel}`:\n\nAttachment: `{get_attached_file_url(message)}`\n\nContent: {display_message_content}')
            elif message.author.bot and message.author != client.user:
                await channel_log_zebdm.send(f'**{message.author}** *__[BOT]__* logged text (*{datetime.now().strftime("%x")} {datetime.now().strftime("%X")} UTC*) in `{message.channel}``:\n\nAttachment: `{get_attached_file_url(message)}`\n\nContent: {display_message_content}')

    # GREET A USER
    if message.content.startswith(f'{b_t} greet') and '@everyone' in message.content:
        await message.channel.send(f':bouquet: Hey **everyone**! Greetings from {message.author.mention} :bouquet:')
    elif message.content.startswith(f'{b_t} greet') and (len(message.mentions) > 1 and '@everyone' not in message.content):
        await message.channel.send(f':bouquet: Hey {multi_mentions()}! Greetings from {message.author.mention}! :bouquet:')
    elif message.content.startswith(f'{b_t} greet') and (len(message.mentions) == 0 or (len(message.mentions) == 1 and message.mentions[0].mention == message.author.mention)):
        await message.channel.send(':bouquet: Hello there, ' + message.author.mention + '! Greetings from **' + client.user.display_name + '**! :bouquet:')
    elif message.content.startswith(f'{b_t} greet') and len(message.mentions) == 1:
        await message.channel.send(':bouquet: Hello there, ' + str(message.mentions[0].mention) + '! Greetings from ' + message.author.mention + '! :bouquet:')
    elif message.content.startswith(f'{b_t} greet') and (len(message.mentions) > 1 or '@everyone' in message.content):
        await message.channel.send('Sorry, you cannot greet everyone at once! :bouquet:')

    # ROLL THE DIE
    if message.content.lower() == f'{b_t} rtd':
        await message.channel.send(f':game_die: **{message.author.display_name}** just rolled **{die(1, 6)}** :game_die:')

    # SLAP
    if message.content.startswith(f'{b_t} slap'):
        if '@everyone' in message.content:
            await message.channel.send(f":clap: {message.author.mention} just slapped **EVERYONE**! :clap: WE'VE GOT A BADASS OVER HERE! :eyes:")
        elif len(message.mentions) > 1 and '@everyone' not in message.content:
            await message.channel.send(f':clap: {message.author.mention} just slapped {multi_mentions()}! :clap: GET REKT KIDS! :nerd:')
        elif len(message.mentions) == 0 or (len(message.mentions) == 1 and message.mentions[0].mention == message.author.mention):
            await message.channel.send(f':clap: {message.author.mention} just slapped themself! :clap: Make sure you mention someone ||*other than you*|| to avoid slapping yourself. :robot:')
        elif len(message.mentions) == 1:
            await message.channel.send(f':clap: {message.author.mention} just slapped {message.mentions[0].mention}! :clap: GET REKT KID! :nerd: ')

    # GUILD ROLES INFO
    if message.content.lower() == f'{b_t} server roles':
        role_str = ''
        for role in get_server_roles_list():
            role_str = f'Name: `{role[0]}` // Colour: `{role[1]}` // Members: `{role[3]}`' if get_server_roles_list().index(role) == 0 else role_str + f'\nName: `{role[0]}` // Colour: `{role[1]}` // Members: `{role[3]}`'
        await message.channel.send(f'**__SERVER ROLES__**:\n\n{role_str}')

    # SHOW AVATAR
    if message.content.startswith(f'{b_t} avatar'):
        passed = False
        requested_uinfo = None
        if len(message.mentions) == 1:
            passed = True
            requested_uinfo = message.mentions[0]
        elif message.content.lower() == f'{b_t} avatar':
            passed = True
            requested_uinfo = message.author

        if passed:
            ava_embed = discord.Embed(title=f'{requested_uinfo.name}\'s Avatar', url=f'{requested_uinfo.avatar_url}', colour=requested_uinfo.color)
            ava_embed.set_image(url=f'{requested_uinfo.avatar_url}')
            ava_embed.set_footer(text=f'{verinfo}', icon_url=client.user.avatar_url)
            ava_embed.set_author(name=f'{message.author} requested:', icon_url=message.author.avatar_url)
            await message.channel.send(embed=ava_embed)
        else:
            await message.channel.send('To show someone\'s avatar by mentioning them, type `zeb avatar <@User>`\nTo show your own avatar, type `zeb avatar`')

    # VIEW USER INFO
    if message.guild is not None:
        passed = False
        requested_uinfo = None
        if message.content.startswith(f'{b_t} userinfo'):
            if len(message.mentions) == 1:
                requested_uinfo = message.mentions[0]
                passed = True
            elif message.content.lower() == f'{b_t} userinfo':
                requested_uinfo = message.author
                passed = True

            if message.author.typing:
                pass

            if passed:
                user_embed = discord.Embed(title=f'{requested_uinfo.name}\'s User Information', colour=requested_uinfo.color)
                user_embed.set_thumbnail(url=f'{requested_uinfo.avatar_url}')
                user_embed.add_field(name='Username', value=f'{requested_uinfo.name}')
                user_embed.add_field(name='Discriminator', value=f'{requested_uinfo.discriminator}')
                user_embed.add_field(name='User ID', value=f'{requested_uinfo.id}')
                user_embed.add_field(name='Current Status', value=f'{str(requested_uinfo.status).upper()}')
                user_embed.add_field(name='Server Nickname', value=f'{requested_uinfo.nick}')
                user_embed.add_field(name='Highest Role', value='OWNER' if requested_uinfo.id == message.guild.owner_id else f'{requested_uinfo.top_role}')
                user_embed.add_field(name='Joined Discord', value=f'{requested_uinfo.created_at}')
                user_embed.add_field(name='Joined Server', value=f'{requested_uinfo.joined_at}')
                user_embed.set_footer(text=f'{verinfo}', icon_url=client.user.avatar_url)
                user_embed.set_author(name=f'{message.author} requested:', icon_url=message.author.avatar_url)
                await message.channel.send(embed=user_embed)
            else:
                await message.channel.send(f'To view someone\'s userinfo by mentioning them, type `{b_t} userinfo <@user>`\nTo view your own userinfo, type `{b_t} userinfo`')

    # RECENT ANIME NEWS
    if message.content.lower() == 'zeb aninews':
        aninews = feedparser.parse('https://myanimelist.net/rss/news.xml')

        ani_embed = discord.Embed(title='Recent Anime News', colour=random_colors(), url='https://myanimelist.net/news')
        for i in range(5):
            ani_embed.add_field(name=f'{i+1}. {aninews.entries[i].title}', value=f'`{aninews.entries[i].published.strip("-0700")} UTC-07:00`\n{aninews.entries[i].description}..[read more]({aninews.entries[i].link})')
        ani_embed.set_footer(text=f'{verinfo}', icon_url=client.user.avatar_url)
        ani_embed.set_author(name=f'{message.author} requested:', icon_url=message.author.avatar_url)
        ani_embed.set_thumbnail(url=aninews.entries[0]['media_thumbnail'][0]['url'])
        await message.channel.send(embed=ani_embed)

    # ROULETTE BETA
    if message.content.startswith(f'{b_t} roulette'):
        db = psycopg2.connect(host=dbhost, user=dbuser, password=dbpw, database=dbdb)
        cur = db.cursor()

        cur.execute(f'select schema_name from information_schema.schemata')
        users_schema_list = cur.fetchall()

        cur.close()
        db.close()

        user_schema_tuple = (f'u_{message.author.id}',)
        user_guild_tuple = (message.guild.id,)

        if message.content.lower() == f'{b_t} roulette signup':
            db = psycopg2.connect(host=dbhost, user=dbuser, password=dbpw, database=dbdb)
            cur = db.cursor()

            if user_schema_tuple in users_schema_list:
                cur.execute(f'select guild from u_{message.author.id}.roulette;')
                user_roul_guilds_list = cur.fetchall()
                if user_guild_tuple not in user_roul_guilds_list:
                    cur.execute(f'insert into u_{message.author.id}.roulette(guild) values ({message.guild.id})')
                    db.commit()
                    await message.channel.send(f'Hey {message.author.mention}, I\'ve just signed you up for roulette in this server! Type `zeb roulette help` to get started.')
                elif user_guild_tuple in user_roul_guilds_list:
                    await message.channel.send(f'It seems like you\'re already in this server\'s roulette club, {message.author.mention}! Type `zeb roulette help` if you need some assistance.')

            elif user_schema_tuple not in users_schema_list:
                cur.execute(f'create schema u_{message.author.id}')
                cur.execute(f'create table u_{message.author.id}.roulette(guild bigint primary key, rolls integer default 0, points integer default 10)')
                cur.execute(f'insert into u_{message.author.id}.roulette(guild) values ({message.guild.id})')
                db.commit()
                await message.channel.send(f'Hey {message.author.mention}, I\'ve just signed you up for roulette in this server! Type `zeb roulette help` to get started.')

            cur.close()
            db.close()

        elif message.content.lower() == f'{b_t} roulette help':
            await message.channel.send(f'**:money_with_wings: :dollar: :money_with_wings: :dollar: :money_with_wings: :dollar: :money_with_wings: :moneybag: ZEBOT ROULETTE :moneybag: :money_with_wings: :dollar: :money_with_wings: :dollar: :money_with_wings: :dollar: :money_with_wings:**\n\n:white_check_mark: **FORMAT**: `{b_t} roulette <number in range -14 to 14> <points to bet>` :white_check_mark:\n\n:white_small_square: A **negative** number `-N` represents the colour **Black**, a **positive** number `N` denotes **Red**, while the number **0** denotes **Green**.\n:white_small_square: A number representing the same colour as that of the rolled number will award you **2x** points.\n:white_small_square: If your number and its colour are same as the rolled one, you\'ll be rewarded **20x** points.\n:white_small_square: If your number hits the jackpot, i.e. **0**, you\'re in for a treat with **200x** points!\n:black_small_square: ||And if you hit none of these, you just lose the points that you bet. *(oof)*||\n\n:paperclip: **__NOTE :__**\n:pushpin: As starters you get **10** points to begin rolling.\n:pushpin: You can only bet an amount of integral value that\'s **more than 0**.\n:pushpin: The winning amount is added to your points pool after deducting the betting amount.\n:pushpin: To check your roulette stats on this server, type `{b_t} roulette stats`.\n:pushpin: To reset your roulette stats on this server, type `{b_t} roulette reset`.')

        elif message.content.lower() == f'{b_t} roulette reset':
            if user_schema_tuple in users_schema_list:
                db = psycopg2.connect(host=dbhost, user=dbuser, password=dbpw, database=dbdb)
                cur = db.cursor()
                cur.execute(f'select guild from u_{message.author.id}.roulette;')
                user_roul_guilds_list = cur.fetchall()
                cur.close()
                db.close()

                if user_guild_tuple in user_roul_guilds_list:
                    await message.channel.send(f'**Do you really want to reset all your roulette stats, {message.author.mention}?** `type y/yes to confirm`')
                    try:
                        def check(msg):
                            return msg.author == message.author and msg.channel == message.channel

                        reset_msg = await client.wait_for('message', check=check, timeout=15)

                        if reset_msg:
                            if reset_msg.content.lower() in ['y', 'yes']:
                                db = psycopg2.connect(host=dbhost, user=dbuser, password=dbpw, database=dbdb)
                                cur = db.cursor()
                                cur.execute(f'update u_{message.author.id}.roulette set rolls = 0, points = 10 where guild = {message.guild.id}')
                                db.commit()
                                cur.close()
                                db.close()
                                await message.channel.send(f'**{message.author.mention} your `rolls` and `points` have been reset to `0` and `10` respectively.**')
                            else:
                                await message.channel.send(f'**No reset confirmation received. Dismissing roulette stats reset request by {message.author.mention}.**')
                    except asyncio.futures.TimeoutError:
                        await message.channel.send(f'**Reset confirmation timed out. Dismissing roulette stats reset request by {message.author.mention}.**')
                else:
                    await message.channel.send(f'**You\'re not signed up for playing roulette in this server yet! Type `{b_t} roulette signup` to join this server\'s roulette club!**')
            else:
                await message.channel.send(f'**You\'re not signed up for playing roulette yet! Type `{b_t} roulette signup` to join this server\'s roulette club!**')

        elif user_schema_tuple in users_schema_list:
            db = psycopg2.connect(host=dbhost, user=dbuser, password=dbpw, database=dbdb)
            cur = db.cursor()
            cur.execute(f'select guild from u_{message.author.id}.roulette;')
            user_roul_guilds_list = cur.fetchall()
            cur.close()
            db.close()

            if user_guild_tuple in user_roul_guilds_list:

                try:
                    if message.content.lower() == f'{b_t} roulette stats':
                        db = psycopg2.connect(host=dbhost, user=dbuser, password=dbpw, database=dbdb)
                        cur = db.cursor()
                        cur.execute(f'select * from u_{message.author.id}.roulette where guild = {message.guild.id}')
                        data_roulette = cur.fetchone()
                        cur.close()
                        db.close()
                        await message.channel.send(f'{message.author.mention} you\'ve rolled **{data_roulette[1]}** times till now and you have **{data_roulette[2]}** roulette points in your pool.')

                    elif len(message.content.split()) == 4 and int(message.content.split()[2]) in range(-14, 15):
                        user_roll = int(message.content.split()[2])
                        user_bet = int(message.content.split()[3])

                        db = psycopg2.connect(host=dbhost, user=dbuser, password=dbpw, database=dbdb)
                        cur = db.cursor()
                        cur.execute(f'select * from u_{message.author.id}.roulette where guild = {message.guild.id}')
                        data_roulette = cur.fetchone()

                        if data_roulette[2] >= user_bet:
                            if user_bet > 0:
                                computed_roll = roul(-14, 14)

                                def roll_colour():
                                    return discord.Colour.green() if computed_roll == 0 else discord.Colour.dark_red() if computed_roll > 0 else discord.Colour.from_rgb(0, 0, 0)

                                roulembed = discord.Embed(colour=roll_colour())
                                roulembed.set_image(url=roul_num_img_gen(computed_roll))
                                roulembed.set_author(name=f'{message.author} rolled:', icon_url=message.author.avatar_url)
                                roulembed.set_footer(text=f'{verinfo}', icon_url=client.user.avatar_url)

                                update_roulette_data = f'update u_{message.author.id}.roulette set rolls = %s, points = %s where guild = {message.guild.id}'

                                if user_roll == computed_roll:
                                    if user_roll == 0:
                                        cur.execute(update_roulette_data, (data_roulette[1] + 1, data_roulette[2] + 199 * user_bet))
                                        db.commit()
                                        cur.close()
                                        db.close()
                                        await message.channel.send(embed=roulembed, content=f'**JACKPOT!** {message.author.mention} JUST WON **{200 * user_bet}** ROULETTE POINTS!\nYour current roulette points: **{data_roulette[2] + 199 * user_bet}**')

                                    else:
                                        cur.execute(update_roulette_data, (data_roulette[1] + 1, data_roulette[2] + 19 * user_bet))
                                        db.commit()
                                        cur.close()
                                        db.close()
                                        await message.channel.send(embed=roulembed, content=f'**Bull\'s eye!** {message.author.mention} just won **{20 * user_bet}** points!\nYour current roulette points: **{data_roulette[2] + 19 * user_bet}**')

                                elif (user_roll < 0 and computed_roll < 0) or (user_roll > 0 and computed_roll > 0):
                                    cur.execute(update_roulette_data, (data_roulette[1] + 1, data_roulette[2] + user_bet))
                                    db.commit()
                                    cur.close()
                                    db.close()
                                    await message.channel.send(embed=roulembed, content=f'\'Grats {message.author.mention}! You just won **{2 * user_bet}** points!\nYour current roulette points: **{data_roulette[2] + user_bet}**')

                                else:
                                    cur.execute(update_roulette_data, (data_roulette[1] + 1, data_roulette[2] - user_bet))
                                    db.commit()
                                    cur.close()
                                    db.close()
                                    await message.channel.send(embed=roulembed, content=f'There\'s nothing for you right now, {message.author.mention}. Better luck next time!\nYour current roulette points: **{data_roulette[2] - user_bet}**')

                            else:
                                await message.channel.send('**You can only bet an amount of integral value that\'s more than 0.**')
                        else:
                            cur.close()
                            db.close()
                            await message.channel.send(f'**Sorry {message.author.mention}! You don\'t have sufficient points to bet {user_bet} points right now.**\nYour current roulette points: **{data_roulette[2]}**')
                    else:
                        await message.channel.send('**Invalid input!** Type `zeb roulette help` in chat if you need some assistance.')
                except ValueError:
                    await message.channel.send('**Invalid input!** Type `zeb roulette help` in chat if you need some assistance.')
            else:
                await message.channel.send(f'**You\'re not signed up for playing roulette in this server yet! Type `{b_t} roulette signup` to join this server\'s roulette club!**')
        else:
            await message.channel.send(f'**You\'re not signed up for playing roulette yet! Type `{b_t} roulette signup` to join this server\'s roulette club!**')


client.run(token)
