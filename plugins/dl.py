import os
import requests
import asyncio
from pyrogram import Client, filters
from urllib.parse import urlparse

@Client.on_message(filters.command(["download", "dl"], prefixes=".") & filters.me)
async def download(client, message):
    url = None
    if message.reply_to_message:
        url = message.reply_to_message.text
    elif len(message.command) > 1:
        url = message.command[1]
    if not url or not url.startswith(("http", "https")):
        await message.edit("Please provide a valid URL or reply to a message containing a URL")
        return
    try:
        msg = await message.edit("Waiting for page to load...")
        await asyncio.sleep(5)  # wait for 10 seconds
        msg = await message.edit("Downloading...")
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            filename = os.path.basename(urlparse(response.url).path)
            if os.path.exists(filename):
                await msg.edit("File already exists. Uploading...")
                await client.send_document(message.chat.id, filename)
                await message.delete()
                return
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024): 
                    if chunk: 
                        f.write(chunk)
            await msg.edit("Uploading...")
            m = await client.send_document(message.chat.id, filename)
            if m:
                await message.delete()
            os.remove(filename)
        else:
            await msg.edit(f"Failed to download {url}")
    except Exception as e:
        await msg.edit(f"Failed to download {url}\n{e}")