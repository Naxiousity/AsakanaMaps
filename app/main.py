from fastapi import FastAPI
from .db import init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
async def read_root():
    return {"message": "Asakana App for Me and you babe"}

