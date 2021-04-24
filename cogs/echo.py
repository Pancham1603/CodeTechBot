from discord.ext import commands
import discord


class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Repeats whatever is typed and deletes the user command
    @commands.command(aliases=['echo', 'say'])
    async def mimic(self, ctx, *, words: commands.clean_content):
        channel = ctx.channel
        msg = discord.utils.get(await channel.history(limit=100).flatten(), author=ctx.author)
        await msg.delete()
        await ctx.send(words)


def setup(bot):
    bot.add_cog(Startup(bot))