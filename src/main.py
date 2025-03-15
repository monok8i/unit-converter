from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request


app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")

templates = Jinja2Templates(directory="src/templates")

@app.get("/{convert_type:str}")
def index(request: Request, convert_type: str):
    active_tabs: dict = {
        "lenght": "",
        "weight": "",
        "temperature": "",
    }

    if convert_type in active_tabs.keys():
        active_tabs[convert_type] = "active"

    return templates.TemplateResponse("index.html", {"request": request, **active_tabs})
