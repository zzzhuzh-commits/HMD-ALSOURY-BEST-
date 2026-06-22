from database.mongo import users

async def add_user(user_id):

    user = await users.find_one(
        {"user_id": user_id}
    )

    if not user:
        await users.insert_one(
            {"user_id": user_id}
        )

async def get_users():

    data = []

    async for user in users.find():
        data.append(user["user_id"])

    return data
