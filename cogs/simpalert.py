from discord.ext import commands
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw
import discord


class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def simpalert(self, ctx, simp: discord.Member = None):
        if simp is None:
            simp = ctx.author
        template = Image.open('codetechbot/images/simp_template.png')
        asset = simp.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        simp_pfp = Image.open(data)
        simp_pfp = simp_pfp.resize((184, 184))
        template.paste(simp_pfp, (36, 89))
        font = ImageFont.truetype('codetechbot/fonts/college.ttf', 40)
        draw = ImageDraw.Draw(template)
        text = simp.display_name
        draw.text((42, 283), text, (255, 255, 255), font=font)
        template.save('codetechbot/images/simp_user_profile.png')
        await ctx.send(file=discord.File('codetechbot/images/simp_user_profile.png'))


def setup(bot):
    bot.add_cog(Startup(bot))