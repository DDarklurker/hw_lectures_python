# на зірочку написати тайпінг до цього класу
from typing import Union, TypeVar


class Lenth():
    metric = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
              "in": 0.0254, "ft": 0.3048, "yd": 0.9144,
              "mi": 1609.344}

    def __init__(self, value: Union[float, int], unit="m") -> None:
        self.value = value
        self.unit = unit

    def converToMeters(self) -> 'Lenth':
        return self.value * self.metric[self.unit]

    def __add__(self, other: 'Lenth') -> 'Lenth':
        lenth_meter = self.converToMeters() + other.converToMeters()
        return Lenth(lenth_meter / Lenth.metric[self.unit], self.unit)

    def __sub__(self, other: 'Lenth') -> None:
        pass

    def __mul__(self, other: 'Lenth') -> None:
        pass

    def __divmod__(self, other: 'Lenth') -> None:
        pass

    def __ge__(self, other: 'Lenth') -> 'Lenth':
        return max(self.converToMeters(), other.converToMeters())

    def __str__(self) -> str:
        return str(self.converToMeters()) + "m"

    def __repr__(self) -> str:
        return f"Lenth {self.value} {self.unit}"
