from pyrogram import filters
from config import OWNER_ID
from database.users import get_users

def register(app):

    @app.on_message(filters.command(["broadcast", "اذاعه"]))
    async def broadcast_cmd(client, message):

        if message.from_user.id != OWNER_ID:
            return

        if not message.reply_to_message:
            await message.reply_text(
                "❌ قم بالرد على الرسالة المراد إذاعتها"
            )
            return

        users = await get_users()

        sent = 0
        failed = 0

        for user_id in users:

            try:
                await message.reply_to_message.copy(user_id)
                sent += 1

            except Exception:
                failed += 1

        await message.reply_text(
            f"""
✅ تمت الإذاعة

📨 تم الإرسال: {sent}
❌ فشل: {failed}
"""
        )
