from pyrogram import Client, filters, enums

@Client.on_message(filters.command("leave", prefixes=".") & filters.me)
async def leave(client, message):
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        await client.leave_chat(message.chat.id)
        
        