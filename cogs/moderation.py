from discord.ext import commands
from discord.ext.commands import has_permissions
import discord
import asyncio

muted_members = []


class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, time='null', *, reason='No reason'):
        logchannel = self.bot.get_channel(***REMOVED***)
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
            muted_members.append(member)
            embed = discord.Embed(title=f"{member.name} has been muted for {time} by {ctx.author.name}",
                                  description=reason,
                                  color=discord.Colour.blue())
            await ctx.send(embed=embed)
            await logchannel.send(f"{member} was muted for {time} by {ctx.author}. [{reason}]")

            await asyncio.sleep(tempmute)
            await member.remove_roles(muted_role)
            muted_members.remove(member)
            await ctx.send(f'{member.mention} You have been unmuted.')

    # Unmutes the mentioned user (Mod only)
    @commands.command()
    @has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member):
        logchannel = self.bot.get_channel(***REMOVED***)
        muterole = ctx.guild.get_role(***REMOVED***)
        await member.remove_roles(muterole)
        await ctx.send(f"{member.mention} was unmuted by {ctx.author.mention}")
        await logchannel.send(f"{member} was unmuted by {ctx.author}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        muted_role = discord.utils.get(guild.roles, name="Muted")
        if member in muted_members:
            await member.add_roles(muted_role)

    # Kicks the mentioned user (Mod only)
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason='No reason'):
        logchannel = self.bot.get_channel(***REMOVED***)
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} was kicked by {ctx.author.mention}. [{reason}]")
        await logchannel.send(f"{member.mention} was kicked by {ctx.author.mention}. [{reason}]")

    # Bans the mentioned user (Mod only)
    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason='No reason'):
        logchannel = self.bot.get_channel(***REMOVED***)
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} was banned by {ctx.author.mention}. [{reason}]")
        await logchannel.send(f"{member.mention} was banned by {ctx.author.mention}. [{reason}]")


def setup(bot):
    bot.add_cog(Startup(bot))