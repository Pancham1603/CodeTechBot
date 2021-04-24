from discord.ext import commands
from discord.ext.commands import has_permissions

class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Deletes messages in bulk (Mod only)
    @commands.command(aliases=['purge'])
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        logchannel = self.bot.get_channel(***REMOVED***)
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"{ctx.author} deleted {amount} messages.", delete_after=5)
        await logchannel.send(f"{ctx.author} deleted {amount} messages in {ctx.channel}")

def setup(bot):
    bot.add_cog(Startup(bot))