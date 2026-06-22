import os

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

MONGO_DB_URI = os.getenv("MONGO_DB_URI")

OWNER_ID = int(os.getenv("OWNER_ID", 0))

LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", 0))

MUST_JOIN_CHANNEL = os.getenv("MUST_JOIN_CHANNEL")

WEB_URL = os.getenv("WEB_URL")
