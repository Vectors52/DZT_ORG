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

    embed.set_image(url="https://i.imgur.com/F5La6FP.png")
    embed.set_thumbnail(url="https://i.imgur.com/F5La6FP.png")

    # الأزرار
    rules_button = Button(label="الخريطه", emoji="📕", style=discord.ButtonStyle.primary)
    rank_button = Button(label="الرتب", emoji="⭐", style=discord.ButtonStyle.success)
    support_button = Button(label="الدعم", emoji="🎧", style=discord.ButtonStyle.secondary)

    async def rules_callback(interaction):
        await interaction.response.send_message("  الرومات


╭━━─☾ ---------- ☽─━━╮

الـرومــات :DZT~1:


:1DZT:   ⁠#1346826604982177865


أهم ما يجب إتباعه بالسيرفر لأحسن تجربة


:2DZT:  ⁠#1346826604982177866


جديد و تحديثات السيرفر


:3DZT:  ⁠#1475485136144306336


رتب إشعارات ما يهمك من الألعاب و المجالات


:4DZT:  ⁠#1474926897627660388


الدعم الفني لطرح المشاكل, الشكاوي ، الإستفسارات و غيرها


:5DZT: #1475567438346326106


إمكانية التوثيق بالنسبة للبنات


:6DZT:   ⁠#1360388162559672558


روم يظهر داعمين السيرفر ببوست و المميزات الحصرية لهم



━━─☾ ------------ ☽─━━


:1DZT:  ⁠#1359468127255269468


مكان الدردشة و الترفيه


:2DZT:   ⁠unknown


روم خاص بتبادلات كل بلوكس فروت .


:3DZT:   ⁠unknown


تقديم و إستقبال أذكار و مقاطع مفيدة دينية


:4DZT:   ⁠#1359995210989305947


إستعمال أوامر البوت


:5DZT:   ⁠#1477032038442729512



معرفة مستواك التفاعلي في السيرفر


:6DZT:  ⁠#1360004700887453966


إنشاء روم صوتي مؤقت خاص بك ، و للتحكم به يمكنك التوجه إلى

⁠#1360006848123637790


:7DZT:  ⁠#1469018876401422346


يمكنكم تبادل اغلب الاشياء داخل الروم مثل روبلوكس ، باونتي الخخ..


:8DZT:  ⁠#1474926897627660388


يمكنكم طلب وسيط لضمان تبادلاتكم من خلاله .


━━─☾ ------------ ☽─━━


:1DZT: ⁠unknown


جديد بلوكس فروت من أخبار و متجر فواكهها


╰━━─☾ --------- ☽─━━╯"
, ephemeral=True)

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