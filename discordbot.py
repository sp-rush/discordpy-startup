from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='キョウカちゃん、')
token = os.environ['DISCORD_BOT_TOKEN']
        
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
    await ctx.send('予約を確認します。')
    for Boss in BossNum:
        tmpList = []
            if Boss in a:
                BookList = "Booking" + Boss
                tmpList = [x[0] for x in eval(BookList)]
                BossName = BossList[int(Boss)]
                member = ""
            for one in tmpList:
                member += one + " "
            await ctx.send(BossName + ":" + member)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def ぴんぐ(ctx):
    await ctx.send('ぽんぐ')

bot.run(token)
