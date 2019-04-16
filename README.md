# zebot

A simple Discord BOT which is still under development.

### COMMANDS (till now)
- `zebot help` : list of available commands
- `zebot guilds` : list of servers with **zebot**
- `zebot greet <@user1> <@user2> ...` : greet people by mentioning them
- `zebot rtd` : roll a die
- `zebot slap <@user1> <@user2> ...` : I wonder what this does... maybe I'll try it on myself
- `zebot server roles` : info about every role in the server

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
