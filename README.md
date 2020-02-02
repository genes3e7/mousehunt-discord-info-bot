# Mousehunt discord info bot
Displaying of information of many often referenced things in mousehunt.<br/>
This bot is made for practice purposes as such will not often be updated.<br/>
Main objective of creating a chat bot for the first time and getting used to github.

## Pre-requisites
1. Go to discord's [developer portal](https://discordapp.com/developers/applications)
2. Create a New Application
3. Choose a good name for your discord bot
4. Go to the Bot tab, create a new bot.
5. Copy the token, you will need it later.
    - However do not ever lose this token.
    - If your token is somehow compromised, regenerate a new token
6. Select public bot if you wish for anyone else to be able to reuse your bot in their server.
7. Go to the OAuth2 tab, under scopes select bot.
8. Copy and paste the url into your browser
9. Select the server where you wish to place the bot in and Authorize.

## To run the backend of the bot.
1. Run the python script using [mhdiscordbot.py](./mhdiscordbot.py) as the starting point.
2. Enter token when prompted or as commandline argument when running script from terminal

## All features
| No. | Command | Description |
|:---:|:-----------------------:|:------------------------------------------------------------------------:|
| 1 | `....prestigestats` | Checking prestige base stats |
| 2 | `....vriftfragcore` | Checking number of frag or core<br>in valor rift |
| 3 | `....aboutprestigebase` | Display floors where prestige base<br>starts to match other popular base |
| 4 | `....vriftfloorcache` | Displays floor cache of<br>particular floor |

## Credits, references and other details
- Change Log: [Here](./changelog.md)
- discord api: [Here](https://discordpy.readthedocs.io/en/latest/api.html)
