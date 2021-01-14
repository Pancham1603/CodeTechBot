import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio
import aiohttp
import random
import smtplib
import config
# import os

bot = commands.Bot(command_prefix="!")

def sendverifymail(receiver, message):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(config.EMAIL_ADDRESS, config.PASSWORD)
    server.sendmail(config.EMAIL_ADDRESS, receiver, message)
    server.quit()

@bot.event
async def on_ready():
    print('Bot is ready')
    print('Logged in as')
    print(bot.user.name)
    print('---------')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "!subhajit":
        await message.channel.send('ew')
    messageauthor = message.author
    msg = message.content
    print(f"{messageauthor} said {msg}")
    await bot.process_commands(message)


@bot.command()
async def sendcode(ctx,*, email):
    code = random.randint(100000, 999999)
    subject = 'CodeTech BVN DISCORD VERIFICATION'
    msg = f"""
            Welcome to CodeTech BVN's official Discord Server!
                Type '!verify XXXXXX' in the verify channel to get verified.
                Your verification code is {code}
            Regards,
            Team CodeTech
            Birla Vidya Niketan
            """
    message = 'Subject: {}\n\n{}'.format(subject, msg)
    sendverifymail(email, message)
    await ctx.send(f'{ctx.author.mention} Check your inbox and verify by using the command !verify XXXXXX')
    return code





#@bot.command()
#async def verify(ctx,*,input):


@bot.command()
async def bully(ctx, member: discord.Member):
    savage_lines = ['Remember when I asked for your opinion? Me neither.',
                    'Your ass must be jealous of all that shit that comes out of your mouth.',
                    'I’m really jealous of all the people who have never met you.',
                    'Whenever I see your face, I’m reminded that God has a great sense of humor.',
                    'Wipe your mouth, there’s a little bit of bullshit around your lips.',
                    'I know that everyone is allowed to act stupid once in awhile, but you’re really abusing that privilege.',
                    'You and Monday are really similar — nobody likes you.',
                    'There are some really dumb people in this world. Thanks for helping me understand that.',
                    'Good story bro, but in what part do you shut the fuck up?',
                    'I think I might have Alzheimer’s because I can’t remember when was the last time I asked for your opinion.',
                    'If ignorance is really a bliss, you must be the happiest person in the world.',
                    'Jesus loves you but everyone thinks you’re a jerk.',
                    'I would love to insult you but I’m afraid I wouldn’t do as well as nature did.',
                    'Your d*ck belongs in your pants, not your personality.',
                    'I love the sound you make when you shut up.',
                    'The jerk store called, they’re running out of you.',
                    'Remember that time you shut the f*ck up? Me neither',
                    'I hope one day you choke on all the shit you talk.',
                    'It is actually pretty easy not to be a shitty human being. Try it sometime.',
                    'I  am returning your nose. I found it in my business.',
                    'You’re like a bag of Pampers. Self absorbed and full of shit.',
                    'I would tell you to go f*ck yourself but I’m pretty sure you’d be disappointed.',
                    'Since you know it all, you should know when to shut the f*ck up.',
                    'Yep, no doubt about it, your father should have pulled out earlier.',
                    'I swear some men were conceived by anal sex. There is no way being that much of an asshole is natural.',
                    'I’m not a proctologist but I sure know an asshole when I see one.',
                    'I hear there’s a new app called a sense of humour. Download it bitch or take some from me!',
                    'You’re like a plunger, you like bringing up old shit.',
                    'Acting like a d*ck won’t make yours any bigger.',
                    'I should feel bad about what you are saying but you’re not worth it.']

    line = random.choice(savage_lines)

    # pancham = discord.utils.get(ctx.server.roles, name = 'CT#Vice Prez')

    # if pancham in member.role_mentions:
    #     await ctx.send(f'{ctx.author.mention} {line}')
    #     await ctx.send(f"{ctx.author.mention} You can't bully the god.")

    await ctx.send(f"{member.mention} {line}")


@bot.command(aliases=['echo', 'say'])
async def mimic(ctx, *, words: commands.clean_content):
    channel = ctx.channel
    msg = discord.utils.get(await channel.history(limit=100).flatten(), author=ctx.author)
    await msg.delete()
    await ctx.send(words)


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.command()
async def cthelp(ctx):
    embed = discord.Embed(title="Here, check out some of my awesome features!", description='  ',
                          colour=discord.Colour.blue(), url='***REMOVED***')
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
    embed.add_field(name='!bully (mention_user)', value="Bullies the mentioned user", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def user(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = []
    for role in member.roles:
        roles.append(role)

    embed = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at)
    embed.set_author(name=f'User Info - {member}')
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID         ', value=member.id, inline=False)
    embed.add_field(name="Name       ", value=member.display_name, inline=False)
    embed.add_field(name='Created on      ', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'),
                    inline=False)
    embed.add_field(name='Member since    ', value=member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'),
                    inline=False)
    embed.add_field(name='Roles      ', value=''.join([role.mention for role in roles]), inline=False)
    embed.add_field(name='Power      ', value=member.top_role.mention, inline=False)
    embed.add_field(name='Bot      ', value=member.bot, inline=False)

    await ctx.send(embed=embed)


@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason='No reason'):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} was kicked by {ctx.author.mention}. [{reason}]")


@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason='No reason'):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} was banned by {ctx.author.mention}. [{reason}]")


@bot.command(aliases=['purge'])
@has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{ctx.author} deleted {amount} messages.", delete_after=5)


@bot.command()
async def addevent(ctx, *, event=None):
    upcoming = []
    if event != None:
        upcoming.append(event)
    else:
        ctx.channel.send("This command requires an event name.")

    embed = discord.Embed(title="Upcoming Events")
    embed.set_footer(text="To add an event use !addevent command.")
    embed.add_field(name=event, value='Command under development')

    await ctx.send(embed=embed)


@bot.command()
@has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member, *, reason='No reason'):
    muterole = ctx.guild.get_role(***REMOVED***)
    await member.add_roles(muterole)
    await ctx.send(f"{member} was muted indefinitely by {ctx.author}. [{reason}]")


@bot.command()
@has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    muterole = ctx.guild.get_role(***REMOVED***)
    await member.remove_roles(muterole)
    await ctx.send(f"{member} was unmuted by {ctx.author}")


async def changepresence():
    await bot.wait_until_ready()
    while not bot.is_closed():
        statuses = ['!cthelp', 'Under development :/']
        status = random.choice(statuses)
        await bot.change_presence(activity=discord.Game(status))
        await asyncio.sleep(3)


# for cog in os.listdir('.\\cogs'):
#   if cog.endswith('.py'):
#      try:
#         cog = f"cogs.{cog.replace('.py', '')}"
#        bot.load_extension(cog)
#   except Exception as e:
#      print(f"{cog} can't be loaded ")
#     raise e
# bot.load_extension('cogs/moderation.py')

token = 'Nzk3NTM3NTAxNDQ2OTMwNDYz.X_n6rQ.GaxI936_Q7x1BQS0LrQjCEzZkxE'
bot.loop.create_task(changepresence())
bot.run(token)
