# This project has been made by Pancham Agarwal for internal use in CodeTech BVN only.
# For any queries mailto: pancham1603@gmail.com

import asyncio
import random
import discord
from discord.ext import commands
import os
from pymongo import MongoClient
import random
import datetime


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command('help')


# Keeps changing the status of the bot
async def changepresence():
    await bot.wait_until_ready()
    while not bot.is_closed():
        statuses = ['!help', 'Under development :/', 'check out upcoming !events', 'ask the ball !m8b', 'tictactoe !ttt']
        status = random.choice(statuses)
        await bot.change_presence(activity=discord.Game(status))
        await asyncio.sleep(3)


bot.load_extension('cogs.bully')
bot.load_extension('cogs.echo')
bot.load_extension('cogs.events')
bot.load_extension('cogs.help')
bot.load_extension('cogs.logos')
bot.load_extension('cogs.magic8ball')
bot.load_extension('cogs.moderation')
# bot.load_extension('cogs.mod_moderation')
bot.load_extension('cogs.purge')
bot.load_extension('cogs.simpalert')
bot.load_extension('cogs.tictactoe')
bot.load_extension('cogs.userinfo')
bot.load_extension('cogs.verification')
bot.load_extension('cogs.welcomer')
bot.load_extension('cogs.startup')


token = '***REMOVED***'  # input the unique bot token from dev panel (string)
bot.loop.create_task(changepresence())  # to change status every 3 seconds
bot.run(token)  # finally run the bot
