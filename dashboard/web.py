from fastapi import FastAPI
from fastapi.responses import HTMLResponse

web = FastAPI()

@web.get("/")
async def home():
    return HTMLResponse("""
    <h1>🎵 HMD ALSOURY MUSIC</h1>
    <p>لوحة التحكم تعمل بنجاح</p>
    """)
