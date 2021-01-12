#CODETECH BVN DISCORD BOT MADE BY PANCHAM AGARWAL

import discord
from discord.ext import commands


client = commands.Bot(command_prefix= "ct!")


@client.event
async def on_ready():
    print("Bot is ready!")


@client.event
async def on_member_join(member):
    print("new member")


@client.event
async def on_member_remove(member):
    print("member left")


@client.command()
async def ping(ctx):
    await ctx.send('pong')


@client.event
async def on_message(message):
    server = client.get_guild(738328219027111966)
    abuse = ['fuck', 'bastard', 'bc', 'chutiya']

    for word in abuse:
        if message.content.count(word.lower()) > 0:
            await message.channel.purge(limit=1)

    if message.content == "ct!help":
        embed = discord.Embed(title="CTBot Commands", description='Some useful commands')
        embed.add_field(name="ct!users", value="Tells the number of members in the server")
        embed.add_field(name="ct!subhajit", value="Bullies Subhajit the SIMP :)")
        await message.channel.send(content=None, embed=embed)

    if message.content.find("ct!hello") != -1:
        await message.channel.send("Hi!")
    elif message.content == "ct!users":
        await message.channel.send(f"""Members: {server.member_count}""")
    elif message.content == "ct!subhajit":
        await message.channel.send("ew") 


client.run("your token here")
