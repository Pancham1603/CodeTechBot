from discord.ext import commands
import discord
import smtplib
import random

TFAcodes = {}
EMAIL_ADDRESS = '***REMOVED***'
PASSWORD = '***REMOVED***'


def sendverifymail(receiver, message):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS, PASSWORD)
    server.sendmail(EMAIL_ADDRESS, receiver, message)
    server.quit()


class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sendcode(self, ctx, *, email):
        await ctx.channel.purge(limit=1)
        self.sendcode.code = random.randint(100000, 999999)
        subject = f'CodeTech BVN Discord Verification ({self.sendcode.code})'
        msg = f"""
    Hey {ctx.author.name}! Welcome to CodeTech BVN's official Discord Server!
    Type '!verify XXXXXX' in the verify channel to get verified.
    Your verification code is {self.sendcode.code}

    Server Rules:
    1.  Please keep your messages as formal as possible: no cursing, no slangs, and no off-topic conversations. 
    2. Please be kind to other participants: don't write anything disrespectful or potentially offensive.
    3. Please do not write in all caps. 
    4. Please ONLY ping others when extremely urgent, and even then, only ping once and be patient. 
    5. No Spamming, no copy-pastes, no walls of text, ear-rape in voice channels, or even send weird messages to annoy people on purpose, etc.
    6. All chat must be in the respective channels. Random stuff and chit-chat to be done in #spam, use #general for important work. 
    7. Use Common Sense, if you think something might not be allowed, don't do it.
    8. Contact the moderators for roles, channel and personal vc.                
    We will strictly enforce the above set of rules and actively take action, depending on severity, against those in violation.

    Regards
    Team CodeTech
    Birla Vidya Niketan
    """
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        sendverifymail(email, message)
        embed = discord.Embed(title=f'{ctx.author.mention} Check your inbox and verify by using the command !verify XXXXXX', colour=discord.Colour.dark_orange())
        await ctx.send(embed=embed)
        member = ctx.author
        TFAcodes[member] = self.sendcode.code

    # Verifies the new user with the code generated above
    # Deletes the key from the map one the user gets verified
    @commands.command()
    async def verify(self, ctx, *, pin):
        member = ctx.author
        if str(pin) == str(TFAcodes.get(member)):
            del TFAcodes[member]
            verifyrole = ctx.guild.get_role(***REMOVED***)
            genchannel = self.bot.get_channel(***REMOVED***)
            await member.add_roles(verifyrole)
            embed = discord.Embed(title=f"{ctx.author.mention} You are now verified.", colour=discord.Colour.green())
            await genchannel.send(embed=embed)
            await ctx.send(embed=embed)
            embed = discord.Embed(title="New members: Request a code by using '!sendcode <email_here>' and then verify by using '!verify <code_here>'", colour=discord.Colour.dark_grey())
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(title=f"{ctx.author.mention} Invalid code!")
            await ctx.send(embed=embed)
            embed = discord.Embed(title="Request a code by using '!sendcode <email_here>' and then verify by using '!verify <code_here>'", colour=discord.Colour.dark_grey())
            await ctx.send(embed=embed)
            del TFAcodes[member]


def setup(bot):
    bot.add_cog(Startup(bot))
