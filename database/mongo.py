from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI

mongo = AsyncIOMotorClient(MONGO_DB_URI)

db = mongo["HMD_MUSIC"]

users = db.users
groups = db.groups
playlists = db.playlists
settings = db.settings
