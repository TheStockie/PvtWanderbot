# PvtWanderbot    ![logo](https://cdn.discordapp.com/avatars/807240437936554004/8c374795c7d790b36dd6e595ad9bb196.png?size=32)
Welcome to my Twitch and Discord Bots!
This has been a small passion project that I want to expand quite a bit in the coming months.

Currently, the bots are very bare bones but a good starting point if you don't want to get too much into the Twitch and Discord APIs.

### Discord
The Discord bot is programmed in [Python 3.9](https://www.python.org/downloads/), using the [Discord.py](https://discordpy.readthedocs.io/en/latest/index.html) API wrapper.

It's current functionality is:
- Connection to Discord Servers
- Basic Text Commands
- Twitch Username ID Parsing (Used for checking if a channel is streaming)
- Bot Presence Changing

### Twitch
The Twitch bot is programmed in [NodeJS](https://nodejs.org/en/download/), using the [TMI.js](https://github.com/tmijs/tmi.js) library.

It's current functionality is:
- Connection to Twitch Chats
- Basic Text Commands

# Setup
Firstly, install [Python 3.9](https://www.python.org/downloads/) and [NodeJS](https://nodejs.org/en/download/) to execute the bots. For ease of use and data protection, this project uses [dotENV](https://github.com/motdotla/dotenv#dotenv) and [Python-dotEnv](https://github.com/theskumar/python-dotenv#python-dotenv) for all the sensitive information!

## Discord
Create a text file in the Discord folder called .env (No name, only file extension) and open it in a text editor. Inside the .env you must write these variables, with these names and your specific bots information:
```
TOKEN = 'Bot-Token'
CLIENT_ID = 'Twitch-Bot-ID'
CHANNEL = 'Your-Channel'
```
Make sure this information has the apostrophes at either side!

## Twitch
Just like with the Discord bot, create a text file in the Twitch folder called .env and open it in a text editor. Inside write:
```
USERNAME = Twitch-Bot-Username
PASSWORD = Twitch-Bot-Password
CHANNELS = Your-Channel
```
This time, no need to add any apostrophes, just write the information!

# Execution
You're nearly there! Now open two command prompts and navigate to your source folder.
### Discord
For Discord, navigate to the Discord folder and execute this command:
```
python mainDiscord.py
```

### Twitch
For Twitch, navigate to the Twitch folder and execute this command:
```
node mainTwitch.js
```

Now you should have two command prompts, one running each bot and that's it!

# Fair Use
This project falls under the MIT License, so you're more than welcome to use, modify and reupload it!

The project does not require you to credit myself as the bot author, but it would be very much appretiated! Have fun and happy streaming!
