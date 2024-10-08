#!/usr/bin/env python3

import sys
import discord
from discord.ext import commands
import asyncio
from cogs.utils import set_config,get_config
import logging

logging.basicConfig(level=logging.INFO)

# call make config
# get token object
set_config("config.ini")
    

token = ""
try:
    token = get_config().token
    assert len(token) > 10
except Exception as e:
    print(e)
    print("Missing token.")
    print("Edit 'config.ini' and add your token accordingly.")
    print("Press Enter to continue...")
    input()
    sys.exit(0)

async def start_bot():
    bot = commands.Bot(command_prefix=get_config().prefix or ",", intents=discord.Intents.all(), help_command=None)

    cfg = get_config()
    if(cfg.help_cog):
        print("Loaded help cog")
        await bot.load_extension('cogs.help_cog')   
    if(cfg.music_cog):
        print("Loaded music cog")
        await bot.load_extension('cogs.music_cog')
    if(cfg.wow_cog ):
        print("Loaded wow cog")
        await bot.load_extension('cogs.wow_cog')
    return bot

async def main():
    bot = await start_bot()
    await bot.start(f'{token}')

if __name__ == '__main__':
    # bot = asyncio.run(start_bot())
    # bot.run(f'{token}')
    asyncio.run(main())


