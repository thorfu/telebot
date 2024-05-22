import time, asyncio, logging, aiohttp
from info import DEPLOY_HOOK
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from plugins.facts import get_facts
from plugins.emoji import emoji
from plugins.quotes import get_quotes
from plugins.urban import urban, meaning
from plugins.imgq import set_profile_photo, add_quote_to_image
from plugins.telegraph import telegraph
from plugins.yt_dl import song, vsong
from plugins.animation import hack_fn, ily, heart_fn


@Client.on_message(filters.command(["help", "h"], prefixes=".") & filters.me)
async def help_cmd(_, message):
    await message.edit_text(
        f"**Commands**\n\n"
        "`.ping` - Check the bot's ping\n"
        "`.urban or .ud <word>` - Get the urban dictionary meaning of the word\n"
        "`.meaning or .m <word>` - Get the meaning of the word\n"
        "`.emoji or .e <emoji>` - To generate emoji text\n"
        "`.facts or .f` - Get random facts\n"
        "`.quotes or .q` - Get random quotes\n"
        "`.ask or .a <question>` - Ask a question\n"
        "`.pfq` - Change your profile picture with random quotes\n"
        "`.bio` - Change your bio with random quotes\n"
        "`.imgq` - Generate image with random quotes\n"
        "`.telegraph` - Create a telegraph post\n"
        "`.song <song name | song url>` - Download song from youtube\n"
        "`.video <video url>` - Download video from youtube\n"
        "`.spam <number> <text>` - Spam the text\n"
        "`.on9 <on | off>` - To activate One9word game cheat\n"
        "`.approve` - Approve all joinRequest\n"
        "`.clearchat` - Delete all chat message from your group\n"
        "`.update` - Deploy the latest changes\n"
        "`.dl` - download from http url\n"
        "`.hack` - Hack animation\n",
        parse_mode=enums.ParseMode.MARKDOWN
    )


@Client.on_message(filters.command("ping", prefixes=".") & filters.me)   
async def ping(_, message):
    start = time.time()  
    m = await message.edit("Pong!")
    end = time.time()
    await m.edit(f"Pong! {round(end-start, 2)}s") 

@Client.on_message(filters.command("update", [".", "/"]) & filters.me)
async def deploy(_, message):
    m = await message.edit("Deploying the latest changes...")
    await asyncio.sleep(2)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(DEPLOY_HOOK) as resp:
                if resp.status == 200:
                    await m.edit("Deploying...!")
                else:
                    await m.edit("Failed to deploy!")
    except Exception as e:
        await message.edit(f"Error: {str(e)}")    

typing_on = False
@Client.on_message(filters.command("typing", prefixes=".") & filters.me)
async def typing(client, message):
    global typing_on
    typing_on = not typing_on
    await message.delete()
    if typing_on:
        while True:
            if not typing_on:
                break
            await client.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
            await asyncio.sleep(5)
            

playing_on = False
@Client.on_message(filters.command("playing", prefixes=".") & filters.me)
async def playing(client, message):
    global playing_on
    playing_on = not playing_on
    await message.delete()
    if playing_on:
        while True:
            if not playing_on:
                break
            await client.send_chat_action(message.chat.id, enums.ChatAction.PLAYING)
            await asyncio.sleep(5)
        

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
@Client.on_message(filters.command("pfq", prefixes=".") & filters.me)
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

@Client.on_message(filters.command("bio", prefixes=".") & filters.me)
async def change_bio(client, message):
    try:
        msg = await message.edit("Changing bio...")
        while True:
            quote = await get_quotes()
            if len(quote) <= 70:
                await client.update_profile(bio=quote)
                await msg.edit(f"**Bio has been changed to:** {quote}")
                break    
    except Exception as e:
        await message.edit(f"An error occurred: {e}")            

@Client.on_message(filters.command("imgq", prefixes=".") & filters.me)
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

@Client.on_message(filters.command("hack", prefixes=".") & filters.me)
async def hack_cmd(client: Client, message: Message):
    await hack_fn(message)

@Client.on_message(filters.command("ily", prefixes=".") & filters.me)
async def ily_cmd(client: Client, message: Message):
    await ily(message)

@Client.on_message(filters.command("heart", prefixes=".") & filters.me)
async def heart_cmd(client: Client, message: Message):
    number = int(message.command[1]) if len(message.command) > 1 else 0
    await heart_fn(number, message)