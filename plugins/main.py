from pyrogram import Client, filters
from plugins.modules import urban, emoji, spam, meaning
import time


@Client.on_message(filters.command("start", prefixes=".") & filters.me)
async def start(_, message):
    await message.reply_text("Hello, World!")

@Client.on_message(filters.command("ping", prefixes=".") & filters.me)   
async def ping(_, message):
    start = time.time()
    await message.edit("Pong!")
    end = time.time()
    await message.edit(f"Pong! {round(end-start, 2)}s") 

@Client.on_message(filters.command(["urban", "ud"], prefixes="."))
async def get_urban(client, message):
    await urban(client, message)

@Client.on_message(filters.command(["meaning", "m"], prefixes="."))
async def get_meaning(_, message):
    await meaning(message)    

@Client.on_message(filters.command("emoji", prefixes=".") & filters.private)
async def get_emoji(_, message):
    await emoji(message)

@Client.on_message(filters.command("spam", prefixes=".") & filters.me)
async def spam_message(_, message):
    await spam(message)