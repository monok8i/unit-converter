from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api import router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)
