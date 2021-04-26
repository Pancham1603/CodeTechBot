from discord.ext import commands
import discord

muted_mod = []


class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def modmute(self, ctx, member: discord.Member = None):
        valid = ['ids here in int format']
        mod_role = discord.utils.get(ctx.guild.roles, name='CT#Admin')
        if ctx.author.id in valid:
            if member == None:
                await ctx.send("Please mention a moderator!")
            elif mod_role not in member.roles:
                await ctx.send(f"The mentioned user is not a moderator.")
            else:
                muted_mod.append(member.id)
                logchannel = self.bot.get_channel()
                embed = discord.Embed(title=f'{ctx.author.display_name} muted {member.display_name}',
                                      color=discord.Color.red())
                await ctx.send(embed=embed)
                await logchannel.send(embed=embed)
        else:
            await ctx.send("This command can only be used by roles higher than 'CT#Admin'.")

    @commands.command()
    async def modunmute(self, ctx, member: discord.Member = None):
        valid = [, , ]
        mod_role = discord.utils.get(ctx.guild.roles, name='CT#Admin')
        if ctx.author.id in valid:
            if member == None:
                await ctx.send("Please mention a moderator!")
            elif mod_role not in member.roles:
                await ctx.send(f"The mentioned user is not a moderator.")
            elif member.id not in muted_mod:
                await ctx.send("The mentioned user is not muted.")
            else:
                muted_mod.remove(member.id)
                logchannel = self.bot.get_channel()
                embed = discord.Embed(title=f'{ctx.author.display_name} ummuted {member.display_name}',
                                      color=discord.Color.green())
                await ctx.send(embed=embed)
                await logchannel.send(embed=embed)
        else:
            await ctx.send("This command can only be used by roles higher than 'CT#Admin'.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in muted_mod:
            await message.delete()


def setup(bot):
    bot.add_cog(Startup(bot))
