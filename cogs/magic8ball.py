from discord.ext import commands
import random

class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['m8b', '8ball', 'magicball'])
    async def magic8ball(self, ctx, *, question):
        answers = [
            'It is certain',
            'It is decidedly so',
            'Without a doubt',
            'Yes, definitely',
            'You may rely on it',
            'Ah I see it, yes',
            'Most likely',
            'Outlook good',
            'Yes',
            'Signs point to yes',
            'Reply hazy try again',
            'Ask again later',
            'Better not tell you now',
            'Cannot predict now',
            'Concentrate and ask again',
            "Don't count on it",
            'My reply is no',
            'My sources say no',
            'Outlook not so good',
            'Very doubtful'
        ]
        reply = random.choice(answers)
        await ctx.send(f"{ctx.author.mention} {reply}.")


def setup(bot):
    bot.add_cog(Startup(bot))