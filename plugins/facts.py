from plugins.urban import get_json
from pyrogram import Client, filters

async def get_facts(message):
    data = await get_json(f"https://nekos.life/api/v2/fact")
    fact = data.get('fact')
    if not fact:
        await message.reply(f"Something went wrong!")
    await message.reply(f"{fact}")

@Client.on_message(filters.command(["facts", "f"], prefixes=".") & filters.me)
async def fact_msg(_, message):
    if message.text:
        await message.delete()
    await get_facts(message)
