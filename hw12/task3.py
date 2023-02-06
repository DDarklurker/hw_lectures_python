#task3
"""
В відриві від проекту обміника написати програму через класс, яка складає сумму декількох валют та виводить у іншій.
Для простоти гривня, долар, евро, злотий
"""
from typing import Union


class Currency():
    exchange_rate = {
        "USD": {
            "UAH": 36.74,
            "EUR": 0.93,
            "PLN": 4.42
        },
        "EUR":{

        },
        "PLN":{

        }
              }
    pass

    def __init__(self, uah: Union[int,float], usd: Union[int,float], eur: Union[int,float], pln: Union[int,float]):
        self.uah = uah
        self.usd = usd
        self.eur = eur
        self.pln = pln

    def summary(self) -> str:
        return f"{self.uah:.2f} UAH, {self.usd:.2f} USD, {self.eur:.2f} EUR, {self.pln:.2f} PLN."
    def eqvival(self, rate:str) -> Union[int,float]:
        if rate == "USD":
            return  f"  {self.uah / 26} USD: {self.usd} EUR: {self.eur  / 29} PLN: {self.pln / 5.5}"




my_saving = Currency(33, 100, 200, 100)
print(my_saving.summary())
print(my_saving.uah)

"""
my_saving = Currency(33, 100, 200, 100)# 4 наших валюти
my_saving.summary() - виводить мій банк в різних валютах як є
my_saving.UAH - скільки окремої валюти
my_saving.eqvival("UAH") - 33, 100, 200, 100 - загалом в гривнях\чи інших з 4
my_saving == your_saving - true якщо сумми в еквіваленті рівні
my_saving + your_saving ...."""