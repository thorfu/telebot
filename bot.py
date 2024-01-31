import os
import google.generativeai as genai
from pyrogram import Client, filters
from flask import Flask, redirect
from threading import Thread
import time
import asyncio

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")
GENAI_API_KEY = os.getenv("GENAI_API_KEY")

SUDO = set()
ACCESS = False
GLOBAL_ACCESS = False

genai.configure(api_key=GENAI_API_KEY)

bot = Client(
    name="geminibot",
    session_string=SESSION,
    api_id=API_ID,
    api_hash=API_HASH
)

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
        model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings)
        convo = model.start_chat()
        convo.send_message(text)
        return f"{convo.last.text}"
    except Exception as e:
        print(f"Error generating text: {str(e)}")
        return f"Error generating text: {str(e)}"
    
@bot.on_message(filters.command("ping", prefixes=".") & filters.me)
async def ping(_, message):
    start = time.time()
    await message.edit(f"<code>Pong!</code>")
    end = time.time()
    await message.edit(f"<code>Pong! {round(end-start, 2)}s</code>")

@bot.on_message(filters.command("sudo", prefixes=".") & filters.me)
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


@bot.on_message(filters.command("unsudo", prefixes=".") & filters.me)
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

@bot.on_message(filters.command("access", prefixes=".") & filters.me)
async def access(_, message):
    global ACCESS
    ACCESS = not ACCESS
    m = await message.edit("Access has been granted" if ACCESS else "Access has been revoked")
    await asyncio.sleep(2)
    await m.delete()

@bot.on_message(filters.command("global", prefixes=".") & filters.me)
async def gaccess(_, message):
    global GLOBAL_ACCESS
    GLOBAL_ACCESS = not GLOBAL_ACCESS
    m = await message.edit("Global access has been granted" if GLOBAL_ACCESS else "Global access has been revoked")
    await asyncio.sleep(2)
    await m.delete()    

@bot.on_message(filters.text & filters.me)
async def genmessage(_, message):
    if ACCESS:
        await message.edit(gemini(message.text))

@bot.on_message(filters.text)
async def gen_message(_, message):
    if ACCESS and message.from_user.id in list(SUDO):
        await message.reply(gemini(message.text))
    if ACCESS and GLOBAL_ACCESS:
        await message.reply(gemini(message.text))
    
app = Flask(__name__)

@app.route('/')
def index():
    return redirect("https://telegram.me/iryme", code=302)

def run():
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))

if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    bot.run()