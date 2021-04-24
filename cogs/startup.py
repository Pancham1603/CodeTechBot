from discord.ext import commands


class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')
        print(f'Logged in as: {self.bot.user.name}')
        print('-------------------')


    @commands.command()
    async def ping(self, ctx):
        print(ctx.author)
        print(ctx.channel.id)
        await ctx.send(f"Pong! **Latency: {round(self.bot.latency * 1000)}ms**")

def setup(bot):
    bot.add_cog(Startup(bot))
