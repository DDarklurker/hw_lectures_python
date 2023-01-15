
corency_courses = {
    "UAH": {
        "buy": {
            "USD": 40,
            "EUR": 36,
            "PLN": 6
        },
        "sell": {}}
}
def sell_value(your_course):
    return your_course + (your_course * 0.05)


for i in corency_courses["UAH"]["buy"].keys():
    corency_courses["UAH"]["sell"][i] = sell_value(corency_courses["UAH"]["buy"][i])

bank = {100: 100, 50: 20, 10: 10, 1: 0, 5: 0}

print(f"{'':*^17}")
print(f"{'* BUY':<5}{'':6}{'SELL *':>5}")
print(f"*{corency_courses['UAH']['buy']['EUR']:<5.2f}{'EUR':^5}{corency_courses['UAH']['sell']['EUR']:>5.2f}*")
print(f"*{corency_courses['UAH']['buy']['USD']:<5.2f}{'USD':^5}{corency_courses['UAH']['sell']['USD']:>5.2f}*")
print(f"*{corency_courses['UAH']['buy']['PLN']:<5.2f}{'PLN':^5}{corency_courses['UAH']['sell']['PLN']:>5.2f}*")
print(f"{'':*^17}")


def your_dollars(val_uah):
    return val_uah // corency_courses['UAH']['buy']['USD']


def your_payment(val_uah):
    return val_uah % corency_courses['UAH']['buy']['USD']

"""def currency_in_exhange(exchange):
"""
while True:
    val_uah = (input("Введіть кількість гривень, яку ви хочете продати (для виходу введіть end): "))
    if val_uah.endswith("end"):
        break
    else:
        try:
            val_uah = float(val_uah)
            print(f"Вашаша валюти {your_dollars(val_uah)} дол")
            print(f"Ваша решта {your_payment(val_uah):>7} грн")
        except ValueError:
            print("Не вірна операція, спробуйде ще!")

