from discord.ext import commands
from datetime import datetime
import discord
import os
import traceback

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 607555169751793674

RoundCount = 0 # 周回数
StageCount = 0 # 段階数
DateCount = 0 # 日数
DateCountLast = 0 # 最終日
BossNum = ["1","2","3","4","5"] # ボス番号
BossList = ["0","ミノタウロス","トライロッカー","メガラパーン","ワイルドグリフォン","ゴブリングレート"] # ボス名前
BossHP = 0 # ボスHP
LoginList = [] #参戦メンバーリスト
Booking1 = ["すぷ","コペ丸"] # 予約を追加するリスト
Booking2 = [] # book→予約
Booking3 = []
Booking4 = []
Booking5 = []

@client.event
async def on_message(message):
    listFlag = 0
    deleteFlag = 0
    displayFlag = 0
    bookingFlag = 0

    if message.content.startswith("キョウカちゃん、")
        if "ping" in message.content:
            await message.channel.send("pong!")
        elif "ぴんぐ" in message.content:
            await message.channel.send("ぽんぐ!")
        elif "確認" in message.content:
            listFlag = 1
        elif "全削除" in message.content:
            deleteFlag = 1
        elif "全表示" in message.content:
            displayFlag = 1
        elif "予約" in message.content:
            bookFlag = 1


#@bot.command()
#async def 足し算(ctx, a: int, b: int):
#    ans = a + b
#    await ctx.send(str(a) + '+' + str(b) + 'は' + str(ans) + 'です')

#@bot.command()
#async def 引き算(ctx, a: int, b: int):
#    ans = a - b
#    await ctx.send(str(a) + '-' + str(b) + 'は' + str(ans) + 'です')

    if listFlag == 1:
        reply = "予約を表示しますね。"
        await message.channel.send(reply)
        for i in BossNum:
            tmpList = []
            BossName = BossList[int(i)]
            if i in message.content:
                BookList = "Booking" + i
                tmpList = [x[0] for x in eval(BookList)]
                member = ""
                for j in tmpList:
                    member += j + " "
                await message.channel.send(BossName + ":" + member)
        listFlag = 0

    elif deleteFlag == 1:
        reply = "予約を全部消しちゃいます！"
        await ctx.send(reply)
        for i in BossNum:
            BookList = "Booking" + i
            eval(BookList).clear()
        reply = "コスモブルーフラッシュ！！"
        await message.channel.send(reply)
        deleteFlag = 0

    elif displayFlag == 1:
        reply = "予約を全部表示しますね。"
        await ctx.send(reply)
        for i in BossNum:
            tmpList = []
            BossName = BossList[int(i)]
            BookList = "Booking" + i
            tmpList= [x[0] for x in eval(BookList)]
            member = ""
            for j in tmpList:
                member += j + " "
            await message.channel.send(BossName + ":" + member)
        displayFlag = 0

    elif bookFlag == 1:
        reply = message.author.display_name + "さんを"
        for i in BossNum:
            if i in message.content:
                BookList = "Booking" + i
                eval(BookList).append([message.author.display_name, str(message.author.mention)])
                BossName = BossList[int(i)]
                reply += " " + BossName
        reply += " に予約しました。"
        if reply == message.author.display_name + "さんを に予約しました。"
            reply = "予約されませんでした。"
        await message.channel.send(reply)
        bookFlag = 0

client.run(token)
