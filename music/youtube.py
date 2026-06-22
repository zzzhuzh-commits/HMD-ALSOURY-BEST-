from yt_dlp import YoutubeDL

async def search_youtube(query):

    ydl_opts = {
        "quiet": True,
        "noplaylist": True
    }

    with YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(
            f"ytsearch:{query}",
            download=False
        )

        if not info["entries"]:
            return None

        video = info["entries"][0]

        return {
            "title": video["title"],
            "url": video["webpage_url"]
        }
