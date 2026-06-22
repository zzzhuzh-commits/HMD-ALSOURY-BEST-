from pyrogram import filters
from database.playlists import (
    add_playlist,
    get_playlist,
    delete_playlist
)

def register(app):

    @app.on_message(filters.command("اضف_للقائمة"))
    async def add_song(client, message):

        text = message.text.split(None, 2)

        if len(text) < 3:
            await message.reply_text(
                "مثال:\n/اضف_للقائمة اسم_الأغنية الرابط"
            )
            return

        title = text[1]
        url = text[2]

        await add_playlist(
            message.from_user.id,
            title,
            url
        )

        await message.reply_text(
            "✅ تمت إضافة الأغنية"
        )

    @app.on_message(filters.command("قائمة_التشغيل"))
    async def show_playlist(client, message):

        songs = await get_playlist(
            message.from_user.id
        )

        if not songs:
            await message.reply_text(
                "❌ القائمة فارغة"
            )
            return

        text = "🎵 قائمة التشغيل:\n\n"

        for song in songs:
            text += f"• {song['title']}\n"

        await message.reply_text(text)

    @app.on_message(filters.command("حذف_من_القائمة"))
    async def remove_song(client, message):

        text = message.text.split(None, 1)

        if len(text) < 2:
            return

        await delete_playlist(
            message.from_user.id,
            text[1]
        )

        await message.reply_text(
            "🗑 تم الحذف"
        )
