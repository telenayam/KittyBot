import discord
from discord.ext.commands import Bot
from discord.ext import commands
from time import *
import asyncio

client = discord.Client()
Client = commands.Bot(command_prefix = "")

async def my_background_task():
    await client.wait_until_ready()
    global counter
    counter = 7
    channel = discord.Object(id=401429023114133510)
    while not client.is_closed:
        if counter > 11:
            counter = 0
        await client.send_message(channel, counter)
        await asyncio.sleep(3600) # task runs every 60 minutes
        counter += 1

        

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.upper().startswith('Q'):
        userID = message.author.id
        await client.send_message(message.channel, counter)
    if message.content.upper().startswith('!C'):
        args = ['Might','Resources','Troops','Monster','Construction','Troops','Monster','Resources','Research','Troops','Monster']
        await client.send_message(message.channel, "**Current Quest : %s**" % (args[counter]))
    if message.content.upper().startswith('!N'):
        args = ['Might','Resources','Troops','Monster','Construction','Troops','Monster','Resources','Research','Troops','Monster']
        await client.send_message(message.channel, "**Next Quest : %s**" % (args[counter+1]))
    if message.content.upper().startswith('!L'):
        args = ['Might','Resources','Troops','Monster','Construction','Troops','Monster','Resources','Research','Troops','Monster','Might','Resources','Troops','Monster','Construction','Troops','Monster','Resources','Research','Troops','Monster']
        ind_pos = [counter,counter+1,counter+2,counter+3,counter+4,counter+5,counter+6,counter+7,counter+8,counter+9,counter+10]
        await client.send_message(message.channel, "**Current Quest : %s**" % (args[counter:counter+11]))
        
client.loop.create_task(my_background_task())

client.run("NDAxMzgwNDI5MzQyNTcyNTU1.DTseKw.BNRX2aSovvDj8RD9LUT5UyZLzTY")
