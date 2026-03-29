import discord
from discord.ext import commands
from discord.ui import Button, View
import os

intents = discord.Intents.all()
intents.message_content = True
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
        description="نرجو من جميع الأعضاء قراءة خريطة السيرفر عبر الأزرار بالأسفل 👇",
        color=0xff0000
    )

    embed.set_image(url="https://i.imgur.com/F5La6FP.png")
    embed.set_thumbnail(url="https://i.imgur.com/rO3pb7D.gif")
    embed.set_footer(text="© DEREK DZT BOT")

    # ================= BUTTONS =================

    rules_button = Button(label="الخريطة", emoji="📕", style=discord.ButtonStyle.primary)
    rank_button = Button(label="الرتب", emoji="⭐", style=discord.ButtonStyle.success)
    support_button = Button(label="الداعمين", emoji="🎧", style=discord.ButtonStyle.secondary)

    # ================= MAP BUTTON =================
    async def rules_callback(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        map_embed = discord.Embed(
            title="Map / خريطة السيرفر",
            description="""/activ**

╭━━─☾ ---------- ☽─━━╮

__ الـرومــات <a:DZT:1352711674108575825>  __

- <:1DZT:1475478821133221919>   <#1346826604982177865>  
- أهم ما يجب إتباعه بالسيرفر لأحسن تجربة 

- <:2DZT:1475478833678389248>  <#1346826604982177866> 
- جديد و تحديثات السيرفر 

- <:3DZT:1475478844302426296>  <#1475485136144306336> 
- رتب إشعارات ما يهمك من الألعاب و المجالات 

- <:4DZT:1475478856180961373>  <#1474926897627660388> 
- الدعم الفني لطرح المشاكل, الشكاوي ، الإستفسارات و غيرها

- <:5DZT:1475478869048955025> <#1475567438346326106> 
- إمكانية التوثيق بالنسبة للبنات 

- <:6DZT:1475478880801263698>   <#1360388162559672558> 
- روم يظهر داعمين السيرفر ببوست و المميزات الحصرية لهم 

━━─☾  ------------  ☽─━━

- <:1DZT:1475478821133221919>  <#1359468127255269468> 
- مكان الدردشة و الترفيه 

- <:2DZT:1475478833678389248>  
https://discord.com/channels/1346826603526619206/1486722908821913692 
- روم تبادلات بلوكس فروت

- <:3DZT:1475478844302426296>  
https://discord.com/channels/1346826603526619206/1487247807831212054 
- أذكار ومقاطع دينية

- <:4DZT:1475478856180961373>  <#1359995210989305947> 
- أوامر البوت

- <:5DZT:1475478869048955025>  <#1477032038442729512> 
- معرفة مستوى التفاعل

- <:6DZT:1475478880801263698>  
https://discord.com/channels/1346826603526619206/1360004700887453966

- إنشاء روم صوتي مؤقت  
https://discord.com/channels/1346826603526619206/1360006848123637790

- <:7DZT:1475478912971837450>  <#1469018876401422346> 
- روم التريد

- <:8DZT:1475478923151278120>  <#1474926897627660388> 
- طلب وسيط

━━─☾  ------------  ☽─━━

- أخبار بلوكس فروت  
https://discord.com/channels/1346826603526619206/1486724525415731250

╰━━─☾  ---------  ☽─━━╯

**e-dev-badge**""",
            color=0xff0000
        )

        await interaction.followup.send(embed=map_embed, ephemeral=True)

    # ================= RANK BUTTON =================
    async def rank_callback(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        rank_embed = discord.Embed(
            title="⭐ نظام الرتب",
            description="""
TRAINER — 5 لفل كتابي  
SOLDIER — 10 لفل كتابي  
WARRIOR — 15 لفل كتابي  
KNIGHT — 25 لفل كتابي  
COLONEL — 35 لفل كتابي  
SIR — 45 لفل كتابي  
KING — 75 لفل كتابي + 10 صوتي  
Mr — 100 لفل كتابي + 17 صوتي  

🎥 Streamer — للستريمر  
📺 Youtuber — 4k مشترك  
🎨 Designer — مصمم  
🖼 Avatars — رسام أفاتار  
💎 Special Friend — صديق خاص
""",
            color=0xff0000
        )
        await interaction.followup.send(embed=rank_embed, ephemeral=True)

    # ================= SUPPORT BUTTON =================
    async def support_callback(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        support_embed = discord.Embed(
            title="💎 نظام البوست",
            description="""
البوست = 120 روب  
الدبل بوست = 300 روب  

⚠️ إزالة البوست = باند دائم  
لاستلام الروب افتح تكت خلال 24 ساعة
""",
            color=0xff0000
        )

        await interaction.followup.send(embed=support_embed, ephemeral=True)

    # ================= ربط الأزرار بالوظائف =================
    rules_button.callback = rules_callback
    rank_button.callback = rank_callback
    support_button.callback = support_callback

    view = View(timeout=None)
    view.add_item(rules_button)
    view.add_item(rank_button)
    view.add_item(support_button)

    await ctx.send(embed=embed, view=view)

# شغّل البوت، ضع التوكن هنا أو استخدم env
bot.run(os.getenv("TOKEN") or "ضع_التوكن_هنا")