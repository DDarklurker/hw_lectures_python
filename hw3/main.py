"""
Написати програму яка розраховує за курсом, скільки грошей має отримати людина за свою валюту
Курс валют - done
ввод значення
Розрахунок отриманої валюти
Вивод результату
uah->usd
usd->uah
"""

AUH_USD = 40.123
AUH_EUR = 41.123
AUH_GBP = 45.120
# round up to hundredths of buy
AUH_USD = float(f"{AUH_USD:.2f}")
AUH_EUR = float(f"{AUH_EUR:.2f}")
AUH_GBP = float(f"{AUH_GBP:.2f}")
# sales currencies
USD_SELL = AUH_USD + AUH_USD * 5 / 100
EUR_SELL = AUH_EUR + AUH_EUR * 5 / 100
GBP_SELL = AUH_GBP + AUH_GBP * 5 / 100
# round up to hundredths of sales
USD_SELL = float(f"{USD_SELL:.2f}")
EUR_SELL = float(f"{EUR_SELL:.2f}")
GBP_SELL = float(f"{GBP_SELL:.2f}")

# create a stand EURO, USD, GBP
print(f"{'':*^25}")
print(f"{'':*^2}{'BUY':^7}{'*'}{'':^5}{'*'}{'SELL':^7}{'':*^2}")
print(f"{'':*^2}{AUH_EUR:^7}{'*'}{'EUR':^5}{'*'}{EUR_SELL:^7}{'':*^2}")
print(f"{'':*^2}{AUH_USD:^7}{'*'}{'USD':^5}{'*'}{USD_SELL:^7}{'':*^2}")
print(f"{'':*^2}{AUH_GBP:^7}{'*'}{'GBP':^5}{'*'}{GBP_SELL:^7}{'':*^2}")
print(f"{'':*^25}")
buy_sell = input("Виберіть операцію (buy/sell): ")
if buy_sell.endswith("sell"):
    # input your GRN
    val_usd = float(input("Кількість гривень: "))
    # your USD
    result = int(val_usd / USD_SELL)
    # your submission
    remain = val_usd % USD_SELL
    # round up to hundredths
    remain = float(f"{remain:.2f}")
    # result
    print(f"Ваша конвертація{result:>7}\nВаша решта{remain:>16} грн")
elif buy_sell.endswith("buy"):
    # input your USD
    val_usd = float(input("Кількість доларів: "))
    # your UAH
    result = float(val_usd * AUH_USD)
    # result
    print(f"Ваша конвертація{result:>7.2f} грн")
else:
    print("Не вірна операція!")

