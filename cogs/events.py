from discord.ext import commands
from pymongo import MongoClient
import discord
import datetime
import random

client = MongoClient(
        "***REMOVED***")
db = ***REMOVED***
collection1 = ***REMOVED***
collection2 = ***REMOVED***
collection3 = ***REMOVED***

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
    async def addevent(self, ctx, *, eventname):
        try:
            results = collection1.find()
            for result in results:
                _id = result['_id']
            _id += 1
        except:
            _id = 1
        collection1.insert_one(
            {'_id': _id, 'title': eventname, 'added_by': f'{ctx.author.name}#{ctx.author.discriminator}',
             'time': datetime.datetime.now()})
        embed = discord.Embed(title=f'New Event: {eventname}', colour=random.choice(embedColors))
        embed.set_footer(text=f'Added by {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def events(self, ctx, event_num=None):
        if event_num is None:
            results = collection1.find()
            embed = discord.Embed(title=f'CodeTech Events 2021-22',
                                  description="For info on any of the below listed events use !events <event_num>",
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
            invalid = ['_id', 'title', 'description', 'time', 'added_by']
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
            embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def editevent(self, ctx, event_num, field, *, data):
        results = collection1.find_one({'_id': int(event_num)})
        updated = {'$set': {f'{field}': data}}
        collection1.update_one(results, updated)
        embed = discord.Embed(title=f"Event Modified: {results['title']}",
                              description=f"{field.title()}: {data.capitalize()}", colour=random.choice(embedColors))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Startup(bot))