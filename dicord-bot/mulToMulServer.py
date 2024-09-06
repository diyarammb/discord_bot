import discord
from discord.ext import commands
from Api import *

intents = discord.Intents.default()
intents.message_content = True
intents.message_content = True  # Ensure this is set to enable message content

client = commands.AutoShardedBot(command_prefix='!', intents=intents)

# Define mappings of source channels to target channels
CHANNEL_MAPPINGS = {
    1267863979217256448: 1270685372938063933,  # Source channel ID: Target channel ID
    1039654795650269264: 1267543834825588767,  # Add more mappings as needed
}

@client.event
async def on_ready():
    print(f'Bot is ready. Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.channel.id in CHANNEL_MAPPINGS and message.author != client.user:
        target_channel_id = CHANNEL_MAPPINGS[message.channel.id]
        target_channel = client.get_channel(target_channel_id)
        
        if target_channel:
            content = message.content
            author = message.author.name
            timestamp = message.created_at.strftime("%Y-%m-%d %H:%M:%S")

            forward_message = f'**{author}** at {timestamp}:\n{content}'
            await target_channel.send(forward_message)
            
            if message.attachments:
                for attachment in message.attachments:
                    await target_channel.send(attachment.url)
    
    await client.process_commands(message)

client.run(token)
