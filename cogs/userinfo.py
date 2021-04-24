from discord.ext import commands
import discord

class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Displays full info of the requested user
    @commands.command()
    async def user(self, ctx, member: discord.Member = None):
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

def setup(bot):
    bot.add_cog(Startup(bot))