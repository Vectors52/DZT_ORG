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

    # ================= CALLBACKS =================
    async def rules_callback(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        map_embed = discord.Embed(
            title="Map / خريطة السيرفر",
            description="""/activ** ... (كل محتوى الخريطة هنا كما في كودك)""",
            color=0xff0000
        )

        await interaction.followup.send(embed=map_embed, ephemeral=True)

    async def rank_callback(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        rank_embed = discord.Embed(
            title="⭐ نظام الرتب",
            description=""" ... (محتوى الرتب كامل كما في كودك)""",
            color=0xff0000
        )
        await interaction.followup.send(embed=rank_embed, ephemeral=True)

    async def support_callback(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        support_embed = discord.Embed(
            title="💎 نظام البوست",
            description=""" ... (محتوى الدعم كامل كما في كودك)""",
            color=0xff0000
        )

        await interaction.followup.send(embed=support_embed, ephemeral=True)

    rules_button.callback = rules_callback
    rank_button.callback = rank_callback
    support_button.callback = support_callback

    view = View(timeout=None)
    view.add_item(rules_button)
    view.add_item(rank_button)
    view.add_item(support_button)

    await ctx.send(embed=embed, view=view)


# ================= أمر جديد: لوحة القوانين =================
@bot.command()
async def rulespanel(ctx):
    embed = discord.Embed(
        title="📜 القوانين والسلوكيات",
        description="نرجو من جميع الأعضاء قراءة القوانين والسلوكيات عبر الأزرار بالأسفل 👇",
        color=0xff0000
    )
    embed.set_image(url="https://i.imgur.com/fc718ebc-8dca-4709-bbc6-d31dc9870319.png")  # الصورة المرفقة
    embed.set_footer(text="© DEREK DZT BOT")

    # ================= BUTTONS =================
    rules_button = Button(label="قوانين السيرفر", style=discord.ButtonStyle.danger, emoji="📕")
    etiquette_button = Button(label="السلوكيات", style=discord.ButtonStyle.primary, emoji="⭐")
    events_button = Button(label="الفعاليات والتحديثات", style=discord.ButtonStyle.success, emoji="🎉")
    ramadan_button = Button(label="قوانين رمضانية", style=discord.ButtonStyle.secondary, emoji="🌙")

    # ================= CALLBACKS =================
    async def rules_callback(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        rules_embed = discord.Embed(
            title="📜 قوانين السيرفر",
            description="""
- احترم جميع الأعضاء  
- عدم السب أو التجريح  
- الالتزام بالقنوات المناسبة  
- أي مخالفة ستؤدي إلى التحذير أو الباند
""",
            color=0xff0000
        )
        await interaction.followup.send(embed=rules_embed, ephemeral=True)

    async def etiquette_callback(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        etiquette_embed = discord.Embed(
            title="⭐ السلوكيات",
            description="""
- كن لطيفًا مع الجميع  
- لا تزعج الأعضاء في الدردشة  
- ساعد من يحتاج المساعدة
""",
            color=0x00ff00
        )
        await interaction.followup.send(embed=etiquette_embed, ephemeral=True)

    async def events_callback(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        events_embed = discord.Embed(
            title="🎉 الفعاليات والتحديثات",
            description="""
- متابعة الأخبار في قناة #News  
- المشاركة في المسابقات الأسبوعية  
- الاطلاع على الأحداث الجديدة باستمرار
""",
            color=0x0000ff
        )
        await interaction.followup.send(embed=events_embed, ephemeral=True)

    async def ramadan_callback(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        ramadan_embed = discord.Embed(
            title="🌙 القوانين الرمضانية",
            description="""
- التفاعل مع الآخرين بالاحترام  
- الامتناع عن المشاركات المزعجة أثناء الصيام  
- الالتزام بالقنوات الخاصة برمضان
""",
            color=0xffff00
        )
        await interaction.followup.send(embed=ramadan_embed, ephemeral=True)

    rules_button.callback = rules_callback
    etiquette_button.callback = etiquette_callback
    events_button.callback = events_callback
    ramadan_button.callback = ramadan_callback

    view = View(timeout=None)
    view.add_item(rules_button)
    view.add_item(etiquette_button)
    view.add_item(events_button)
    view.add_item(ramadan_button)

    await ctx.send(embed=embed, view=view)


# شغّل البوت، ضع التوكن هنا أو استخدم env
bot.run(os.getenv("TOKEN") or "ضع_التوكن_هنا")