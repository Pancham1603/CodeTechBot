# This project has been made by Pancham Agarwal for internal use in CodeTech BVN only.
# For any queries mailto: pancham1603@gmail.com

import asyncio
import random
import smtplib
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import config

bot = commands.Bot(command_prefix="!")

TFAcodes = {}
botbully = {}

# Sends email by obtaining credentials from the config.py file
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


# Reacts to the mentioned messages
# @bot.event
# async def on_message(message):
#    if message.author == bot.user:
#        return
#    if message.content == "!subhajit":
#        await message.channel.send('ew')
#    messageauthor = message.author
#    msg = message.content
#    print(f"{messageauthor} said {msg}")
#    await bot.process_commands(message)


# Member welcome
@bot.event
async def on_member_join(member):
    doorchannel = bot.get_channel(***REMOVED***)
    verifychannel = bot.get_channel(***REMOVED***)
    await doorchannel.send(
        f"{member.mention} Welcome to the server! Type !sendcode <your_email> in {verifychannel.mention} to gain access to the server.")
    await bot.process_commands(member)


# Member leave
@bot.event
async def on_member_remove(member):
    doorchannel = bot.get_channel(***REMOVED***)
    await doorchannel.send(f"{member.mention} left the server.")
    await bot.process_commands(member)


# Sends a verification code to the inputted email-id using the sendverifymail() function
# Maps the generated code with the user's discord name until the user is verified
@bot.command()
async def sendcode(ctx, *, email):
    sendcode.code = random.randint(100000, 999999)
    subject = f'CodeTech BVN Discord Verification ({sendcode.code})'
    msg = f"""
Hey {ctx.author.name}! Welcome to CodeTech BVN's official Discord Server!
Type '!verify XXXXXX' in the verify channel to get verified.
Your verification code is {sendcode.code}

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
    await ctx.send(f'{ctx.author.mention} Check your inbox and verify by using the command !verify XXXXXX')
    member = ctx.author
    TFAcodes[member] = sendcode.code


# Verifies the new user with the code generated above
# Deletes the key from the map one the user gets verified
@bot.command()
async def verify(ctx, *, pin):
    member = ctx.author
    if str(pin) == str(TFAcodes.get(member)):
        del TFAcodes[member]
        verifyrole = ctx.guild.get_role(***REMOVED***)
        genchannel = bot.get_channel(***REMOVED***)
        await member.add_roles(verifyrole)
        await genchannel.send(f"{ctx.author.mention} You are now verified.")
        await ctx.send('Verified')
        await ctx.send(
            "New members: Request a code by using '!sendcode email_here' and then verify by using '!verify code_here'")
    else:
        await ctx.send(f'{ctx.author.mention} Invalid code!')
        await ctx.send("Request a code by using '!sendcode email_here' and then verify by using '!verify code_here'")
        del TFAcodes[member]


# Bullies the mentioned user with a random line
@bot.command(aliases=['roast'])
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

    if member.id == ***REMOVED***:
        await ctx.send(f'{ctx.author.mention} {line}')
        await ctx.send(f"{ctx.author.mention} You can't bully the god.")
    elif member.id == ***REMOVED***:
        if ctx.author in botbully:
            muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
            await ctx.author.add_roles(muted_role)
            await ctx.send(f"{ctx.author.mention} I muted you for 5min lol")
            del botbully[ctx.author]
            await asyncio.sleep(300)
            await ctx.author.remove_roles(muted_role)
            await ctx.send(f'{ctx.author.mention} You have been unmuted.')
        else:
            botbully[ctx.author] = 1
            await ctx.send(f'{ctx.author.mention} Do it once more then you see :)')
    else:
        await ctx.send(f"{member.mention} {line}")


# Repeats whatever is typed and deletes the user command
@bot.command(aliases=['echo', 'say'])
async def mimic(ctx, *, words: commands.clean_content):
    channel = ctx.channel
    msg = discord.utils.get(await channel.history(limit=100).flatten(), author=ctx.author)
    await msg.delete()
    await ctx.send(words)


# Test command
@bot.command()
async def ping(ctx):
    print(ctx.author)
    await ctx.send(f"Pong! **Latency: {round(bot.latency * 1000)}ms**")


# Displays a detailed list of useful commands
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
    embed.add_field(name='!bully/!roast (mention_user)', value="Bullies the mentioned user", inline=False)
    embed.add_field(name='!sendcode email_here', value='Sends TFA email for verified role', inline=False)
    embed.add_field(name='!magic8ball question_here', value='Magic 8 ball', inline=False)
    await ctx.send(embed=embed)


# Displays full info of the requested user
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


# Kicks the mentioned user (Mod only)
@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason='No reason'):
    logchannel = bot.get_channel(***REMOVED***)
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} was kicked by {ctx.author.mention}. [{reason}]")
    await logchannel.send(f"{member.mention} was kicked by {ctx.author.mention}. [{reason}]")


# Bans the mentioned user (Mod only)
@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason='No reason'):
    logchannel = bot.get_channel(***REMOVED***)
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} was banned by {ctx.author.mention}. [{reason}]")
    await logchannel.send(f"{member.mention} was banned by {ctx.author.mention}. [{reason}]")


# Deletes messages in bulk (Mod only)
@bot.command(aliases=['purge'])
@has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    logchannel = bot.get_channel(***REMOVED***)
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{ctx.author} deleted {amount} messages.", delete_after=5)
    await logchannel.send(f"{ctx.author} deleted {amount} messages in {ctx.channel}")


# Creates a list of upcoming events (under development)
@bot.command()
async def addevent(ctx, *, event=None):
    embed = discord.Embed(title="Upcoming Events")
    embed.set_footer(text="To add an event use !addevent command.")
    embed.add_field(name=event, value='Command under development')

    await ctx.send(embed=embed)


# Mutes the mentioned user (Mod only)
@bot.command()
@has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member, time='null', *, reason='No reason'):
    logchannel = bot.get_channel(***REMOVED***)
    # muterole = ctx.guild.get_role(***REMOVED***)
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    if time == 'null':
        await ctx.send(f'{ctx.author.mention} Please specify a time period!')
    else:
        if not time[-1].isalpha:
            tempmute = int(time[0]) * time_convert['m']
        else:
            tempmute = int(time[0]) * time_convert[time[-1]]
        await member.add_roles(muted_role)
        embed = discord.Embed(title=f"{member.name} has been muted for {time} by {ctx.author.name}", description=reason,
                              color=discord.Colour.blue())
        await ctx.send(embed=embed)
        await logchannel.send(f"{member} was muted for {time} by {ctx.author}. [{reason}]")

        await asyncio.sleep(tempmute)
        await member.remove_roles(muted_role)
        await ctx.send(f'{member.mention} You have been unmuted.')


# Unmutes the mentioned user (Mod only)
@bot.command()
@has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    logchannel = bot.get_channel(***REMOVED***)
    muterole = ctx.guild.get_role(***REMOVED***)
    await member.remove_roles(muterole)
    await ctx.send(f"{member.mention} was unmuted by {ctx.author.mention}")
    await logchannel.send(f"{member} was unmuted by {ctx.author}")


@bot.command()
async def play(ctx):
    channel = ctx.author.voice.channel
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if not voice.is_connected():
        await channel.connect()


@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send('I am not connected to any voice channel.')


@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        await voice.pause()
    else:
        await ctx.send('I am not playing any audio right now.')


@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        await voice.resume()
    else:
        await ctx.send('I am already playing audio.')


@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    await voice.stop()


@bot.command(aliases=['m8b', '8ball', 'magicball'])
async def magic8ball(ctx, *, question):
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


@bot.event
async def on_message_delete(message):
    logs = bot.get_channel(***REMOVED***)
    embed = discord.Embed(title=f'Message deleted in {message.channel}', colour=discord.Color.blue())
    embed.add_field(name=f'Sender: {message.author}', value=f'Message: {message.content}')
    await logs.send(embed=embed)


# Keeps changing the status of the bot
async def changepresence():
    await bot.wait_until_ready()
    while not bot.is_closed():
        statuses = ['!cthelp', 'Under development :/']
        status = random.choice(statuses)
        await bot.change_presence(activity=discord.Game(status))
        await asyncio.sleep(3)


token = 'Nzk3NTM3NTAxNDQ2OTMwNDYz.X_n6rQ.FlMhIWM6x_eeQV93Eibsn4C6lno'  # input the unique bot token from dev panel (string)
bot.loop.create_task(changepresence())  # to change status every 3 seconds
bot.run(token)  # finally run the bot
