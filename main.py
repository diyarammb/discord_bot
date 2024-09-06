import discord
from discord.ext import commands
from Api import *
intents = discord.Intents.default()
intents.message_content = True 
intents.members = True 

# client = commands.Bot(command_prefix='!', intents=intents)
client = commands.AutoShardedBot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print("This bot is now ready for use")
    print("-------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am Daya. How can I help you?")

@client.event
async def on_member_join(memeber):
    print("Hello")

client.run(token)

