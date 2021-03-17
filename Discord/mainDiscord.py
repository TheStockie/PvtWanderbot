import discord
import os
import discordParse
import twitch_check

from discord.ext import tasks, commands
from itertools import cycle
import asyncio

from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

# ENV values
TOKEN = os.getenv('TOKEN')
CHANNEL = os.getenv('CHANNEL')

# Console log for joining and execution of any function needed on boot
@client.event
async def on_ready():
    print('I have arrived with {0.user}'.format(client))
    
    change_status.start()
    check_streaming.start()

# Call to discordParse.py when message is sent starting with !
@client.event
async def on_message(message):
    if(message.content.startswith("!")):
        await discordParse.parse_command(message)

# Simple presence cycle. Helps with knowing the bot is functioning well
status = cycle(['Classic', 'Ueda', 'Moment', 'CUM'])
@tasks.loop(seconds=1)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

# Looping function to check if x channel is streaming and send a message accordingly to a text chat
@tasks.loop(seconds=120)
async def check_streaming():
    global streaming_flag
    streaming_status = twitch_check.is_streaming(CHANNEL)

    if streaming_status == True and streaming_flag == False:
        # Change with your own channel ID and message before getting rid of the comment!
        # await client.get_channel(807227296616153129).send('@everyone Stockie is streaming over at https://twitch.tv/stockiestreams')
        streaming_flag = True
        print('YUP')

    if streaming_status == False:
        streaming_flag = False
        print('NOPE')

# Actually running the bot
client.run(TOKEN)