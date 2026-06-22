from pyrogram import Client
from config import *

app = Client(
    "ArabicMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
async def start_handler(client, message):
    if message.text == "/start":
        await message.reply_text(
            "🎵 أهلاً بك في بوت الموسيقى العربي"
        )

app.run()
