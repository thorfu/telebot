import logging, os
from pyrogram import Client
from info import API_ID, API_HASH, SESSION
from aiohttp import web
from plugins.route import web_server

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="telebot",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION,
            workers=100,
            plugins={"root": "plugins"}
        )

    async def start(self):
        await super().start()
        logging.info(f"Bot started")
        await self.send_message(chat_id="me", text="Bot started")
        #web-server
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", port=os.getenv("PORT", 5051)).start()

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped.")
    
app = Bot()
app.run()