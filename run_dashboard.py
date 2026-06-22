import uvicorn
from dashboard.web import web

uvicorn.run(
    web,
    host="0.0.0.0",
    port=8000
)
