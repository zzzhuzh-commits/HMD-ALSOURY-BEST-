from pyrogram import filters

def register(app):

    @app.on_message(filters.text)
    async def play_music(client, message):

        if not message.text:
            return

        if message.text.startswith("شغل "):

            song = message.text.replace("شغل ", "", 1)

            await message.reply_text(
                f"🎵 جاري البحث عن:\n\n{song}"
            )
