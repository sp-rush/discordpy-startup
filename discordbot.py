from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

RoundCount = 0 # 周回数
StageCount = 0 # 段階数
DateCount = 0 # 日数
DateCountLast = 0 # 最終日
BossNum = ["1","2","3","4","5"] # ボス番号
BossList = ["0","ミノタウロス","トライロッカー","メガラパーン","ワイルドグリフォン","ゴブリングレート"] # ボス名前
BossHP = 0 # ボスHP
MemberList = [] #メンバーリスト
Booking1 = [] # 予約を追加するリスト
Booking2 = [] # book→予約
Booking3 = []
Booking4 = []
Booking5 = []

@client.event
async def on_message(message):
    listFlag = 0
    bookFlag = 0
    endFlag = 0
    displayFlag = 0
    
    if message.content.startswith("キョウカちゃん、予約"):
       if "見せて" in message.content: # 指定したボスの予約を表示
           listFlag = 1
       elif "全削除" in message.content: # 全ての予約を削除
           endFlag = 1
       elif "全部見せて" in message.content: # 全ての予約を表示
           displayFlag = 1
       else: # 予約する
           bookFlag = 1

       if listFlag == 1: # 指定したボスの予約を表示
           reply = "予約を表示しますね。"
           await message.channel.send(reply)
           for Boss in BossNum:
               tmpList = []
               if Boss in message.content:
                  BookList = "Booking" + Boss
                  tmpList = [x[0] for x in eval(BookList)]
                  BossName = BossList[int(Boss)]
                  member = ""
                  for one in tmpList:
                      member += one + " "
                  await message.channel.send(BossName + ":" + member)
           listFlag =  0

       elif endFlag == 1: # 全ての予約を削除
           reply = "予約を全部消しちゃいます！"
           await message.channel.send(reply)
           for Boss in BossNum:
                  BookList = "Booking" + Boss
                  eval(BookList).clear()
           reply = "コスモブルーフラッシュ!!"
           await message.channel.send(reply)
           endFlag = 0

       elif displayFlag == 1: # 全ての予約を表示
           reply = "予約を全部表示しますね。"
           await message.channel.send(reply)
           for Boss in BossNum:
               tmpList = []
               BookList = "Booking" + Boss
               tmpList= [x[0] for x in eval(BookList)]
                  BossName = BossList[int(Boss)]
                  member = ""
                  for one in tmpList:
                      member += one + " "
                  await message.channel.send(BossName + ":" + member)
           displayFlag = 0

       elif bookFlag == 1: # 予約する
           reply = message.author.display_name + "さんを"
           bossCount = 0
           for Boss in BossNum:
               if Boss in message.content:
                  BookList = "Booking" + Boss
                  eval(BookList).append([message.author.display_name, str(message.author.mention)])
                  BossName = BossList[int(Boss)]
                  reply += BossName + " "
                  bossCount += 1
           if bossCount >= 1:
               reply += "に予約しました。"
               await message.channel.send(reply)

           reply = "現在の予約↓\n"
           for Boss in BossNum:
               tmpList = []
               if Boss in message.content:
                  BookList = "Booking" + Boss
                  tmpList = [x[0] for x in eval(BookList)]
                  BossName = BossList[int(Boss)]
                  member = ""
                  for one in tmpList:
                      member += one + " "
                      reply += BossName + ":" + member + "\n"
                  await message.channel.send(BossName + ":" + member)
           bookFlag = 0

    elif message.content.startswith("fin"):
        for Boss in BossNum:
               if Boss in message.content:
                   BookList = "Booking" + Boss
                   eval(BookList).remove([message.author.display_name,str(message.author.mention)]) 
        reply = "削除完了 >" + message.author.display_name
        await message.channel.send(reply)

    elif message.content.startswith("ment"):
        for Boss in BossNum:
            tmpList = []
            if Boss in message.content:
                  BookList = "Booking" + Boss
                  tmpList = [x[1] for x in eval(BookList)]
                  member = ""
                  for one in tmpList:
                      member += one + " "
                  await message.channel.send("Boss" + Boss + ":" + member)
    
    elif message.content.startswith("cmd"):
        reply = "予約:rsv 1-5 / 予約表示:rsv list 1-5 / 予約全表示:rsv! / 予約削除:fin 1-5 / 予約全削除:rsv END / 通知:ment 1-5"
        await message.channel.send(reply)

        
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


client.run(token)
bot.run(token)
