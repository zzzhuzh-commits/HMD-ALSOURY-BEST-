from database.mongo import playlists

async def add_playlist(user_id, title, url):

    await playlists.insert_one(
        {
            "user_id": user_id,
            "title": title,
            "url": url
        }
    )

async def get_playlist(user_id):

    data = []

    async for song in playlists.find(
        {"user_id": user_id}
    ):
        data.append(song)

    return data

async def delete_playlist(user_id, title):

    await playlists.delete_one(
        {
            "user_id": user_id,
            "title": title
        }
    )
