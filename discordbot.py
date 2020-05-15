from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='キョウカちゃん、')
token = os.environ['DISCORD_BOT_TOKEN']

RoundCount = 0 # 周回数
StageCount = 0 # 段階数
DateCount = 0 # 日数
DateCountLast = 0 # 最終日
BossNum = ["1","2","3","4","5"] # ボス番号
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
    else:
        for one in Booking5:
            member += one + " "
    await ctx.send(BossName + ":" + member)

@bot.command()
async def 予約全削除(ctx):
    reply = "予約を全部消しちゃいます！"
    await ctx.send(reply)
    Booking1 = []
    Booking2 = []
    Booking3 = []
    Booking4 = []
    Booking5 = []
    reply = "コスモブルーフラッシュ!!"
    await ctx.send(reply)

@bot.command()
async def 予約全表示(ctx):
    reply = "予約を全部表示しますね。"
    await ctx.send(reply)
    member = ""
    for one in Booking1:
        member += one + " "
    BossName = BossList[1]
    await ctx.send(BossName + ":" + member)
    member = ""
    for one in Booking2:
        member += one + " "
    BossName = BossList[2]
    await ctx.send(BossName + ":" + member)
    member = ""
    for one in Booking3:
        member += one + " "
    BossName = BossList[3]
    await ctx.send(BossName + ":" + member)
    member = ""
    for one in Booking4:
        member += one + " "
    BossName = BossList[4]
    await ctx.send(BossName + ":" + member)
    member = ""
    for one in Booking5:
        member += one + " "
    BossName = BossList[5]
    await ctx.send(BossName + ":" + member)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def ぴんぐ(ctx):
    await ctx.send('ぽ\nん\nぐ')

bot.run(token)
