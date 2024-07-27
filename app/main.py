from fastapi import FastAPI
from app.routes import user, discussion

app = FastAPI()

app.include_router(user.router, prefix="/api/v1")
app.include_router(discussion.router, prefix="/api/v1")
