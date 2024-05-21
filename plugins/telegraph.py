import os
import logging
from telegraph import upload_file

logging.basicConfig(level=logging.ERROR)

async def telegraph(client, message):
    if not message.reply_to_message:
        await message.edit('Reply to a message with .telegraph')
        return
    reply = message.reply_to_message
    if reply.media:
        if reply.media.document or reply.media.photo or reply.media.video or reply.media.animation:
            file = await client.download_media(reply)
            try:
                media = upload_file(file)
                if media:
                    await message.edit(f'https://telegra.ph{media[0]}')
                os.remove(file)
            except Exception as e:
                await message.edit(str(e))
    else:
        await message.edit('Reply to a media file with .telegraph')