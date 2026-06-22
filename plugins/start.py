from pyrogram import filters

def register(app):

    @app.on_message(filters.command("start"))
    async def start_cmd(client, message):
        await message.reply_text(
            "🎵 أهلاً بك في سورس HMD-ALSOURY-BEST"
        )

    @app.on_message(filters.command("ping"))
    async def ping_cmd(client, message):
        await message.reply_text(
            "🏓 البوت يعمل"
        )
