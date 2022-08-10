from discord.ext import commands, tasks
from asyncio import sleep
import random
import discord
import datetime
import asyncio
import os
import httpx
import json
from discord.ext.commands.core import guild_only
from discord.raw_models import RawMessageUpdateEvent
from random import choice, randint
from discord.utils import get
from dotenv import load_dotenv
import requests
import sys

pp = ["**8=D**","**8==D**","**8===D**","**8====D**","**8=====D**","**8======D**"]
ben = ["Yes?","No","Ugh","NaNaNa","HoHoHo","Ben?"]
bella = ["Yes?","No","Bruh","NaNaNa","Hehehe","Bella?"]
killmessages = [" died.", " died from cringe."," saw floppa r34", " posted memes in #general", " took the L.", " got rickrolled by a free bobux link.", " got cancelled on Twitter."," got ratio'd on Twitter."," got caught in 4K"," ragequitted."," went to Brazil.", " got ratio'd"," got [Content Deleted]", " died because yes.", " got yeeted."," got permbanned.", " posted cringe 💀"," choked to death on a fortune cookie"," said deez nuts in 2022 💀"," went on a date with a catfishing 69 year old man."," said 'amogus' in 2022 💀"," got rejected by their crush."," found out what poison was."," choked on their spit."," hugged a bee hive"," stuck his pp in a electrical socket"," had explosive diarrhea after eating taco bell."," dabbed in 2022."," bought Stitch Face"," said amogus is still funny"," forgot how to breath 💀"," became emo"," became a TikToker"," became a dream stan"]
hellolist = ["Wsg ","Yo ","Hi ","Hello ","Greeting ","Hola "]

bot = commands.Bot(command_prefix = "%", case_insensitive=True)
bot.requests = httpx.AsyncClient()
blacklist = ""
ID = "898358037239201812"  #enter your user ID

load_dotenv()

def admin_list():
    def predicate(ctx):
        list = [898358037239201812]  # ENTER YOUR USER ID HERE
        return ctx.message.author.id in list

    return commands.check(predicate)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    game = discord.Game("Idfk lol")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
async def hello(ctx):
	await ctx.send(f"{random.choice(hellolist)} {ctx.author.mention}!")

@bot.command()
async def uwu(ctx):
	await ctx.send ("please just stfu u fucking furry")

@bot.command()
async def die(ctx):
	await ctx.send("make me oh right u cant cuz im a fucking bot dumbass")

@bot.command()
async def imfat(ctx):
	await ctx.send("L BOZO")
  
@bot.command()
async def ampro(ctx):
	await ctx.send("i smell cap")

@bot.command()
async def deez(ctx):
	await ctx.send("deez nuts in yo mouth")


@bot.command()
async def candice(ctx):
	await ctx.send("candice dick fit in yo mouth")

@bot.command()
async def imgay(ctx):
	await ctx.send("ok?")

@bot.command()
async def gayrate(ctx, user: discord.Member):
 await ctx.send(f"{user.mention} is {random.randrange(101)}% gay")


@bot.command()
async def bella(ctx, text: str):
    await ctx.send(f"My Answer To **{text}** was **{random.choice(bella)}**")

@bot.command()
async def ben(ctx, text: str):
    await ctx.send(f"My Answer To **{text}** was **{random.choice(ben)}**")


@bot.command()
async def ratio(ctx, user: discord.Member):
    await ctx.send(f"{user.mention} L + don’t care + didn’t ask + cry about it + who asked + stay mad + get real + mald, seethe, cope harder + incorrect + hoes mad + pound sand + basic skill issue + typo + ur dad left + you fell off + no u + the audacity + triggered + repelled + get a life + ok and? + cringe + go outside + touch grass + kick rocks + think again + not based + not funny didn’t laugh + get good + reported + small pp + ur allergic to sunlight + GG! + get rekt + trolled + your loss + muted + banned + kicked + permaban + useless + i slept with ur mom + redpilled + i said it better + tiktok fan + get a life + unsubscribed + plundered + go tell reddit + talk nonsense + you're a full time discord mod + you’re* + grammar issue + nerd + get clapped + go outside + bleach + lol + gay + retard + autistic + reported + ask deez + ez clap + straight cash + idgaf + stay mad + youre lost + you “re” + stay pressed + reverse double take back + pedophile + cancelled + don't give a damn + get a job + dumb kid + sussy baka + get blocked + mad free + freer than air + furry + rip bozo + you're a (insert stereotype) + slight_smile + aired + cringe again + mad cuz bad + my pronouns are xe, xem & xyr + irrelevant + deal with it + screencapped your bio + karen/kyle + jealous + you're deaf + balls + i'll be right back + go ahead whine about it + eat paper + you lose + your problem + no one cares + log off + don't care even more + sex offender + sex defender + get religion + NFT owner + you make bad memes + problematic + fall in line + dog water + you are going to my cringe comp + you failed kindergarten + you have a anime profile picture + an* + fatherless + motherless + sisterless + brotherless + orphan + catch some bitches + I don't care about your opinion + genshin player + you dress like garbage + 日 amogus + get fucked + queued + put some thought into what you're going to do with that + stfu + go to bed + yes, i'm taller than you + I win BOZO")


