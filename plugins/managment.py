from pyrogram import Client, filters, enums

@Client.on_message(filters.command("leave", prefixes=".") & filters.me)
async def leave(client, message):
    try:
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            await client.leave_chat(message.chat.id)
    except Exception as e:
        await message.edit_text(f"{e}")

@Client.on_message(filters.command("kick", prefixes=".") & filters.me)
async def kick(client, message):
    try:
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            await client.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    except Exception as e:
        await message.edit_text(f"{e}")

@Client.on_message(filters.command("ban", prefixes=".") & filters.me)
async def ban(client, message):
    try:
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            await client.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    except Exception as e:
        await message.edit_text(f"{e}")

@Client.on_message(filters.command("unban", prefixes=".") & filters.me)
async def unban(client, message):
    try:
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            await client.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    except Exception as e:
        await message.edit_text(f"{e}")

@Client.on_message(filters.command("promote", prefixes=".") & filters.me)
async def promote(client, message):
    try:
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            await client.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    except Exception as e:
        await message.edit_text(f"{e}")

@Client.on_message(filters.command("demote", prefixes=".") & filters.me)
async def demote(client, message):
    try:
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            await client.demote_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    except Exception as e:
        await message.edit_text(f"{e}")

@Client.on_message(filters.command("pin", prefixes=".") & filters.me)
async def pin(client, message):
    try:
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            await client.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    except Exception as e:
        await message.edit_text(f"{e}")

@Client.on_message(filters.command("unpin", prefixes=".") & filters.me)
async def unpin(client, message):
    try:
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            await client.unpin_chat_message(message.chat.id)
    except Exception as e:
        await message.edit_text(f"{e}")

@Client.on_message(filters.command("mute", prefixes=".") & filters.me)
async def mute(client, message):
    try:
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            await client.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages=False)
    except Exception as e:
        await message.edit_text(f"{e}")

@Client.on_message(filters.command("unmute", prefixes=".") & filters.me)
async def unmute(client, message):
    try:
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            await client.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages=True)
    except Exception as e:
        await message.edit_text(f"{e}")