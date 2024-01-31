import google.generativeai as genai
from pyrogram import Client, filters
import time
import asyncio
from info import GENAI_API_KEY

SUDO = set()
ACCESS = False
GLOBAL_ACCESS = False

genai.configure(api_key=GENAI_API_KEY)


def gemini(text):
    try:
        generation_config = {
            "temperature": 0.6,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        }
        safety_settings = [
          {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_ONLY_HIGH"
          },
          {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_ONLY_HIGH"
          },
          {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_ONLY_HIGH"
          },
          {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_ONLY_HIGH"
          },
        ]
        model = genai.GenerativeModel(model_name="gemini-pro",
                                      generation_config=generation_config,
                                      safety_settings=safety_settings)
        convo = model.start_chat()
        convo.send_message(text)
        return f"{convo.last.text}"
    except Exception as e:
        print(f"Error generating text: {str(e)}")
        return f"Error generating text: {str(e)}"
    
@Client.on_message(filters.command("alive", prefixes=".") & filters.me)
async def start(_, message):
    await message.edit("I'm alive.")

@Client.on_message(filters.command("ping", prefixes=".") & filters.me)
async def ping(_, message):
    start = time.time()
    await message.edit("Pong!")
    end = time.time()
    await message.edit(f"Pong!\nTook {round(end-start, 2)}s")

@Client.on_message(filters.command("sudo", prefixes=".") & filters.me)
async def sudo(client, message):
    user_id = message.reply_to_message.from_user.id if message.reply_to_message else None
    if user_id:
        SUDO.add(user_id)
        k = await client.get_users(user_id)
        name = k.first_name if not k.last_name else k.first_name + " " + k.last_name
        m = await message.edit(f"<b>{name}</b> has been given sudo access.")
        await asyncio.sleep(5)
        await m.delete()
    else:
        m = await message.edit("Reply to a message to give sudo access to the user.")
        await asyncio.sleep(2)
        await m.delete()

@Client.on_message(filters.command("unsudo", prefixes=".") & filters.me)
async def unsudo(client, message):
    user_id = message.reply_to_message.from_user.id if message.reply_to_message else None
    if user_id and user_id in SUDO:
        SUDO.remove(user_id)
        k = await client.get_users(user_id)
        name = k.first_name if not k.last_name else k.first_name + " " + k.last_name
        m = await message.edit(f"<b>{name}</b> has been removed from sudo access.")
        await asyncio.sleep(5)
        await m.delete()
    else:
        m = await message.edit("Reply to a message to remove sudo access from the user.")
        await asyncio.sleep(3)
        await m.delete()

@Client.on_message(filters.command("access", prefixes=".") & filters.me)
async def access(_, message):
    global ACCESS
    ACCESS = not ACCESS
    m = await message.edit("Access has been granted" if ACCESS else "Access has been revoked")
    await asyncio.sleep(2)
    await m.delete()

@Client.on_message(filters.command("global", prefixes=".") & filters.me)
async def gaccess(_, message):
    global GLOBAL_ACCESS
    GLOBAL_ACCESS = not GLOBAL_ACCESS
    m = await message.edit("Global access has been granted" if GLOBAL_ACCESS else "Global access has been revoked")
    await asyncio.sleep(2)
    await m.delete()    

@Client.on_message(filters.text & filters.me)
async def genmessage(_, message):
    if ACCESS:
        await message.edit(gemini(message.text))

@Client.on_message(filters.text)
async def gen_message(_, message):
    if ACCESS and message.from_user.id in list(SUDO):
        await message.reply(gemini(message.text))
    if ACCESS and GLOBAL_ACCESS:
        await message.reply(gemini(message.text))