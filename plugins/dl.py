import os
import time
import aiohttp
from pyrogram import Client, filters
from urllib.parse import urlparse

CHUNK_SIZE = 1024 * 1024  # 1MB
RETRY_TIMES = 3

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
        msg = await message.edit("Downloading...")
        async with aiohttp.ClientSession() as session:
            for i in range(RETRY_TIMES):
                try:
                    async with session.get(url, allow_redirects=True) as resp:
                        if resp.status == 200:
                            filename = os.path.basename(urlparse(resp.url).path)
                            if os.path.exists(filename):
                                await msg.edit("File already exists. Uploading...")
                                await client.send_document(message.chat.id, filename)
                                await message.delete()
                                return
                            with open(filename, "wb") as f:
                                total_size = int(resp.headers.get('content-length', 0))
                                downloaded_size = 0
                                start_time = time.time()
                                while True:
                                    chunk = await resp.content.read(CHUNK_SIZE)
                                    if not chunk:
                                        break
                                    downloaded_size += len(chunk)
                                    f.write(chunk)
                                    elapsed_time = time.time() - start_time
                                    speed = downloaded_size / elapsed_time
                                    progress = (downloaded_size / total_size) * 100
                                    await msg.edit(f"Downloading... {progress:.2f}% Speed: {speed:.2f} bytes/sec")
                            await msg.edit("Uploading...")
                            await client.send_document(message.chat.id, filename)
                            await message.delete()
                            os.remove(filename)
                        else:
                            await msg.edit(f"Failed to download {url}")
                        break
                except Exception as e:
                    if i < RETRY_TIMES - 1:  # i is zero indexed
                        await msg.edit(f"Failed to download {url}. Retrying...")
                        continue
                    else:
                        await msg.edit(f"Failed to download {url}\n{e}")
                        break
    except Exception as e:
        await msg.edit(f"Failed to download {url}\n{e}")