@bot.command()
async def earsburn(ctx):
	await ctx.send("https://youtu.be/fujCdB93fpw")

@bot.command()
async def never(ctx):
    await ctx.send("https://youtu.be/fujCdB93fpw")

@bot.command()
async def stfu1(ctx):
	await ctx.send("https://cdn.discordapp.com/attachments/841451660059869194/958183891536056380/MemeFeedBot.mov")

@bot.command()
async def invite(ctx):
	await ctx.send("https://discord.com/oauth2/authorize?client_id=898570522261065748&permissions=8&scope=bot")

@bot.command()
async def amogus(ctx):
    await ctx.send("cringy ass mf 💀💀💀")


@bot.command()
async def freerobux(ctx):
    await ctx.send("goofy ahh 5 year old")


@bot.command()
async def ballz(ctx):
    await ctx.send(
        "Can I put My Ballz In Yo Jaws Ballz In Yo Jaws Can iiii Can iiii Can iiii Can iiii"
    )

@bot.command()
async def slap(ctx):
    await ctx.send("<https://youtu.be/4pMDXygA688>")


@bot.command()
async def fatherless(ctx):
    await ctx.send("<https://youtu.be/p4-rtsidmh8>")


@bot.command()
async def weeb(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/841451660059869194/958480754617233408/MemeFeedBot.mov?5055d5f502867d9ef900225ce4df37bfd956bedfa1b82f97f6e74b7e927697fb"
    )


@bot.command()
async def chad(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/841451660059869194/958484667441487882/MemeFeedBot.mp4"
    )


@bot.command()
async def stfu2(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/841451660059869194/957022464095961098/MemeFeedBot.mp4?5111d310cada3ff90e34d05d346c41c475ab54f0f193a8f458fc46e94dc9a1ec"
    )


@bot.command()
async def kys(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/841451660059869194/987913380201390110/MemeFeedBot.mov?de5d4298159510fb0bee754707cd92d4fa9948440badf195db16884eac686a5c"
    )


@bot.command()
async def punch(ctx):
    await ctx.send("<https://youtu.be/AexeWtlbEBk>")


@bot.command()
async def clown(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/841451660059869194/958479783602290728/MemeFeedBot.mov"
    )


@bot.command()
async def FORTNITE(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/841451660059869194/958495289495416852/MemeFeedBot.mp4?f1fb5465cfb1f22cca0df7d7b09e961ab5e62e7ccdbed2e103b923e7c58a89e1"
    )


@bot.command()
async def FU(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/841451660059869194/958494697762979890/MemeFeedBot.mov"
    )


@bot.command()
async def OG(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/841451660059869194/958490151221338182/MemeFeedBot.mp4?f3e8d0cf41eea2528d13b017c28fd28dcc021d06a6eff5e20f140355a956c37f"
    )


@bot.command()
async def FU2(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/841451660059869194/958865376547045406/MemeFeedBot.mov"
    )


@bot.command()
async def credits(ctx):
    await ctx.send("MemeFeedBot for da memes and me for making the script lol")



