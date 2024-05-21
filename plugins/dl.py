import os, re, mimetypes
import requests
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
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
        msg = await message.edit("Fetching...")
        await asyncio.sleep(3)  # wait for 3 seconds
        msg = await message.edit("Download started...")
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            filename = os.path.basename(urlparse(response.url).path)
            # Check if the URL already has an extension
            _, url_extension = os.path.splitext(filename)
            if url_extension:
                filename += url_extension
            else:
                content_disposition = response.headers.get('content-disposition')
                if content_disposition:
                    filename = re.findall('filename=(.+)', content_disposition)[0]
                else:
                    # Guess the file extension based on the Content-Type header
                    content_type = response.headers.get('content-type')
                    if content_type:
                        extension = mimetypes.guess_extension(content_type)
                        if extension:
                            filename += extension

            if os.path.exists(filename):
                await msg.edit("File already exists. Uploading...")
                await client.send_document(message.chat.id, filename)
                await message.delete()
                return
            total_size = int(response.headers.get('content-length', 0))
            downloaded_size = 0
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=524288): 
                    if chunk: 
                        f.write(chunk)
                        downloaded_size += len(chunk)
                        progress = (downloaded_size / total_size) * 100
                        try:
                            await msg.edit(f"Downloading... {progress:.2f}%")
                        except FloodWait as e:
                            await asyncio.sleep(e.x)  # Sleep for the time recommended by Telegram
            await msg.edit("Download complete. Uploading...")
            await asyncio.sleep(1)
            await msg.edit("Uploading...")
            m = await client.send_document(message.chat.id, filename)
            if m:
                await message.delete()
            os.remove(filename)
        else:
            await msg.edit(f"Failed to download {url}")
    except Exception as e:
        await msg.edit(f"Failed to download {url}\n{e}")