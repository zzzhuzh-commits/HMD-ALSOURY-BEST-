from pyrogram import filters
from database.users import add_user

def register(app):

    @app.on_message(filters.command("start"))
    async def start_cmd(client, message):

        await add_user(message.from_user.id)

        await message.reply_text(
            """
🎵 أهلاً بك في سورس HMD-ALSOURY-BEST

✨ بوت موسيقى عربي متكامل

📌 الأوامر:
/ping - فحص البوت
/help - المساعدة
            """
        )

    @app.on_message(filters.command("ping"))
    async def ping_cmd(client, message):
        await message.reply_text(
            "🏓 البوت يعمل بنجاح"
        )

    @app.on_message(filters.command("help"))
    async def help_cmd(client, message):
        await message.reply_text(
            """
🎵 قائمة الأوامر

/start - تشغيل البوت
/help - المساعدة
/ping - فحص البوت

🎶 سيتم إضافة:
• قوائم التشغيل
• الإذاعات
• الاشتراك الإجباري
• لوحة التحكم
            """
        )
