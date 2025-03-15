from typing import Final
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


templates = Jinja2Templates(directory="templates")


UNITS: Final[dict[str, list[str]]] = {
    "length": ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile"],
    "weight": ["milligram", "gram", "kilogram", "pound", "ounce"],
    "temperature": ["celsius", "fahrenheit", "kelvin"],
}


def active_tabs(convert_type: str):
    _tabs: Final[dict[str, str]] = {
        "length": "",
        "weight": "",
        "temperature": "",
    }

    if convert_type in _tabs.keys():
        _tabs[convert_type] = "active"

    return _tabs


def build_page(request: Request, convert_type: str, **kwargs) -> HTMLResponse:

    return templates.TemplateResponse(
        "index.jinja2", 
        {
            "request": request, 
            "convert_type": convert_type, 
            "units": UNITS, 
            **active_tabs(convert_type)
        }
    )


def generate_response(request: Request, convert_type: str, **kwargs) -> HTMLResponse:
    return templates.TemplateResponse(
        "index.jinja2",
        {
            "request": request, 
            "convert_type": convert_type,
            **active_tabs(convert_type),
            **kwargs 
        }
    )

