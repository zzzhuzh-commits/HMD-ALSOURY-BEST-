from pyrogram import filters
from config import MUST_JOIN_CHANNEL

def register(app):

    @app.on_message(filters.private & ~filters.bot)
    async def force_sub(client, message):

        if not MUST_JOIN_CHANNEL:
            return

        user_id = message.from_user.id

        try:
            member = await client.get_chat_member(
                MUST_JOIN_CHANNEL,
                user_id
            )

            if member.status in [
                "member",
                "administrator",
                "creator"
            ]:
                return

        except Exception:
            pass

        invite_link = f"https://t.me/{MUST_JOIN_CHANNEL.replace('@','')}"

        await message.reply_text(
            f"""
🔒 يجب الاشتراك بالقناة أولاً

📢 {MUST_JOIN_CHANNEL}

ثم أرسل /start

{invite_link}
"""
        )
        raise StopPropagation
