import time, asyncio, logging
from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.facts import get_facts
from plugins.emoji import emoji
from plugins.quotes import get_quotes
from plugins.urban import urban, meaning
from plugins.pfpquote import set_profile_photo, add_quote_to_image
from plugins.telegraph import telegraph
from plugins.yt_dl import song, vsong


@Client.on_message(filters.command(["help", "h"], prefixes=".") & filters.me)
async def help_cmd(_, message):
    await message.edit(
        f"**Commands**\n\n"
        "`.ping` - Check the bot's ping\n"
        "`.urban or .ud <word>` - Get the urban dictionary meaning of the word\n"
        "`.meaning or .m <word>` - Get the meaning of the word\n"
        "`.emoji or .e <emoji>` - To generate emoji text\n"
        "`.facts or .f` - Get random facts\n"
        "`.quotes or .q` - Get random quotes\n"
        "`.ask or .a <question>` - Ask a question\n"
        "`.pfp` - Change your profile picture with random quotes \n"
        "`.run` - Accept all JoinRequest Instantly\n"
        "`.clearchat` - Delete all chat message from your group\n"
    )


@Client.on_message(filters.command("ping", prefixes=".") & filters.me)   
async def ping(_, message):
    start = time.time()  
    m = await message.edit("Pong!")
    end = time.time()
    await m.edit(f"Pong! {round(end-start, 2)}s") 

@Client.on_message(filters.command(["facts", "f"], prefixes=".") & filters.me)
async def fact_msg(_, message):
    await get_facts(message)

@Client.on_message(filters.command(["emoji", "e"], prefixes=".") & filters.me)
async def get_emoji(_, message):
    await emoji(message)

@Client.on_message(filters.command(["quotes", "q", "quote"], prefixes=".") & filters.me)
async def get_quote(_, message):
    quotes = await get_quotes()
    await message.edit(f"{quotes}")

@Client.on_message(filters.command(["spam", "s"], prefixes=".") & filters.me)
async def spam_message(_, message):
    _, *text_parts = message.text.split()
    await message.delete()
    try:
        number_of_messages = int(text_parts[0])
        text = ' '.join(text_parts[1:])
    except ValueError:
        number_of_messages = 10
        text = ' '.join(text_parts)
    if text:  # Only send messages if there's text to be spammed
        for _ in range(number_of_messages):
            await message.reply_text(text)


@Client.on_message(filters.command(["urban", "ud"], prefixes=".") & filters.me)
async def get_urban(_, message):
    await urban(message)

@Client.on_message(filters.command(["meaning", "m"], prefixes=".") & filters.me)
async def get_meaning(_, message):
    await meaning(message)

# Command to change profile picture
@Client.on_message(filters.command("pfp", prefixes=".") & filters.me)
async def change_pfp(client, message):
    try:
        m = await message.edit("Changing profile pic...")
        success = await set_profile_photo(client)
        if success:
            await m.edit_text("Profile picture has been changed successfully")
        else:
            await m.edit_text("Failed to change profile picture")
        await asyncio.sleep(30)
        await m.delete()
    except Exception as e:
        await message.edit(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}")

@Client.on_message(filters.command("imagequote", prefixes=".") & filters.me)
async def image_quote(client, message):
    try:
        m = await message.edit("Fetching image quote...")
        quotes = await get_quotes()
        if quotes:
            IMAGE_URL = "https://source.unsplash.com/random/800x600"
            photo_path = add_quote_to_image(IMAGE_URL, quotes)
            if photo_path:
                await client.send_photo(message.chat.id, photo=photo_path)
                await m.delete()
                return
    except Exception as e:
        await message.edit(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}")

@Client.on_message(filters.command("telegraph", prefixes=".") & filters.me)
async def telegraph_cmd(client, message):
    await telegraph(client, message)
            
@Client.on_message(filters.command(['song', 'mp3'], prefixes=".") & filters.me)
async def song_cmd(_, message):
    await song(_, message)

@Client.on_message(filters.command(['video', 'mp4'], prefixes=".") & filters.me)
async def vsong_cmd(_, message: Message):
    await vsong(_, message)