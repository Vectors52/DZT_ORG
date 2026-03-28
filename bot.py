import discord
from discord.ext import commands
from discord.ui import Button, View
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"تم تشغيل البوت: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong 🏓")

# أمر خريطة السيرفر
@bot.command()
async def servermap(ctx):

    embed = discord.Embed(
        title="خريطة السيرفر",
        description="""نرجوا من كل الأعضاء قراءة خريطة السيرفر وخاصة الجدد سواء الرومات أو الرتب
لمعرفة كل ما يخص السيرفر ونيل أفضل تجربة فيه.""",
        color=0xff0000
    )

    embed.set_image(url="https://i.imgur.com/8nQ5KqX.png")
    embed.set_thumbnail(url="https://i.imgur.com/F5La6FP.png")

    # الأزرار
    rules_button = Button(label="القوانين", emoji="📕", style=discord.ButtonStyle.primary)
    rank_button = Button(label="الرتب", emoji="⭐", style=discord.ButtonStyle.success)
    support_button = Button(label="الدعم", emoji="🎧", style=discord.ButtonStyle.secondary)

    async def rules_callback(interaction):
        await interaction.response.send_message("   👉 <#945476859511046214>", ephemeral=True)

    async def rank_callback(interaction):
        await interaction.response.send_message("اذهب إلى قناة الرتب 👉 <#ID_HERE>", ephemeral=True)

    async def support_callback(interaction):
        await interaction.response.send_message("اذهب إلى الدعم 👉 <#ID_HERE>", ephemeral=True)

    rules_button.callback = rules_callback
    rank_button.callback = rank_callback
    support_button.callback = support_callback

    view = View()
    view.add_item(rules_button)
    view.add_item(rank_button)
    view.add_item(support_button)

    await ctx.send(embed=embed, view=view)

bot.run(os.getenv("TOKEN"))