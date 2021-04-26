from discord.ext import commands
import discord


class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Displays a detailed list of useful commands
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Here, check out some of my awesome features!",
                              description='Use !help <command> for extended information on a command.',
                              colour=discord.Colour.blue(), url='https://sexkardun.ga')
        # embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
        embed.set_thumbnail(url='https://static.wixstatic.com/media/ce33e6_1bcf87668c56491694ecffda5c7b910a~mv2.png/v1'
                                '/fill/w_401,h_280,al_c,q_85,usm_0.66_1.00_0.01/main_logo.webp')
        embed.set_footer(text="For any further help or suggestions contact the online Mods.")

        embed.add_field(name='!mimic/!echo/!say', value='Repeats after you', inline=False)

        embed.add_field(name='!user (mention_user)', value='Gives information about the requested user', inline=False)

        embed.add_field(name='!mute (Mod only)', value='Mutes the mentioned user', inline=False)
        embed.add_field(name='!unmute (Mod only)', value='Unmutes the mentioned user', inline=False)

        embed.add_field(name='!kick (Mod only)', value='Kicks the mentioned user', inline=False)
        embed.add_field(name='!ban (Mod only)', value='Bans the mentioned user', inline=False)

        embed.add_field(name='!purge/!clear (Mod only)', value='Deletes bulk messages', inline=False)
        embed.add_field(name='!bully/!roast (mention_user)', value="Bullies the mentioned user", inline=False)
        embed.add_field(name='!sendcode email_here', value='Sends TFA email for verified role', inline=False)
        embed.add_field(name='!magic8ball question_here', value='Magic 8 ball', inline=False)
        embed.add_field(name='!tictactoe/!ttt', value='Tic Tac Toe game', inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Startup(bot))