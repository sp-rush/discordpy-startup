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
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def ぴんぐ(ctx):
    await ctx.send('ぽんぐ')

bot.run(token)
