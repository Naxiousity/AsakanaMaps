from fastapi import FastAPI
from .routers import auth
from .db import init_db



app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(auth.router)

@app.get("/")
async def read_root():
    return {"message": "Asakana App for Me and you babe"}
