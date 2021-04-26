from discord.ext import commands
from discord.ext.commands import has_permissions
import discord

class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Deletes messages in bulk (Mod only)
    @commands.command(aliases=['purge'])
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        logchannel = self.bot.get_channel()
        await ctx.channel.purge(limit=amount + 1)
        embed = discord.Embed(title=f"{ctx.author} deleted {amount} messages.", colour=discord.Colour.dark_grey())
        await ctx.send(embed=embed, delete_after=5)
        await logchannel.send(embed)


def setup(bot):
    bot.add_cog(Startup(bot))