from discord.ext import commands
import discord


class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        logs = self.bot.get_channel()
        embed = discord.Embed(title=f'Message deleted in {message.channel}', colour=discord.Color.blue())
        embed.add_field(name=f'Sender: {message.author}', value=f'Message: {message.content}')
        await logs.send(embed=embed)


def setup(bot):
    bot.add_cog(Startup(bot))