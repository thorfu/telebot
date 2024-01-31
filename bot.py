import os
import google.generativeai as genai
from pyrogram import Client, filters
from flask import Flask, redirect
from threading import Thread
import time

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")
GENAI_API_KEY = os.getenv("GENAI_API_KEY")

SUDO = set()
ACCESS = False

genai.configure(api_key=GENAI_API_KEY)

bot = Client(
    name="geminibot",
    session_string=SESSION,
    api_id=API_ID,
    api_hash=API_HASH
)

def gemini(text):
    try:
        model = genai.GenerativeModel(model_name="gemini-pro")
        convo = model.start_chat()
        convo.send_message(text)
        return f"{convo.last.text}"
    except Exception as e:
        print(f"Error generating text: {str(e)}")
        return f"Error generating text: {str(e)}"
    
@bot.on_message(filters.command("alive", prefixes=".") & filters.me)
async def start(_, message):
    await message.edit("Hello! I'm alive.")

@bot.on_message(filters.command("ping", prefixes=".") & filters.me)
async def ping(_, message):
    start = time.time()
    await message.edit("Pong!")
    end = time.time()
    await message.edit(f"Pong!\nTook {round(end-start, 2)}s")

@bot.on_message(filters.command("sudo", prefixes=".") & filters.me)
async def sudo(_, message):
    user_id = message.reply_to_message.from_user.id if message.reply_to_message else None
    if user_id:
        SUDO.add(user_id)
        await message.reply_text(f"User {user_id} has been given sudo access.")
    else:
        await message.reply_text("Reply to a message to give sudo access to the user.")

@bot.on_message(filters.command("unsudo", prefixes=".") & filters.me)
async def unsudo(_, message):
    user_id = message.reply_to_message.from_user.id if message.reply_to_message else None
    if user_id and user_id in SUDO:
        SUDO.remove(user_id)
        await message.edit(f"User {user_id} has been removed from sudo access.")
    else:
        await message.edit("Reply to a message to remove sudo access from the user.")

@bot.on_message(filters.command("access", prefixes=".") & filters.me)
async def access(_, message):
    global ACCESS
    ACCESS = not ACCESS
    await message.edit("Access has been granted" if ACCESS else "Access has been revoked")    

@bot.on_message(filters.text & filters.me)
async def genmessage(_, message):
    if ACCESS:
        await message.edit(gemini(message.text))

@bot.on_message(filters.text)
async def gen_message(_, message):
    if ACCESS and message.from_user.id in list(SUDO):
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