@bot.command()
async def hehe(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/972211631796932699/972237687220240454/28uapGkzLQg145fi53jitYsnYGkqEBTs.webm")


@bot.command()
async def ohno(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/841451660059869194/987880068627963935/MemeFeedBot.mov")


@bot.command()
async def GOOF(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/841451660059869194/987881094915457104/MemeFeedBot.mov")


@bot.command()
async def AYO(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/841451660059869194/982024245485908018/MemeFeedBot.mov")


@bot.command()
async def yes(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/841451660059869194/975927777914159134/MemeFeedBot.mp4")


@bot.command()
async def cock(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/841451660059869194/969336055708925952/MemeFeedBot.mp4")


@bot.command()
async def POOPMAN(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/841451660059869194/969333932980068372/MemeFeedBot.mov")


@bot.command()
async def RAP(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/841451660059869194/969013394889912390/MemeFeedBot.mp4")

@bot.command(aliases=['user' , 'info' , 'userinfo'])
async def whois(ctx, member : discord.Member):
  if member == None:
    member = ctx.author
  whoisembed=discord.Embed(title=f"Userinfo of {member.name}" , description= member.mention , color= discord.Color.blue())
  whoisembed.add_field(name = "User id" , value = member.id , inline=True )
  whoisembed.add_field(name= "Nickname" , value= member.nick, inline=True)
  whoisembed.add_field(name= "Created Date" , value= member.created_at, inline=True)
  whoisembed.set_footer(text = "Generated By Wextra" , icon_url = 'https://media.discordapp.net/attachments/862890805131345930/991468541503086632/image0.jpg?width=810&height=810')
  await ctx.send(embed=whoisembed)

@bot.command()
async def eight_ball(context):

    possible_responses = [

        'That is a resounding no',

        'It is not looking likely',

        'Too hard to tell',

        'It is quite possible',

        'Definitely',

        'Maybe so.'
    ]
    await context.channel.send(random.choice(possible_responses) + ", " + context.message.author.mention)

@bot.command()
async def uwontbelievewhathappens(ctx):
    await ctx.send("https://youtu.be/fujCdB93fpw")

@bot.command()
async def server(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name} Info", description="Information of this Server", color=discord.Colour.blue())
    embed.add_field(name='🆔Server ID', value=f"{ctx.guild.id}", inline=True)
    embed.add_field(name='📆Created On', value=ctx.guild.created_at.strftime("%b %d %Y"), inline=True)
    embed.add_field(name='👑Owner', value=f"{ctx.guild.owner.mention}", inline=True)
    embed.add_field(name='👥Members', value=f'{ctx.guild.member_count} Members', inline=True)
    embed.add_field(name='💬Channels', value=f'{len(ctx.guild.text_channels)} Text | {len(ctx.guild.voice_channels)} Voice', inline=True)
    embed.add_field(name='🌎Region', value=f'{ctx.guild.region}', inline=True)
    embed.set_thumbnail(url=ctx.guild.icon_url) 
    embed.set_footer(text="⭐ • Duo")    

    await ctx.send(embed=embed)

@bot.command()  # troll command
async def summon(ctx):
    await ctx.send(f"Fuck off {ctx.message.author.mention}! Im sleeping, Bitch!")
    
@bot.command()
async def console(ctx):
   message = await ctx.send("H")
   await message.edit(content=f"He")
   await asyncio.sleep(0.7)
   await message.edit(content="Hel")
   await asyncio.sleep(0.7)
   await message.edit(content=f"Hell")
   await asyncio.sleep(0.7)
   await message.edit(content="Hello")
   await asyncio.sleep(0.7)
   await message.edit(content=f"Hello T")
   await asyncio.sleep(0.7)
   await message.edit(content="Hello Th")
   await asyncio.sleep(0.7)
   await message.edit(content=f"Hello The")
   await asyncio.sleep(0.7)
   await message.edit(content="Hello Ther")
   await asyncio.sleep(0.7)
   await message.edit(content=f"Hello There {ctx.message.author.mention}")
   await message.edit(content=f"Hello There {ctx.message.author.mention}!")
   await asyncio.sleep(0.7)
   await message.edit(content=f"Hello There {ctx.message.author.mention}!!")
   await asyncio.sleep(0.7)
   await message.edit(content=f"Hello There {ctx.message.author.mention}!!!")
   await asyncio.sleep(0.7)
    
    
@bot.command()
async def cat(ctx):
   message = await ctx.send("A package has Arrived!")
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(3.5)
   await message.edit(content=f"""Hi...
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(3.5)
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(3.5)
   await message.edit(content=f"""Hi...
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(3.5)
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(3.5)
   await message.edit(content=f"""Hi...
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")		
   await asyncio.sleep(3.5)
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(3.5)
   await message.edit(content=f"""Hi...
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")		
   await asyncio.sleep(3.5)

@bot.command()
async def nuke(ctx, user: discord.Member):
   message = await ctx.send(f"{ctx.message.author.mention} has put a nuke In {user.mention} House, it will go off in **5**")
   await asyncio.sleep(3.5)
   await message.edit(content=f"**4**")
   await asyncio.sleep(1.5)
   await message.edit(content="**3**")
   await asyncio.sleep(1.5)
   await message.edit(content=f"**2**")
   await asyncio.sleep(1.5)
   await message.edit(content="**1**")
   await asyncio.sleep(1.5)
   await message.edit(content=f"https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831")
   await asyncio.sleep(1.7)
   await message.edit(content="**BOOM**")
   await asyncio.sleep(3)
   await message.edit(content=f"rip bozo {user.mention}")
   await asyncio.sleep(3)
   await message.edit(content=f"rest in piss {user.mention}")
   await asyncio.sleep(3)
   await message.edit(content=f"fatty {user.mention}")
   await asyncio.sleep(3)
   await message.edit(content=f"my grandma could've out ran that nuke and shes dead 💀💀💀💀 {user.mention}")
   await asyncio.sleep(3)

    
@bot.command()
async def IQ(ctx, user: discord.Member):
  await ctx.send(f"{user.mention} has {random.randrange(101)} IQ")

@bot.command()
async def coolrate(ctx, user: discord.Member):
  await ctx.send(f"{user.mention} is {random.randrange(101)} cool")

@bot.command()
async def dumbrate(ctx, user: discord.Member):
  await ctx.send(f"{user.mention} is {random.randrange(101)} dumb")

@bot.command()
async def pprate(ctx, user: discord.Member):
  await ctx.send(f"{user.mention} pp size {random.choice(pp)}")

@bot.command()
async def retardrate(ctx, user: discord.Member):
 await ctx.send(f"{user.mention} is {random.randrange(101)}% a retard")

async def cringerate(ctx, user: discord.Member):
 await ctx.send(f"{user.mention} is {random.randrange(101)}% cringe")

@bot.command()
async def quote(ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote_ = json_data[0]['q'] + " ~ " + json_data[0]['a']
    await ctx.send(quote_)

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.command()
async def restart(ctx):
    id = str(ctx.author.id)
    if id == '898358037239201812': # YOUR DISCORD ID HERE
        await ctx.send('Restarting...')
        restart_bot()
    else:
        await ctx.send("You dont have sufficient permmisions to perform this action!")

@bot.command()
async def echo(ctx, text: str):
	await ctx.send(f"**{text}**")

@bot.command()
async def flashingconsole(ctx, text: str):
   message = await ctx.send(f"{text}")
   await message.edit(content=f"⠀⠀⠀")
   await asyncio.sleep(1.7)
   await message.edit(content=f"{text}")
   await asyncio.sleep(1.7)
   await message.edit(content=f"⠀⠀⠀")
   await asyncio.sleep(1.7)
   await message.edit(content=f"{text}")
   await asyncio.sleep(1.7)
   await message.edit(content=f"⠀⠀⠀")
   await asyncio.sleep(1.7)
   await message.edit(content=f"{text}")
   await asyncio.sleep(1.7)
   await message.edit(content=f"⠀⠀⠀")
   await asyncio.sleep(1.7)
   await message.edit(content=f"{text}")
   await asyncio.sleep(1.7)
   await message.edit(content=f"⠀⠀⠀")
   await message.edit(content=f"{text}")
   await asyncio.sleep(1.7)  

@bot.command()
async def kill(ctx, user: discord.Member):
 await ctx.send(user.mention + random.choice(killmessages))

@bot.command()
async def furryrate(ctx, user: discord.Member):
  await ctx.send(f"{user.mention} is {random.randrange(101)}% a furry")

async def customcat(ctx, text: str):
   message = await ctx.send("A package has Arrived!")
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""{text}
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""{text}
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""{text}
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")		
   await asyncio.sleep(2.0)
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""{text}
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")		
   await asyncio.sleep(2.0)
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""{text}
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")		
   await asyncio.sleep(2.0)

@bot.command()
async def bitchesrate(ctx, user: discord.Member):
  await ctx.send(f"{user.mention} is {random.randrange(101)}% bitchless")


bot.run(os.getenv("DISCORD_TOKEN"))
