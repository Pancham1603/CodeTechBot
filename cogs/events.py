from discord.ext import commands
from pymongo import MongoClient
from discord.ext.commands import has_permissions
import discord
import datetime
import random
from discord.utils import get
import asyncio

client = MongoClient(
    "***REMOVED***")
db = ***REMOVED***
collection1 = ***REMOVED***
collection2 = ***REMOVED***
collection3 = ***REMOVED***
collection4 = ***REMOVED***

embedColors = [discord.Color.blue(), discord.Color.blurple(), discord.Color.dark_blue(), discord.Color.dark_gold(),
               discord.Color.dark_green(), discord.Color.dark_grey(), discord.Color.dark_grey(),
               discord.Color.dark_magenta(),
               discord.Color.blue(), discord.Color.dark_orange(), discord.Color.dark_purple(),
               discord.Color.dark_red(),
               discord.Color.dark_teal(), discord.Color.darker_grey(), discord.Color.default(),
               discord.Color.gold(),
               discord.Color.green(), discord.Color.greyple(), discord.Color.light_grey(), discord.Color.magenta(),
               discord.Color.orange(), discord.Color.purple(), discord.Color.teal(),
               discord.Color.red()]


class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(kick_members=True)
    async def addevent(self, ctx, *, eventname):
        try:
            results = collection1.find()
            for result in results:
                _id = result['_id']
            _id += 1
        except:
            _id = 1
        collection1.insert_one(
            {'_id': _id, 'title': eventname, 'subevents': {}, 'added_by': f'{ctx.author.name}#{ctx.author.discriminator}',
             'time': datetime.datetime.now()})
        embed = discord.Embed(title=f'New Event: {eventname}', colour=random.choice(embedColors))
        embed.set_footer(text=f'Added by {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['event'])
    async def events(self, ctx, event_num=None):
        if event_num is None:
            results = collection1.find()
            embed = discord.Embed(title=f'CodeTech Events 2021-22',
                                  description="For info on any of the below listed events use !events <event_num>, to register use !startreg <event_num>",
                                  colour=random.choice(embedColors))
            embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
            for result in results:
                _id = result['_id']
                eventname = result['title']
                try:
                    description = result['description']
                except:
                    description = None
                if description:
                    embed.add_field(name=f"{_id}. {eventname}", value=description, inline=False)
                else:
                    embed.add_field(name=f"{_id}. {eventname}", value='Tech Event', inline=False)
            await ctx.send(embed=embed)
        else:
            results = collection1.find_one({'_id': int(event_num)})
            _id = results['_id']
            eventname = results['title']
            invalid = ['_id', 'title', 'description', 'time', 'added_by', 'subevents']
            try:
                description = results['description']
            except:
                description = None
            if description:
                embed = discord.Embed(title=eventname, description=description, colour=random.choice(embedColors))
            else:
                embed = discord.Embed(title=eventname, colour=random.choice(embedColors))
            for key in results:
                if key not in invalid:
                    embed.add_field(name=key.title(), value=results[key], inline=False)
            embed.set_footer(text=f'Requested by {ctx.author}, To register use !startreg <event_num>', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(aliases=['subevent'])
    async def subevents(self, ctx, eventnum=None):
        if eventnum is None:
            results = collection1.find()
            embed = discord.Embed(title=f'CodeTech Events 2021-22',
                                  description="To view sub-events of the below listed events use !subevents <event_num>",
                                  colour=random.choice(embedColors))
            embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
            for result in results:
                _id = result['_id']
                eventname = result['title']
                try:
                    description = result['description']
                except:
                    description = None
                if description:
                    embed.add_field(name=f"{_id}. {eventname}", value=description, inline=False)
                else:
                    embed.add_field(name=f"{_id}. {eventname}", value='Tech Event', inline=False)
            await ctx.send(embed=embed)
        else:
            results = collection1.find_one({'_id': int(eventnum)})
            _id = results['_id']
            subevents = results['subevents']
            embed = discord.Embed(title=f"Subevents: {results['title']}", description="Below is the list of valid sub-events for this event.", colour=random.choice(embedColors))
            embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
            for subevent in subevents:
                embed.add_field(name=subevent.title(), value="-")
            await ctx.send(embed=embed)

    @commands.command()
    @has_permissions(kick_members=True)
    async def editevent(self, ctx, event_num, field, *, data):
        results = collection1.find_one({'_id': int(event_num)})
        updated = {'$set': {f'{field}': data}}
        collection1.update_one(results, updated)
        embed = discord.Embed(title=f"Event Modified: {results['title']}",
                              description=f"{field.title()}: {data}", colour=random.choice(embedColors))
        await ctx.send(embed=embed)

    @commands.command(aliases=['addsubev'])
    @has_permissions(kick_members=True)
    async def addsubevent(self, ctx, event_num, *, data):
        results = collection1.find_one({'_id': int(event_num)})
        subevents = results['subevents']
        subevents[data.lower()] = ''
        updated = {'$set': {'subevents': subevents}}
        collection1.update_one({'_id': int(event_num)}, updated)
        embed = discord.Embed(title=f"Event Modified: {results['title']}",
                              description=f"New Sub-Event: {data}", colour=random.choice(embedColors))
        await ctx.send(embed=embed)

    @commands.command(aliases=['startreg'])
    async def startregistration(self, ctx, event_num):
        guild = ctx.guild
        member = ctx.author
        admin_role = get(guild.roles, name="CT#Admin")
        gen_role = get(guild.roles, name="Verified")
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            gen_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True),
            admin_role: discord.PermissionOverwrite(read_messages=True)
        }

        channel_name = f'Reg{member}-event{event_num}'
        channel = await guild.create_text_channel(channel_name, overwrites=overwrites)
        perms = channel.overwrites_for(member)
        await channel.set_permissions(member, read_messages=not perms.read_messages)
        embed = discord.Embed(title=f"Head over to {channel_name}")

        await ctx.send(embed=embed)
        await channel.send(member.mention)

        results = collection1.find_one({'_id': int(event_num)})
        _id = results['_id']
        eventname = results['title']
        subevents = results['subevents']
        invalid = ['_id', 'title', 'description', 'time', 'added_by', 'subevents']

        try:
            description = results['description']
        except:
            description = None

        if description:
            embed = discord.Embed(title=eventname, description=description, colour=random.choice(embedColors))
        else:
            embed = discord.Embed(title=eventname, colour=random.choice(embedColors))

        for key in results:
            if key not in invalid:
                embed.add_field(name=key.title(), value=results[key], inline=True)

        embed.set_footer(text=f'For further assistance contact the online administrators.')
        await channel.send(embed=embed)

        embed = discord.Embed(title=f"Subevents: {results['title']}",
                              description="Below is the list of valid sub-events for this event.",
                              colour=random.choice(embedColors))
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
        for subevent in subevents:
            embed.add_field(name=subevent.title(), value="-")
        await channel.send(embed=embed)

        embed = discord.Embed(title=f"Registration: {eventname}",
                              description="To register for the above event use !register <field_name> <your_data>. Field names are mentioned below.",
                              colour=random.choice(embedColors))
        embed.add_field(name="fullname", value="Entries with absurd names will not be entertained.", inline=True)
        embed.add_field(name="cls-sec", value="Mention in numerical values, section is required for BVN students only.",
                        inline=True)
        embed.add_field(name="email", value="We'll use this address and discord to reach out to you.", inline=True)
        embed.add_field(name="subevent", value="To see sub-events use !subevents <main_event_num>. Don't use if there are no sub-events", inline=True)
        embed.add_field(name="school", value="For individual registrations enter individual", inline=True)
        embed.add_field(name="club", value="Don't use if none", inline=True)
        embed.set_footer(text=f'For further assistance contact the online administrators.')
        await channel.send(embed=embed)

        collection3.insert_one({'discord_name': ctx.author.name,'discord_id':ctx.author.discriminator, 'channel_id': channel.id,'member_id':ctx.author.id, 'event': int(event_num)})
        collection2.insert_one(
            {'_id': channel.id, 'discord_name': ctx.author.name,'discord_id':ctx.author.discriminator, 'event_name': eventname, 'event_id': int(event_num), 'time': datetime.datetime.now()})

        await channel.send(
"""
```
SAMPLE REGISTRATION
!register fullname Pancham Agarwal
!register cls-sec 12-C
!register email ***REMOVED***
!register subevent quiz
!register school Birla Vidya Niketan
!register club CodeTech BVN
!closereg

EDIT COMMAND:
!editreg <field name> <data>```"""
        )

    @commands.command()
    async def register(self, ctx, field, *, data):
        result = collection3.find_one({'discord_id': ctx.author.discriminator, 'channel_id': ctx.channel.id})
        eventnum = result['event']
        result = collection1.find_one({'_id': int(eventnum)})
        eventname = result['title']

        if field.lower() == 'subevent':
            event_data = collection1.find_one({'_id': int(eventnum)})
            subevents = event_data['subevents']
            if data.lower() in subevents:
                result = collection2.find_one({'_id':int(ctx.channel.id)})
                update = {'$set': {field: data.lower()}}
                collection2.update_one(result, update)
                embed = discord.Embed(title=f"{eventname}: {ctx.author}",
                                      description=f"{field.title()}: {data}", colour=random.choice(embedColors))
                embed.set_footer(text="To edit use !editreg <field_name> <your_data>. To submit use !closereg")
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title=f"Sub-events: {eventname}",
                                      description=f"Below is the list of valid sub-events for this event.", colour=random.choice(embedColors))
                for subevent in subevents:
                    embed.add_field(name=subevent.title(), value="-", inline=False)
                embed.set_footer(text="To see sub-events use !subevents <main_event_num>. Don't use if there are no sub-events")
                await ctx.send(embed=embed)
        else:
            result = collection2.find_one({'_id':int(ctx.channel.id)})
            update = {'$set': {field: data}}
            collection2.update_one(result, update)
            embed = discord.Embed(title=f"{eventname}: {ctx.author}",
                                  description=f"{field.title()}: {data}", colour=random.choice(embedColors))
            embed.set_footer(text="To edit use !editreg <field_name> <your_data>. To submit use !closereg")
            await ctx.send(embed=embed)

    @commands.command(aliases=['editreg'])
    async def editregistration(self, ctx, field, *, data):
        result = collection3.find_one({'discord_id': ctx.author.discriminator, 'channel_id': ctx.channel.id})
        eventnum = result['event']
        result = collection1.find_one({'_id': int(eventnum)})
        eventname = result['title']
        result = collection2.find_one({'_id':int(ctx.channel.id)})
        update = {'$set': {field: data}}
        collection2.update_one(result, update)
        embed = discord.Embed(title=f"{eventname}: {ctx.author}",
                              description=f"{field.title()} Modified: {data}", colour=random.choice(embedColors))
        embed.set_footer(text="To edit use !editreg <field_name> <your_data>. To submit use !closereg")
        await ctx.send(embed=embed)

    @commands.command(aliases=['closereg'])
    async def closeregistration(self,ctx, member:discord.Member=None):
        if member is None:
            result = collection3.find_one({'discord_id':ctx.author.discriminator,'channel_id': ctx.channel.id})
            eventnum = result['event']
            collection3.delete_one(result)
            embed = discord.Embed(title=f"Registration Successful: {ctx.author}",
                                  description=f"Thankyou for registering. We are looking forward to see you!", colour=random.choice(embedColors))
            result = collection2.find_one({'_id':int(ctx.channel.id)})
            invalid = ['_id', 'event_id','time', 'discord_name', 'discord_id','member_id']

            embed.add_field(name="ID", value=result['_id'])
            for key in result:
                if key not in invalid:
                    embed.add_field(name=key.title(), value=result[key], inline=False)

            embed.set_footer(text=f'This entry cannot be edited. To delete use !deleteregistration <registration_id> in any channel. For further assistance contact the online administrators.')
            await ctx.author.send(embed=embed)
            await ctx.channel.delete()
        else:
            result = collection3.find_one({'discord_id': member.discriminator, 'channel_id': ctx.channel.id})
            collection3.delete_one(result)
            embed = discord.Embed(title=f"Registration Successful: {member}",
                                  description=f"Thankyou for registering. We are looking forward to see you!",
                                  colour=random.choice(embedColors))
            result = collection2.find_one({'_id':int(ctx.channel.id)})
            invalid = ['_id', 'event_id', 'time', 'discord_name', 'discord_id', 'member_id']

            embed.add_field(name="ID", value=result['_id'])
            for key in result:
                if key not in invalid:
                    embed.add_field(name=key.title(), value=result[key], inline=False)

            embed.set_footer(
                text=f'This entry cannot be edited. To delete use !deleteregistration <registration_id> in any channel. For further assistance contact the online administrators.')
            await member.send(embed=embed)
            await ctx.channel.delete()

    @commands.command(aliases=['delreg'])
    async def deleteregistration(self,ctx,registration_id):
        result = collection2.find_one({'_id':int(registration_id)})
        event = result['event_name']
        name = result['discord_name']
        discord_id = result['discord_id']
        collection2.delete_one({'_id':int(registration_id)})
        embed = discord.Embed(title=f"Registration deleted: {name}#{discord_id}", description=f"Event: {event.title()}")
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Startup(bot))
