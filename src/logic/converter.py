from abc import ABC, abstractmethod

class Converter(ABC):
    @abstractmethod
    def convert(self, **kwargs) -> int:
        raise NotImplementedError


class LengthConverter(Converter):
    """
    target_value = source_value * (coefficient of the original unit/coefficient of the target unit)
    """

    def __init__(self) -> None:
        self.factors = {
            "millimeter": 0.001,
            "centimeter": 0.01,
            "meter": 1,
            "kilometer": 1000,
            "inch": 0.0254,
            "foot": 0.3048,
            "yard": 0.9144,
            "mile": 1609.34,
        }

    def convert(self, value: int, from_unit: str, to_unit: str) -> int:
        if from_unit == to_unit:
            return value
        
        return value * (self.factors[from_unit] / self.factors[to_unit])


class WeightConverter(Converter):
    """
    target_value = source_value * (coefficient of the original unit/coefficient of the target unit)
    """

    def __init__(self) -> None:
        self.factors = {
            "milligram": 0.001,
            "gram": 1,
            "kilogram": 1000,
            "ounce": 28.3495,
            "pound": 453.592,
        }
    
    def convert(self, value: int, from_unit: str, to_unit: str) -> int:
        if from_unit == to_unit:
            return value
        
        return value * (self.factors[from_unit] / self.factors[to_unit])
            


class TemperatureConverter(Converter):
    def __init__(self) -> None:
        self.temperature_conversions = {
            ("celsius", "fahrenheit"): lambda c: c * 9 / 5 + 32,
            ("celsius", "kelvin"): lambda c: c + 273.15,
            ("fahrenheit", "celsius"): lambda f: (f - 32) * 5 / 9,
            ("fahrenheit", "kelvin"): lambda f: (f - 32) * 5 / 9 + 273.15,
            ("kelvin", "celsius"): lambda k: k - 273.15,
            ("kelvin", "fahrenheit"): lambda k: (k - 273.15) * 9 / 5 + 32,
        }

    def convert(self, value: int, from_unit: str, to_unit: str) -> int:
        if from_unit == to_unit:
            return value
        return self.temperature_conversions[(from_unit, to_unit)](value)
