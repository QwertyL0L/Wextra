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
async def UL(ctx):
    embed = discord.Embed(title="UpdateLogs", description="updates coming soon", colour=discord.Color.blue())

    await ctx.send(embed=embed) 


@bot.command()
async def hello(ctx):
    embed = discord.Embed(title="Yo!", description="wsg", colour=discord.Color.blue())

    await ctx.send(embed=embed) 

@bot.command()
async def uwu(ctx):
    embed = discord.Embed(title="stfu", description="please just stfu u fucking furry", colour=discord.Color.blue())

    await ctx.send(embed=embed) 


@bot.command()
async def die(ctx):
    embed = discord.Embed(title="im good thx", description="make me oh right u cant cuz im a fucking bot dumbass", colour=discord.Color.blue())

    await ctx.send(embed=embed) 

@bot.command()
async def imfat(ctx):
    embed = discord.Embed(title="no shit", description="L BOZO", colour=discord.Color.blue())

    await ctx.send(embed=embed) 
  
@bot.command()
async def ampro(ctx):
    embed = discord.Embed(title="nah fam", description="i smell cap", colour=discord.Color.blue())

    await ctx.send(embed=embed) 

@bot.command()
async def deez(ctx):
    embed = discord.Embed(title="u already knew where this was going", description="deez nuts in yo mouth", colour=discord.Color.blue())

    await ctx.send(embed=embed)


@bot.command()
async def candice(ctx):
    embed = discord.Embed(title="bruh just stop ok?", description="candice dick fit in yo mouth", colour=discord.Color.blue())

    await ctx.send(embed=embed)

@bot.command()
async def imgay(ctx):
    embed = discord.Embed(title="uh ok?", description="ok cool i didnt ask tho", colour=discord.Color.blue())

    await ctx.send(embed=embed)


@bot.command()
async def ben2(ctx):
    await ctx.send("bendover 😩")

@bot.command()
async def ben1(ctx):
    embed = discord.Embed(title="what", description="Yes?", colour=discord.Color.blue())

    await ctx.send(embed=embed)

@bot.command()
async def ratio(ctx):
    embed = discord.Embed(title="cool but...", description="L + don’t care + didn’t ask + cry about it + who asked + stay mad + get real + bleed + mald seethe cope harder + dilate + incorrect + hoes mad + pound sand + basic skill issue + typo + ur dad left + you fell off + no u + the audacity + triggered + repelled + ur a minor + k. + any askers + get a life + ok and? + cringe + copium + go outside + touch grass + kick rocks + quote tweet + think again + not based + not funny didn’t laugh + social credits -999, 999, 999, 999 + get good + reported + ad hominem + ok boomer + small pp + ur allergic to sunlight + GG! + get rekt + trolled + your loss + muted + banned + kicked + permaban + useless + i slept with ur mom + yo momma + yo momma so fat + redpilled + no bitches allowed + i said it better + tiktok fan + get a life + unsubscribed + plundered + go tell reddit + donowalled + simp + get sticked bug LOL + talk nonsense + trump supporter + your’re a full time discord mod + you’re* + grammar issue + nerd + get clapped + kys + lorem ipsum dolor sit amet + go outside + bleach + lol + gay + retard + autistic + reported + ask deez + ez clap + straight cash + idgaf + ratio again + stay mad + read FAQ + youre lost + you “re” + stay pressed + reverse double take back + pedophile + cancelled + done for + don't give a damn + get a job + sus + baka + sussy baka + get blocked + mad free + freer than air + furry + rip bozo + you're a (insert stereotype) + slight_smile + aired + cringe again + Super Idol的笑容 + mad cuz bad + my pronouns are xe, xem & xyr + irrelevant + deal with it + screencapped your bio + karen/kyle + jealous + you're deaf + balls + i'll be right back + go ahead whine about it + not straight + eat paper + you lose + count to three + your problem + no one cares + log off + don't care even more + sex offender + sex defender + get religion + not okay + glhf + NFT owner + you make bad memes + problematic + fall in line + dog water + you look like a wall + you don’t know 2 + 2 with yo head ass + you are going to my cringe compilation + you can’t count to five + try again + you failed kindergarten + rickrolled + no lifer + guten freunden schickt man einen deutschen panzer + you have a anime profile picture + an* + fatherless + motherless + sisterless + brotherless + orphan + you can't catch this ratio + catch some bitches + I don't care about your opinion + genshin player + you dress like garbage + 日本語がお上手ですね + get fucked + you can’t understand what the word intelligence means with your dumb ass + you have hair + queued + put some thought into what you're going to do with that + stfu + go to bed + yes, i'm taller than you + i think your joke is funny + i rejected your mother's advances + marooned + you can’t read + I win + final ratio", colour=discord.Color.blue())

    await ctx.send(embed=embed)

@bot.command()
async def earsburn(ctx):
    embed = discord.Embed(title="lol", url="https://youtu.be/fujCdB93fpw",description="click the link to see a funny meme! (memes provided by youtube and memefeedbot)", colour=discord.Color.blue())

    await ctx.send(embed=embed)

@bot.command()
async def never(ctx):
    embed = discord.Embed(title="dont click me",url="https://youtu.be/fujCdB93fpw", description="dont click the link or else", colour=discord.Color.blue())

    await ctx.send(embed=embed)

@bot.command()
async def stfu1(ctx):
    embed = discord.Embed(title="click  me to see the meme",url="https://cdn.discordapp.com/attachments/841451660059869194/958183891536056380/MemeFeedBot.mov", description="click the link to see a funny meme! (memes provided by memefeedbot)", colour=discord.Color.blue())

    await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
    embed = discord.Embed(title="click me to invite the bot!",url="https://discord.com/oauth2/authorize?client_id=%20898570522261065748&permissions=8&scope=bot", description="click the link to invite the bot!", colour=discord.Color.blue())

    await ctx.send(embed=embed)

@bot.command()
async def amogus(ctx):
    await ctx.send("cringy ass")


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
  whoisembed.set_footer(text = "Generated By 0w0" , icon_url = 'https://media.discordapp.net/attachments/862890805131345930/991468541503086632/image0.jpg?width=810&height=810')
  await ctx.send(embed=whoisembed)

@bot.command(name='8ball',

            description="Answers a yes/no question.",

            brief="Answers from the beyond.",

            aliases=['eight_ball', 'eightball', '8-ball'],

            pass_context=True)

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
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + "Server Info",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

    @bot.command(name="summon")  # troll command
async def p(ctx):
    await ctx.send(f"Fuck off {ctx.message.author.mention}! Im sleeping, Bitch!")
    
bot.run(os.getenv("DISCORD_TOKEN"))
