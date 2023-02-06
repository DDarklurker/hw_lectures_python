# task3
"""
В відриві від проекту обміника написати програму через класс, яка складає сумму декількох валют та виводить у іншій.
Для простоти гривня, долар, евро, злотий
"""
from typing import Union


class Currency():
    exchange_rate = {
        "UAH": 36.74,
        "EUR": 0.93,
        "PLN": 4.42
    }

    def __init__(self, uah: Union[int, float], usd: Union[int, float], eur: Union[int, float], pln: Union[int, float]):
        self.uah = uah
        self.usd = usd
        self.eur = eur
        self.pln = pln

    def summary(self) -> str:
        return f"{self.uah:.2f} UAH, {self.usd:.2f} USD, {self.eur:.2f} EUR, {self.pln:.2f} PLN."

    def eqvival(self, rate: str) -> str:
        if rate == "USD":
            return f"У вас {self.rate_to_USD():.2f} USD"
        elif rate == "UAH":
            result = self.rate_to_USD() * self.exchange_rate["UAH"]
            return f"У вас {result:.2f} UAH"
        elif rate == "EUR":
            result = self.rate_to_USD() * self.exchange_rate["EUR"]
            return f"У вас {result:.2f} EUR"
        elif rate == "PLN":
            result = self.rate_to_USD() * self.exchange_rate["PLN"]
            return f"У вас {result:.2f} PLN"
        else:
            return "Помилка операції."

    def rate_to_USD(self) -> Union[float, int]:
        return self.usd + self.uah / self.exchange_rate['UAH'] + self.eur / self.exchange_rate['EUR'] + self.pln / \
            self.exchange_rate['PLN']

    def __ge__(self, other: 'Currency') -> str:
        if self.usd == other.usd and self.uah == other.uah and self.eur == other.eur and self.pln == other.pln:
            return "еквіваленті рівні"
        else:
            return "еквіваленто не рівні"

    def __add__(self, other: 'Currency') -> 'Currency':
        return Currency(self.uah + other.uah, self.usd + other.usd, self.eur + other.eur, self.pln + other.pln)


my_saving = Currency(37, 100, 200, 100)
your_saving = Currency(37, 100, 200, 100)
new_saving = my_saving.__add__(your_saving)

assert my_saving.summary() == "37.00 UAH, 100.00 USD, 200.00 EUR, 100.00 PLN."
assert my_saving.uah == 37.00
assert my_saving.eqvival("USD") == "У вас 338.69 USD"
assert new_saving.summary() == '74.00 UAH, 200.00 USD, 400.00 EUR, 200.00 PLN.'




"""
my_saving = Currency(33, 100, 200, 100)# 4 наших валюти
my_saving.summary() - виводить мій банк в різних валютах як є
my_saving.UAH - скільки окремої валюти
my_saving.eqvival("UAH") - 33, 100, 200, 100 - загалом в гривнях\чи інших з 4
my_saving == your_saving - true якщо сумми в еквіваленті рівні
my_saving + your_saving ...."""
