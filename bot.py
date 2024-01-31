import logging
from pyrogram import Client
from info import API_ID, API_HASH, SESSION
from aiohttp import web
from route import web_server

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="autofilter",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION,
            workers=10,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        logging.info(f"Bot started")
        #web-server
        app = web.AppRunner(await web_server())
        await app.setup()
        port = "8080"
        await web.TCPSite(app, "0.0.0.0", port).start()

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped.")
    
app = Bot()
app.run()