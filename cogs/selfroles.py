from discord.ext import commands
from discord.ext.commands import has_permissions
import discord

class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot




def setup(bot):
    bot.add_cog(Startup(bot))