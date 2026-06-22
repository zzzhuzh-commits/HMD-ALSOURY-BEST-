from pyrogram import Client
from config import *

app = Client(
    "ArabicMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# أوامر البداية
from plugins.start import register as start_register
start_register(app)

# الاشتراك الإجباري
from plugins.force_sub import register as force_sub_register
force_sub_register(app)

# الإذاعات
from plugins.broadcast import register as broadcast_register
broadcast_register(app)

print("HMD-ALSOURY-BEST Started")
app.run()
