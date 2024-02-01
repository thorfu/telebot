from plugins.modules.urban import get_json

async def get_quotes(message):
  data = await get_json(f"https://api.quotable.io/quotes/random")
  quotes = data.get('content')
  await message.reply(f"{quotes}")
  
