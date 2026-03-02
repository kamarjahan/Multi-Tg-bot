import os
import asyncio
import logging
from pyrogram import Client, idle
from aiohttp import web
from dotenv import load_dotenv

# Enable basic logging to see errors
logging.basicConfig(level=logging.INFO)

load_dotenv()

# Initialize Bot
app = Client(
    "multi_bot",
    bot_token=os.getenv("BOT_TOKEN"),
    api_id=int(os.getenv("API_ID")) if os.getenv("API_ID") else None,
    api_hash=os.getenv("API_HASH"),
    plugins=dict(root="begin") # Points to your begin folder
)

# Hugging Face Health Check Server
async def handle_health_check(request):
    return web.Response(text="Bot is running!")

async def start_web_server():
    server = web.Application()
    server.router.add_get('/', handle_health_check)
    runner = web.AppRunner(server)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 7860)
    await site.start()
    logging.info("Web server started on port 7860")

async def main():
    # 1. Start the web server first
    await start_web_server()
    
    # 2. Start the Pyrogram bot safely
    logging.info("Starting Telegram Bot...")
    await app.start()
    logging.info("✅ Bot is online and listening!")
    
    # 3. Keep the script running forever so it can listen
    await idle()
    
    # 4. Stop the bot gracefully when you press Ctrl+C
    await app.stop()

if __name__ == "__main__":
    # This ensures the async loop runs perfectly
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())