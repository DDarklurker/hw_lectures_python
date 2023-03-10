"""
2) Облаштувати Переведення валют в обмінику через словник(приклад структури на гітхабі)
3) Загорнути код що робить конвертацію та розраховує курс продажу в фунції.
4) В словнику дані кількість купюр кожного номіналу. Зробити фунцію яка перевіряє чи вистачить коштів чи купюр щоб обміняти гроші..

"""

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


def your_dollars(valual_uah):
    return valual_uah // corency_courses['UAH']['sell']['USD']


def your_payment(valual_uah):
    return valual_uah % corency_courses['UAH']['sell']['USD']


def currency_in_exchange(exchange):
    dollars = your_dollars(exchange)

    def exchange(dollar):
        for key in bank:
            if bank[key] != 0 and key <= dollar:
                bank[key] -= 1
                dollar -= key
                dollar = exchange(dollar)
        return dollar

    differ = exchange(dollars)
    if differ != dollars:
        print(f"На наявні купюри ви отримаєте {dollars - differ:>6} дол")
        print(f"Ваша решта {your_payment(val_uah) + (differ * corency_courses['UAH']['sell']['USD']):>25} грн")
        print(f"В обміннику {bank} валют")
    else:
        print(f"На жаль в обмінику закінчилась валюта, ваша решта {val_uah:>7} грн")
        print(f"В обміннику {bank} валют")
    return


while True:
    val_uah = (input("Введіть кількість гривень, яку ви хочете продати (для виходу введіть end): "))
    if val_uah.endswith("end"):
        break
    else:
        try:
            val_uah = float(val_uah)
            if val_uah < 0:
                print("Не вірне значення, спробуйде ще!")
                continue
            currency_in_exchange(val_uah)
        except ValueError:
            print("Не вірна операція, спробуйде ще!")
