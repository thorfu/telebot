import os
import logging, asyncio
from pyrogram import Client, filters
from telegraph import upload_file

logging.basicConfig(level=logging.ERROR)

@Client.on_message(filters.command("telegraph", prefixes=".") & filters.me)
async def telegraph_upload(bot, update):
    replied = update.reply_to_message
    if not replied:
        await update.edit("Reply to a media file under 5MB to upload to telegra.ph!")
        await asyncio.sleep(5)
        return
    file_info = get_file_id(replied)
    if not file_info:
        await update.edit("Not supported!")
        await asyncio.sleep(5)
        await update.delete()
        return
    text = await update.edit(text="<code>Downloading to my server ...</code>", disable_web_page_preview=True)   
    media = await update.reply_to_message.download()   
    await text.edit_text("<code>Downloading completed. Now I am uploading to telegra.ph...</code>")                                            
    try:
        response = upload_file(media)
    except Exception as error:
        logging.error(error)
        await text.edit_text(f"Error :- {error}")       
        return    
    try:
        os.remove(media)
    except Exception as error:
        logging.error(error)
        return    
    await text.edit_text(
        text=f"<b>Link :-</b>\n\n<code>https://graph.org{response[0]}</code>",
        )
    
async def get_file_id(reply):
    if reply.photo:
        return reply.photo.file_id
    if reply.animation:
        return reply.animation.file_id
    if reply.video:
        return reply.video.file_id
    if reply.document:
        return reply.document.file_id
    return None