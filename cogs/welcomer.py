from discord.ext import commands
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw
import discord

muted_members = []

class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        doorchannel = self.bot.get_channel()
        verifychannel = self.bot.get_channel()
        muted_role = discord.utils.get(guild.roles, name="Muted")

        if member in muted_members:
            await member.add_roles(muted_role)

        template = Image.open('images/discord-invite-bg-template.jpeg')
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        member_pfp = Image.open(data)
        member_pfp = member_pfp.resize((519, 519))
        template.paste(member_pfp, (119, 145))
        font = ImageFont.truetype('fonts/college.ttf', 100)
        draw = ImageDraw.Draw(template)
        text = member.display_name
        draw.text((177, 727), text, (255, 255, 255), font=font)
        template.save('images/discord-invite-bg-user.jpeg')
        await doorchannel.send(
            f"{member.mention} Head over to {verifychannel.mention} to access the server.")
        await doorchannel.send(file=discord.File('images/discord-invite-bg-user.jpeg'))

def setup(bot):
    bot.add_cog(Startup(bot))