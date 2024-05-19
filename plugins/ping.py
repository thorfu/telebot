from pyrogram import Client, filters
import time

@Client.on_message(filters.command("ping", prefixes=".") & filters.me)   
async def ping(_, message):
    start = time.time()  
    m = await message.edit("Pong!")
    end = time.time()
    await m.edit(f"Pong! {round(end-start, 2)}s") 
    if message.text:
        await message.delete()