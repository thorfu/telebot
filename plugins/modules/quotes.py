import aiohttp
from pyrogram import Client, filters

async def get_quotes():
    url = "https://api.quotable.io/quotes/random"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                quote_data = await response.json()
                
                # Check if the response is a list of quotes
                if isinstance(quote_data, list) and len(quote_data) > 0:
                    quote = quote_data[0]
                    return quote.get("content", None)
                
                # If not a list, assume it's a single quote
                return quote_data.get("content", None)
            else:
                return None

@Client.on_message(filters.command(["quotes", "q", "quote"], prefixes=".") & filters.me)
async def get_quote(_, message):
    if message.text:
        await message.delete()
    quotes = await get_quotes()
    await message.reply(f"{quotes}")