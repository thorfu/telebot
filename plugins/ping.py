from pyrogram import Client, filters
import time

@Client.on_message(filters.command(["ping", "alive"], prefixes=".") & filters.me)
async def ping(_, message):
    start = time.time()
    await message.edit("Pong!")
    end = time.time()
    await message.edit(f"Pong! {round(end-start, 2)}s")
