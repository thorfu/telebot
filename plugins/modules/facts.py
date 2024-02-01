from plugins.modules.urban import get_json

async def get_facts(message):
    fact = await get_json(f"https://nekos.life/api/v2/fact")
    if not fact:
        await message.reply(f"Something went wrong!")
    await message.reply(f"{fact}")
