from pyrogram import Client, filters

@Client.on_message(filters.command(["help", "h"], prefixes=".") & filters.me)
async def help(_, message):
    if message.text:
        await message.delete()
    await message.edit(
        f"**Commands**\n\n"
        "`.ping` - Check the bot's ping\n"
        "`.urban or .ud <word>` - Get the urban dictionary meaning of the word\n"
        "`.meaning or .m <word>` - Get the meaning of the word\n"
        "`.emoji or .e <emoji>` - To generate emoji text\n"
        "`.facts or .f` - Get random facts\n"
        "`.quotes or .q` - Get random quotes\n"
        "`.ask or .a <question>` - Ask a question\n"
    )
