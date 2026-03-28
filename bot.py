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
    support_button = Button(label="الداعمين", emoji="🎧", style=discord.ButtonStyle.secondary)

    async def rules_callback(interaction):
        await interaction.response.send_message("""
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

...
╰━━─☾ --------- ☽─━━╯"""
, ephemeral=True)

    async def rank_callback(interaction):
        await interaction.response.send_message("""الـرتـب
@.⭒☆ TRAINER ┃ مـتـدرب ☆⭒.
الخواص : شكل بس,
الشروط : 5 لفل كتابي,
@.⭒☆ SOLDIER ┃ الـجـنـدي ☆⭒.
الخواص : رياكشن,
الشروط : 10 لفل كتابي,
@.⭒☆ WARRIOR ┃ مـحـارب ☆⭒.
الخواص : سوي ستيكرات من سيرفرات اخرى,
الشروط :  15 لفل كتابي,
@.⭒☆ KNIGHT ┃ الـفـارس ☆⭒.
الخواص : 1- تقدر تسوي soundbord,
2- تقدر تسوي soundbord من سيرفرات اخرى
الشروط :  25 لفل كتابي,
@.⭒☆ COLONEL ┃ الـعـقـيـد ☆⭒.
الخواص : تقدر ترسل صور بشات العام,
الشروط :  35 لفل كتابي,
@.⭒☆ SIR ┃ الـسـيـر ☆⭒.
الخواص :  تقدر تسوي gif,
الشروط : 45 لفل كتابي,
@.⭒☆ COLONEL ┃ الـعـقـيـد ☆⭒.
الخواص :  جميع ما سبق,
الشروط : 1- 60 لفل كتابي,
2- 5 لفل صوتي
@.⭒☆ KING ┃ الـمـلـك ☆⭒.
الخواص : جميع ما سبق,
الشروط  : 1-  75 لفل كتابي,
2- 10 صوتي
@𝐌𝐫.
الخواص : جميع ما سبق,
الشروط,
100 لفل كتابي,
17 لفل صوتي,
@𝐓𝐨𝐩 𝐚𝐜𝐭𝐢𝐯𝐞
تاخذ توب اسبوعي في تفاعل,

@𝐃𝐙𝐓 丶𝐒𝐭𝐫𝐞𝐚𝐦𝐞𝐫
الشرط : تكون ستريمر,
الخواص : جميع خواص رتب تفاعليه في رتبه واحده,

@𝐃𝐙𝐓 丶𝐘𝐨𝐮𝐭𝐮𝐛𝐞𝐫
الشروط :  1 - يكون معك 4 الاف مشترك,
2 - 8 الاف مشاهده عل مقطع
3 - مايهم اذا محتواك مش روبلكس او لا بس ممنوع تنشر هاك

@𝐃𝐙𝐓 丶 𝐃𝐞𝐬𝐢𝐠𝐧𝐞𝐫
الشرط :  تكون مصمم وتقدم خدمه لسيرفر بتصميم شي معين,
او يتم اعطائك ياها في حين تصاميمك
@𝐃𝐙𝐓 丶 𝐀𝐯𝐚𝐭𝐚𝐫𝐬
الشرط : رسام افاتار او مصمم صور,
@𝐃𝐙𝐓 丶𝐅𝐫𝐢𝐞𝐧𝐝

الشرط :  تكون صديق ديركس ويعطيك ياها هوا بنفسه,

@𝐒𝐩𝐞𝐜𝐢𝐚𝐥 𝐅𝐫𝐢𝐞𝐧𝐝
الشرط :  تكون من اعز الاصدقاء لديركس,

@Old staff
الشرط :  اداره صغرى مستقيله وتكون high admin,
@𝐑𝐞𝐭𝐢𝐫𝐞𝐝 𝐇𝐢𝐠𝐡 𝐆𝐨𝐯𝐞𝐫𝐧𝐨𝐫
الشرط :  اداره عليا مستقيله,

@𝐚𝐩𝐩𝐫𝐨𝐯𝐞𝐝 𝐥𝐚𝐝𝐲
هام : رتبه يتم الحصول عليها بعد توثيقك وتقدرين تشوفين شات البنات,
""", ephemeral=True)

    async def support_callback(interaction):
        await interaction.response.send_message("""نـظـام الـبـوسـت
• البوست :1000018612: = 120 :rob:

• دبل بوست :1000018612: = 300 :rob:

• ملاحظه : ❗❗❗

• تشيل البوست باند مدى الحياه خذ حذرك

ولاتشيل البوست :E24A_Red:

• لاستلام :rob: افتح تكت

• في حال مرت 24 ساعه بدون فتح تكت لن يتم تسليمك :rob:...""", ephemeral=True)

    rules_button.callback = rules_callback
    rank_button.callback = rank_callback
    support_button.callback = support_callback

    view = View()
    view.add_item(rules_button)
    view.add_item(rank_button)
    view.add_item(support_button)

    await ctx.send(embed=embed, view=view)

bot.run(os.getenv("TOKEN"))