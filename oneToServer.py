import discord
from discord.ext import commands
from Api import *
intents = discord.Intents.default()
intents.message_content = True

client = commands.AutoShardedBot(command_prefix='!', intents=intents)

SOURCE_CHANNEL_ID = 1039655044351529032   
TARGET_CHANNEL_ID = 1267864047618097222  

@client.event
async def on_ready():
    print(f'Bot is ready. Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.channel.id == SOURCE_CHANNEL_ID and message.author != client.user:
        target_channel = client.get_channel(TARGET_CHANNEL_ID)
        if target_channel:
            await target_channel.send(f'{message.author.name}: {message.content}')
        if message.attachments:
          for attachment in message.attachments:
             await target_channel.send(attachment.url)    
    
    await client.process_commands(message)

client.run(token)
