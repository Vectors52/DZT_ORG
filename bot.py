import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"تم تشغيل البوت: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong 🏓")

from discord.ui import Button, View

@bot.command()
async def servermap(ctx):
    

    embed = discord.Embed(
        title="خريطة السيرفر",
        description="مرحباً بك في قناة خريطة السيرفر 📌\nاختر القسم الذي تريد الذهاب إليه من الأزرار بالأسفل.",
        color=0xff0000
    )

    embed.set_image(url="https://i.imgur.com/8nQ5KqX.png") 
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/25/25694.png")

    # إنشاء الأزرار
    rules_button = Button(label="القوانين", emoji="📕", style=discord.ButtonStyle.primary)
    rank_button = Button(label="الرتب", emoji="⭐", style=discord.ButtonStyle.success)
    support_button = Button(label="الدعم", emoji="🎧", style=discord.ButtonStyle.secondary)

    async def rules_callback(interaction):
        await interaction.response.send_message("  <#945476859511046214>    ", ephemeral=True)

    async def rank_callback(interaction):
        await interaction.response.send_message("اذهب إلى قناة الرتب 👉 #ranks", ephemeral=True)

    async def support_callback(interaction):
        await interaction.response.send_message("اذهب إلى الدعم 👉 #support", ephemeral=True)

    rules_button.callback = rules_callback
    rank_button.callback = rank_callback
    support_button.callback = support_callback

    view = View()
    view.add_item(rules_button)
    view.add_item(rank_button)
    view.add_item(support_button)

    await ctx.send(embed=embed, view=view)

import os
bot.run(os.getenv("TOKEN"))
