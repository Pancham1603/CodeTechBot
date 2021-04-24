from discord.ext import commands
import discord


class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['logos'])
    async def logo(self, ctx):
        await ctx.send(file=discord.File('codetechbot/images/codetech_assets.zip'))


def setup(bot):
    bot.add_cog(Startup(bot))