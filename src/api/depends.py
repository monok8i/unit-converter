from fastapi import Depends
from typing import Annotated, Union

from logic.converter import LengthConverter, WeightConverter, TemperatureConverter

ConverterType = Union[LengthConverter, WeightConverter, TemperatureConverter]

def get_converter(convert_type: str) -> ConverterType:
    converters = {
        "length": LengthConverter(),
        "weight": WeightConverter(),
        "temperature": TemperatureConverter()
    }
    return converters[convert_type]

GetConverterDep = Annotated[ConverterType, Depends(get_converter)]
