from fastapi.params import Form
from fastapi.routing import APIRouter
from fastapi.requests import Request

from templates.build import build_page, generate_response
from api.depends import GetConverterDep


router = APIRouter()


@router.get("/{convert_type:str}")
def index(request: Request, convert_type: str):
    return build_page(request, convert_type)


@router.post("/{convert_type:str}")
def convert(request: Request, converter: GetConverterDep, convert_type: str, value: str = Form(), from_unit: str = Form(), to_unit: str = Form()):
    result = converter.convert(int(value), from_unit, to_unit)

    return generate_response(request, convert_type, converted_value=result, value=value, from_unit=from_unit, to_unit=to_unit)