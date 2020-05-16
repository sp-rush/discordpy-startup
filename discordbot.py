from discord.ext import commands
from discord.ext import tasks
from datetime import datetime
import discord
import os
import traceback

bot = commands.Bot(command_prefix='キョウカちゃん、')
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 607555169751793674

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '07:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おはよう')  

RoundCount = 0 # 周回数
StageCount = 0 # 段階数
DateCount = 0 # 日数
DateCountLast = 0 # 最終日
# BossNum = ["1","2","3","4","5"] # ボス番号
BossList = ["0","ミノタウロス","トライロッカー","メガラパーン","ワイルドグリフォン","ゴブリングレート"] # ボス名前
BossHP = 0 # ボスHP
MemberList = [] #メンバーリスト
Booking1 = ["すぷ","コペ丸"] # 予約を追加するリスト
Booking2 = [] # book→予約
Booking3 = []
Booking4 = []
Booking5 = []

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def 足し算(ctx, a: int, b: int):
    ans = a + b
    await ctx.send(str(a) + '+' + str(b) + 'は' + str(ans) + 'です')

@bot.command()
async def 引き算(ctx, a: int, b: int):
    ans = a - b
    await ctx.send(str(a) + '-' + str(b) + 'は' + str(ans) + 'です')

@bot.command()
async def 予約確認(ctx, a: int):
    reply = "予約を表示しますね。"
    flag = 0
    await ctx.send(reply)
    BossName = BossList[a]
    member = ""
    if a == 1:
        for one in Booking1:
            member += one + " "
    elif a == 2:
        for one in Booking2:
            member += one + " "
    elif a == 3:
        for one in Booking3:
            member += one + " "
    elif a == 4:
        for one in Booking4:
            member += one + " "
    elif a == 5:
        for one in Booking5:
            member += one + " "
    else:
        flag = 1
    
    if flag == 0:
        await ctx.send(BossName + ":" + member)
    else:
        await ctx.send("表示失敗しました。")

@bot.command()
async def 予約全削除(ctx):
    reply = "予約を全部消しちゃいます！"
    await ctx.send(reply)
    Booking1.clear()
    Booking2.clear()
    Booking3.clear()
    Booking4.clear()
    Booking5.clear()
    reply = "コスモブルーフラッシュ!!"
    await ctx.send(reply)

@bot.command()
async def 予約全表示(ctx):
    reply = "予約を全部表示しますね。"
    await ctx.send(reply)
    member = BossList[1] + ":"
    for one in Booking1:
        member += one + " "
    member += "\n" + BossList[2] + ":"
    for one in Booking2:
        member += one + " "
    member += "\n" + BossList[3] + ":"
    for one in Booking3:
        member += one + " "
    member += "\n" + BossList[4] + ":"
    for one in Booking4:
        member += one + " "
    member += "\n" + BossList[5] + ":"
    for one in Booking5:
        member += one + " "
    await ctx.send(member)

@bot.command()
async def 予約(ctx, a: int):
    flag = 0
    reply = ctx.author.display_name + "さんを"
    if a == 1:
        Booking1.append(ctx.author.display_name)
    elif a == 2:
        Booking2.append(ctx.author.display_name)
    elif a == 3:
        Booking3.append(ctx.author.display_name)
    elif a == 4:
        Booking4.append(ctx.author.display_name)
    elif a == 5:
        Booking5.append(ctx.author.display_name)
    else:
        flag = 1
    BossName = BossList[a] 
    reply += BossName + "に予約しました。"
    if flag == 1:
        reply = "予約失敗しました。"
    await ctx.send(reply)

    member = "現在の予約↓\n"
    member = BossList[1] + ":"
    for one in Booking1:
        member += one + " "
    member += "\n" + BossList[2] + ":"
    for one in Booking2:
        member += one + " "
    member += "\n" + BossList[3] + ":"
    for one in Booking3:
        member += one + " "
    member += "\n" + BossList[4] + ":"
    for one in Booking4:
        member += one + " "
    member += "\n" + BossList[5] + ":"
    for one in Booking5:
        member += one + " "
    await ctx.send(member)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def ぴんぐ(ctx):
    await ctx.send('ぽんぐ')

bot.run(token)

#ループ処理実行
loop.start()

client.run(token)
