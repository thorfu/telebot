from pyrogram import Client, filters

@Client.on_message(filters.command(["help", "h"], prefixes=".") & filters.me)
async def help(_, message):
    await message.edit(
        f"**Commands**\n\n"
        "`.ping` - Check the bot's ping\n"
        "`.urban or .ud <word>` - Get the urban dictionary meaning of the word\n"
        "`.meaning or .m <word>` - Get the meaning of the word\n"
        "`.emoji or .e <emoji>` - To generate emoji text\n"
        "`.facts or .f` - Get random facts\n"
        "`.quotes or .q` - Get random quotes\n"
        "`.ask or .a <question>` - Ask a question\n"
        "`.pfp` - Change your profile picture with random quotes \n"
        "`.run` - Accept all JoinRequest Instantly\n"
        "`.clearchat` - Delete all chat message from your group\n"
    )
