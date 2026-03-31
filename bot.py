import discord
from discord.ext import commands
from discord.ui import Button, View
import os

# الرتب المسموح لها باستخدام الأوامر
ALLOWED_ROLES = [1346826604067684400, 1473738359221387317]

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# فحص للتحقق من الرتبة
def has_allowed_role():
    async def predicate(ctx):
        user_role_ids = [role.id for role in ctx.author.roles]
        if any(role_id in ALLOWED_ROLES for role_id in user_role_ids):
            return True
        await ctx.send(embed=discord.Embed(
            description="❌ هذا الأمر مخصص للإدارة فقط.",
            color=0xff0000
        ))
        return False
    return commands.check(predicate)

@bot.event
async def on_ready():
    print(f"تم تشغيل البوت: {bot.user}")

@bot.command()
@has_allowed_role()
async def ping(ctx):
    await ctx.send("Pong 🏓")

# أمر خريطة السيرفر
@bot.command()
@has_allowed_role()
async def servermap(ctx):

    embed = discord.Embed(
        title="خريطة السيرفر",
        description="نرجوا من كل الأعضاء قراءة خريطة السيرفر و خاصة الجدد سواء الرومات أو الرتب لمعرفة كل ما يخص السيرفر و نيل أحسن تجربة فيه",
        color=0xff0000
    )

    embed.set_image(url="https://i.imgur.com/F5La6FP.png")
    embed.set_thumbnail(url="https://i.imgur.com/rO3pb7D.gif")
    embed.set_footer(text="© DEREK DZT BOT")

    # ================= BUTTONS =================

    rules_button = Button(label="الرومات", emoji="<:emoji_1:1488380213019807744>", style=discord.ButtonStyle.primary)
    rank_button = Button(label="الرتب", emoji="<:emoji_2:1488351778717307022>", style=discord.ButtonStyle.success)
    support_button = Button(label="الداعمين", emoji="<:emoji_3:1488380683285168178>", style=discord.ButtonStyle.secondary)

    # ================= CALLBACKS =================

    # تعديل محتوى خريطة السيرفر فقط
    async def rules_callback(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        map_embed = discord.Embed(
            title="╭━━─☾ ---------- ☽─━━╮",
            description="""
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

- <:2DZT:1475478833678389248>   https://discord.com/channels/1346826603526619206/1486722908821913692
- روم خاص بتبادلات كل بلوكس فروت .

- <:3DZT:1475478844302426296>  https://discord.com/channels/1346826603526619206/1487247807831212054
- تقديم و إستقبال أذكار و مقاطع مفيدة دينية 

- <:4DZT:1475478856180961373>   <#1359995210989305947>  
- إستعمال أوامر البوت 

- <:5DZT:1475478869048955025>   <#1477032038442729512>  
- معرفة مستواك التفاعلي في السيرفر 

- <:6DZT:1475478880801263698>  https://discord.com/channels/1346826603526619206/1360004700887453966
https://discord.com/channels/1346826603526619206/1360006848123637790
- إنشاء روم صوتي مؤقت خاص بك ، و للتحكم به يمكنك التوجه إلى

- <:7DZT:1475478912971837450>  <#1469018876401422346>  
- يمكنكم تبادل اغلب الاشياء داخل الروم مثل روبلوكس ، باونتي الخخ.. 

- <:8DZT:1475478923151278120>  <#1474926897627660388>  
- يمكنكم طلب وسيط لضمان تبادلاتكم من خلاله .

━━─☾  ------------  ☽─━━

- <:1DZT:1475478821133221919> https://discord.com/channels/1346826603526619206/1486724525415731250
- جديد بلوكس فروت من أخبار و متجر فواكهها 

╰━━─☾  ---------  ☽─━━╯
""",
            color=0xff0000
        )

        # صورة أمبيد الرومات - ضع رابط الصورة هنا
        map_embed.set_image(url="https://i.imgur.com/0CwvQp5.jpeg")

        await interaction.followup.send(embed=map_embed, ephemeral=True)

    async def rank_callback(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        rank_embed = discord.Embed(
            title="⭐ نظام الرتب",
            description="""
<:DZT_mention:1488351778717307022>  <@&1346826603837132884>

- <:emoji_295:1488374546229760011>  الخواص : شكل بس
- <:DZT_chatting:1488354777455792198>  الشروط : 5 لفل كتابي 

<:DZT_mention:1488351778717307022>  <@&1346826603837132885>

- <:emoji_295:1488374546229760011>   الخواص : رياكشن 
- <:DZT_chatting:1488354777455792198>  الشروط : 10 لفل كتابي 

<:DZT_mention:1488351778717307022> <@&1346826603837132886>

- <:emoji_295:1488374546229760011> الخواص : سوي ستيكرات من سيرفرات اخرى
- <:DZT_chatting:1488354777455792198>  الشروط :  15 لفل كتابي 

<:DZT_mention:1488351778717307022>  <@&1476305189542826126>

- <:emoji_295:1488374546229760011> الخواص :  تقدر تسوي soundbord من سيرفرات اخرى 
- <:DZT_chatting:1488354777455792198>  الشروط :  25 لفل كتابي

<:DZT_mention:1488351778717307022>  <@&1475952310961307738>

- <:emoji_295:1488374546229760011>   الخواص : تقدر ترسل صور بشات العام
- <:DZT_chatting:1488354777455792198>   الشروط :  35 لفل كتابي

<:DZT_mention:1488351778717307022><@&1346826603837132887>

- <:emoji_295:1488374546229760011>   الخواص :  تقدر تسوي gif
- <:DZT_chatting:1488354777455792198>   الشروط : 45 لفل كتابي

<:DZT_mention:1488351778717307022><@&1346826603837132888>

- <:emoji_295:1488374546229760011>   الخواص :  جميع ما سبق 
- <:DZT_chatting:1488354777455792198>   الشروط : 1- 60 لفل كتابي 
- <:DZT_Voice:1488364638113370112>      2- 5 لفل صوتي

<:DZT_mention:1488351778717307022><@&1348108598487552111>

- <:emoji_295:1488374546229760011>   الخواص : جميع ما سبق
- <:DZT_chatting:1488354777455792198>   الشروط  : 1-  75 لفل كتابي 
- <:DZT_Voice:1488364638113370112> 2- 10 صوتي 

<:DZT_mention:1488351778717307022><@&1348108717056327792>

- <:emoji_295:1488374546229760011>    الخواص : جميع ما سبق
- <:DZT_chatting:1488354777455792198>   الشروط 100 لفل كتابي 
- <:DZT_Voice:1488364638113370112> 17 لفل صوتي

<:DZT_mention:1488351778717307022><@&1488369923968208967>

- <:DZT_info:1487507997679943680>   تاخذ توب اسبوعي في تفاعل

<:DZT_mention:1488351778717307022><@&1346826603942117409> 

- <:DZT_info:1487507997679943680>   الشرط : تكون ستريمر 
- <:emoji_295:1488374546229760011>  الخواص : جميع خواص رتب تفاعليه في رتبه واحده

<:DZT_mention:1488351778717307022><@&1346826603942117410>

- <:DZT_info:1487507997679943680>    الشروط :  1 - يكون معك 4 الاف مشترك 
2 - 8 الاف مشاهده عل مقطع 
3 - مايهم اذا محتواك مش روبلكس او لا بس ممنوع تنشر هاك

<:DZT_mention:1488351778717307022><@&1346826604009230356> 

- <:DZT_info:1487507997679943680>    الشرط :  تكون مصمم وتقدم خدمه لسيرفر بتصميم شي معين 
او يتم اعطائك ياها في حين تصاميمك

<:DZT_mention:1488351778717307022><@&1346826603971350559>

- <:DZT_info:1487507997679943680>     الشرط : رسام افاتار او مصمم صور 

<:DZT_mention:1488351778717307022><@&1472769789486305332>

- <:DZT_info:1487507997679943680>     الشرط :  تكون صديق ديركس ويعطيك ياها هوا بنفسه 

<:DZT_mention:1488351778717307022><@&1472769891315486894>

- <:DZT_info:1487507997679943680>      الشرط :  تكون من اعز الاصدقاء لديركس 

<:DZT_mention:1488351778717307022><@&1474756964419371008>

- <:DZT_info:1487507997679943680>       الشرط :  اداره صغرى مستقيله وتكون high admin

<:DZT_mention:1488351778717307022><@&1474756899210526813>

- <:DZT_info:1487507997679943680>        الشرط :  اداره عليا مستقيله 

<:DZT_mention:1488351778717307022><@&1472674157060948133>

- <:DZT_info:1487507997679943680>         هام : رتبه يتم الحصول عليها بعد توثيقك وتقدرين تشوفين شات البنات
""",
            color=0xff0000
        )

        # صورة أمبيد الرتب - ضع رابط الصورة هنا
        rank_embed.set_image(url="https://i.imgur.com/aDkylcm.jpeg")

        await interaction.followup.send(embed=rank_embed, ephemeral=True)

    async def support_callback(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        support_embed = discord.Embed(
            title="💎 نظام البوست",
            description=""" ... **
╭━━─☾ ---------- ☽─━━╮

__ رتـب الـداعـمـيـن و شـروطـها <a:DZT:1352711674108575825> __ :


 هي رتب لها مميزات حصرية تحصل عليها عندما تدعم قروب ديريكس بروبلوكس بمبلغ معين لكل رتبة منهم.بحيث : <:emoji_297:1488378998307295303> 

━━─☾  ------------  ☽─━━


-  <:1DZT:1475478821133221919><:DZT_mention:1488351778717307022><@&1477637794947137619>


- تحصل عليها عند الدعم بقيمة 1000 <:Robux:1477629100133978143> 


- <:2DZT:1475478833678389248><:DZT_mention:1488351778717307022><@&1477633157107945603>


- تحصل عليها عند الدعم بقيمة  2500 <:Robux:1477629100133978143> 


- <:3DZT:1475478844302426296><:DZT_mention:1488351778717307022><@&1477637833593323621>


- تحصل عليها عند الدعم بقيمة 3750 <:Robux:1477629100133978143> 


- <:4DZT:1475478856180961373><:DZT_mention:1488351778717307022><@&1477637880368074934>


- تحصل عليها عند الدعم بقيمة 5000 <:Robux:1477629100133978143> 



━━─☾  ------------  ☽─━━

__ كـيـفـيـة الـحـصـول<a:DZT:1352711674108575825> __ : 


- تصوير دليل الدعم ومن ثم فتح تذكرة دعم فني


<:DZT_ticket:1488378327013265418> <#1474926897627660388> 

و من خلال التذكرة ستتواصل مع الطاقم الإداري  لأخذها 

━━─☾  ------------  ☽─━━

__ رابـط قـروب روبـلـكـس <a:DZT:1352711674108575825> __


- https://www.roblox.com/communities/14157269/RED-1-UGC#!/about


╰━━─☾  ---------  ☽─━━╯
**""",
            color=0xff0000
        )

        # صورة أمبيد الداعمين - ضع رابط الصورة هنا
        support_embed.set_image(url="https://i.imgur.com/CaisxC8.jpeg")

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
@has_allowed_role()
async def rulespanel(ctx):
    embed = discord.Embed(
        title="📜 القوانين والسلوكيات",
        description="نرجو من جميع الأعضاء قراءة القوانين والسلوكيات عبر الأزرار بالأسفل 👇",
        color=0xff0000
    )
    embed.set_image(url="https://i.imgur.com/fc718ebc-8dca-4709-bbc6-d31dc9870319.png")
    embed.set_footer(text="© DEREK DZT BOT")

    rules_button = Button(label="قوانين السيرفر", style=discord.ButtonStyle.danger, emoji="📕")
    etiquette_button = Button(label="السلوكيات", style=discord.ButtonStyle.primary, emoji="⭐")
    events_button = Button(label="الفعاليات والتحديثات", style=discord.ButtonStyle.success, emoji="🎉")
    ramadan_button = Button(label="قوانين رمضانية", style=discord.ButtonStyle.secondary, emoji="🌙")

    async def rules_callback(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        rules_embed = discord.Embed(
            title="📜 قوانين السيرفر",
            description="- احترم جميع الأعضاء\n- عدم السب أو التجريح\n- الالتزام بالقنوات المناسبة\n- أي مخالفة ستؤدي إلى التحذير أو الباند",
            color=0xff0000
        )

        rules_embed.set_image(url="ضع_رابط_صورة_قوانين_السيرفر_هنا")

        await interaction.followup.send(embed=rules_embed, ephemeral=True)

    async def etiquette_callback(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        etiquette_embed = discord.Embed(
            title="⭐ السلوكيات",
            description="- كن لطيفًا مع الجميع\n- لا تزعج الأعضاء في الدردشة\n- ساعد من يحتاج المساعدة",
            color=0x00ff00
        )

        etiquette_embed.set_image(url="ضع_رابط_صورة_السلوكيات_هنا")

        await interaction.followup.send(embed=etiquette_embed, ephemeral=True)

    async def events_callback(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        events_embed = discord.Embed(
            title="🎉 الفعاليات والتحديثات",
            description="- متابعة الأخبار في قناة #News\n- المشاركة في المسابقات الأسبوعية\n- الاطلاع على الأحداث الجديدة باستمرار",
            color=0x0000ff
        )

        events_embed.set_image(url="ضع_رابط_صورة_الفعاليات_هنا")

        await interaction.followup.send(embed=events_embed, ephemeral=True)

    async def ramadan_callback(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        ramadan_embed = discord.Embed(
            title="🌙 القوانين الرمضانية",
            description="- التفاعل مع الآخرين بالاحترام\n- الامتناع عن المشاركات المزعجة أثناء الصيام\n- الالتزام بالقنوات الخاصة برمضان",
            color=0xffff00
        )

        ramadan_embed.set_image(url="ضع_رابط_صورة_القوانين_الرمضانية_هنا")

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

# ================= أمر جديد: خط الأخبار / الخط الفاصل =================
@bot.command()
@has_allowed_role()
async def linebar(ctx):
    line_embed = discord.Embed(
        description="",
        color=0xff0000
    )

    # ضع هنا رابط صورة الخط مثل الصورة التي أرسلتها
    line_embed.set_image(url="https://i.imgur.com/aIlc0Vm.png")

    await ctx.send(embed=line_embed)

# شغّل البوت
bot.run(os.getenv("TOKEN") or "ضع_التوكن_هنا")