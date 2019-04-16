# zebot

A simple Discord BOT which is still under development.

### COMMANDS (till now)
- `zeb help` : list of available commands
- `zeb guilds` : list of servers with **zebot**
- `zeb greet <@user1> <@user2> ...` : greet people by mentioning them
- `zeb rtd` : roll a die
- `zeb slap <@user1> <@user2> ...` : I wonder what this does... maybe I'll try it on myself
- `zeb server roles` : info about every role in the server

### INTERNAL FEATURES (till now)
- logs the messages of joined servers into the 'zebot dev' server. message information contains:
  - name of user, server and channel
  - date and time of messaging
  - attachment url (if any)
  - text content of message
  - distinguishes bot messages from humans and logs them into separate 'zebot dev' channels
- logs the joining/removal of zebot to/from servers
- logs DMs sent directly to zebot

#### If you want to share some ideas regarding this bot, just DM me @ my Discord `zeborg#4589`
