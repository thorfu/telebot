import asyncio, random

async def hack_fn(message):
    await message.edit_text("🕵️‍♀️ Initializing Penetration Test...")
    await asyncio.sleep(2)
    await message.edit_text("🔍 Searching for Telegram databases in targeted person's device...")
    await asyncio.sleep(2)
    await message.edit_text(
        "🟢 User online: True\n🟢 Telegram access: True\n🟢 Read Storage: True "
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "🔓 Hacking in progress... 0%\n[░░░░░░░░░░░░░░░░░░░░]\n`Searching for Telegram...`\n⏳ ETA: 0m, 20s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "🔓 Hacking in progress... 11.07%\n[██░░░░░░░░░░░░░░░░░░]\n`Still searching for Telegram...`\n⏳ ETA: 0m, 18s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "🔓 Hacking in progress... 20.63%\n[███░░░░░░░░░░░░░░░░░]\n`Found folder /home/user/Telegram 🎉`\n⏳ ETA: 0m, 16s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "🔓 Hacking in progress... 34.42%\n[█████░░░░░░░░░░░░░░░]\n`Found folder /home/user/Telegram 🎉`\n⏳ ETA: 0m, 14s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "🔓 Hacking in progress... 42.17%\n[███████░░░░░░░░░░░░░]\n`Searching for databases 🔍`\n⏳ ETA: 0m, 12s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "🔓 Hacking in progress... 55.30%\n[█████████░░░░░░░░░░░]\n`Found tdata.DBI 📁`\n⏳ ETA: 0m, 10s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "🔓 Hacking in progress... 64.86%\n[███████████░░░░░░░░░]\n`Found tdata.DBI 📁`\n⏳ ETA: 0m, 08s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "🔓 Hacking in progress... 74.02%\n[█████████████░░░░░░░]\n`Trying to Decrypt... 🔐`\n⏳ ETA: 0m, 06s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "🔓 Hacking in progress... 86.21%\n[███████████████░░░░░]\n`Trying to Decrypt... 🔐`\n⏳ ETA: 0m, 04s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "🔓 Hacking in progress... 93.50%\n[█████████████████░░░]\n`Decryption successful! 🎉`\n⏳ ETA: 0m, 02s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "🔓 Hacking in progress... 100%\n[████████████████████]\n`Scanning file... 🔍`\n⏳ ETA: 0m, 00s"
    )
    await asyncio.sleep(2)
    await message.edit_text("🎉 Hacking complete!\n📤 Uploading file...")
    await asyncio.sleep(2)
    await message.edit_text(
        "🎯 Targeted Account Hacked...!\n\n✅ File has been successfully uploaded to my server.\nTelegram Database:\n`./DOWNLOADS/tdata.DBI`"
    )

async def scan_fn(message):
    await message.edit_text("Initializing system scan...")
    await asyncio.sleep(2)
    await message.edit_text(
        "System Scan: 0%\n[░░░░░░░░░░░░░░░░░░░░]\n`Booting up...`\nETA: 0m, 20s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "System Scan: 15%\n[██░░░░░░░░░░░░░░░░░░]\n`Loading system files...`\nETA: 0m, 18s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "System Scan: 30%\n[████░░░░░░░░░░░░░░░░]\n`Scanning directories...`\nETA: 0m, 16s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "System Scan: 45%\n[██████░░░░░░░░░░░░░░]\n`Checking file integrity...`\nETA: 0m, 14s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "System Scan: 60%\n[█████████░░░░░░░░░░░]\n`Analyzing system logs...`\nETA: 0m, 12s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "System Scan: 75%\n[███████████░░░░░░░░░]\n`Inspecting network connections...`\nETA: 0m, 10s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "System Scan: 90%\n[███████████████░░░░░]\n`Finalizing scan...`\nETA: 0m, 08s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "System Scan: 100%\n[████████████████████]\n`Scan complete!`\nETA: 0m, 00s"
    )
    await asyncio.sleep(2)
    await message.edit_text("System scan complete!\nCompiling report...")
    await asyncio.sleep(2)
    await message.edit_text(
        "Scan Report:\n\n✅ No issues found.\nSystem Status: `Healthy`"
    )
    await asyncio.sleep(5)
    await message.delete()


async def ily(message):
    emojis = ["❤️", "🌹", "💫", "🎉", "💖"]
    texts = ["I", "Love", "You"]
    for text in texts:
        for emoji in emojis:
            await message.edit(emoji + " " + text)
            await asyncio.sleep(random.uniform(0.2, 1.0))
    await message.edit("❤️ I 🌹 Love 💫 You 🎉 <3 💖")
    await asyncio.sleep(3)

heart = """
ㅤ⠀⠀⠀⠀    ⠀⢀⣤⣄
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⡆ ⣠⣶⣿⣶⡀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⠋
⠀⠀⠀⠀⣾⣿⣿⣧⠀⠻⣿⣿⠿⠉
⣰⣿⣿⣿⣿⣿⣿⣿
⠸⣿⣿⣿⣿⣿⣿⠏
⠀⠈⠛⠿⣿⣿⡟
"""

heart1 = """
⠀⠀⠀⠀⣀⡤⢤⣄⠀⣠⡤⣤⡀⠀⠀⠀
⠀⠀⢀⣴⢫⠞⠛⠾⠺⠟⠛⢦⢻⣆⠀⠀
⠀⠀⣼⢇⣻⡀⠀⠀⠀⠀⠀⢸⡇⢿⣆⠀
⠀⢸⣯⢦⣽⣷⣄⡀⠀⢀⣴⣿⣳⣬⣿⠀
⢠⡞⢩⣿⠋⠙⠳⣽⢾⣯⠛⠙⢹⣯⠘⣷
⠀⠈⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠁
"""

async def heart_fn(c, msg):
    if c == 1:
        await msg.edit(heart1)
    else:
        await msg.edit(heart)