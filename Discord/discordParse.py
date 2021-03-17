import discord
import twitch_check

from discord.ext import commands
import asyncio

import os
from dotenv import load_dotenv
load_dotenv()

# Command parser DO NOT TOUCH
async def parse_command(message):
    parse = message.content.split(' ')
    
    if(len(parse) > 1):
        await commandList[parse[0]](message, parse[1])
    else:
        await commandList[parse[0]](message)

# --------- COMMANDS --------- #
# To add basic text commands follow this model:
# async def commandName(message):
#     await message.channel.send("Bot Message")

async def hello(message):
    await message.channel.send("Hello!")

async def is_streaming(message):
    if twitch_check.is_streaming(os.getenv('CHANNEL')) == True:
        await message.channel.send('YUP')

    else:
        await message.channel.send('NOPE')

# --------- COMMAND LIST --------- #
# After creating your command, you must add it to
# the command list with this format:
# "!commandName" : commandName
# DO NOT forget to add the , !

commandList = {
    "!hello" : hello,
    "!isStreaming" : is_streaming
}