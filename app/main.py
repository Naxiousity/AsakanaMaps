from fastapi import FastAPI
from .db import init_db
from .routers.auth import router as auth_router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

# **This line makes /auth/signup live**
app.include_router(auth_router, prefix="/auth", tags=["auth"])


@app.get("/")
async def read_root():
    return {"message": "Asakana App for Me and you babe"}
