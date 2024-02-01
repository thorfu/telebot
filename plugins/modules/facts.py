from plugins.modules.urban import get_json

async def get_facts(message):
    data = await get_json(f"https://nekos.life/api/v2/fact")
    fact = data.get('fact')
    if not fact:
        await message.reply(f"Something went wrong!")
    await message.reply(f"{fact}")
