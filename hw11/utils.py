import json


def get_curr_course(path="data/currency_course.json"):
    """
    Функція витягує з файлу купівлю валют.
    :param path: шлях, де знаходиться json з курсом валют
    :return: дані з файлу
    """
    with open(path, 'r') as file:
        return json.load(file)


def get_bank(path="data/bank.json"):
    """
    Функція витягує з файлу наявні валюти з банку.
    :param path: шлях, де знаходиться json з банком
    :return: дані з файлу
    """
    with open(path, 'r') as file:
        return json.load(file)


def cal_cell_course(cource, mul):
    """
    Функція вичисляє поточний продаж валют за допомогою коефіцієнту.
    :param cource: курс купівлі валют
    :param mul: коефіцієнт за яким вичисляється продаж
    :return: курс валют купівлі та продажу.
    """
    for curr_name in cource.keys():
        for sec_curr, rate in cource[curr_name]["buy"].items():
            cource[curr_name]["sell"].update({sec_curr: round(rate * (1 + mul), 2)})
    return cource


def exchange(amount, cource, operation, old_curr, new_curr):
    """
    Функція вироховує обмін валют.
    :param amount: введена сумма користувача
    :param cource: поточний курс
    :param operation: вид угоди
    :param old_curr: валюта, яка була введена
    :param new_curr: валюта, яка буде отримана
    :return: гроші, по отриманому курсу
    """
    return amount * cource[old_curr][operation][new_curr]


# TODO написати бек і переввезти минуле значення при цьому зберігаючи старе
# TODO якщо помилиться користувач то ввести знову.....
# TODO протестувати цю рекурсію... чи працює вона - не коректно
# TODO написати ітераційний розв'язовак

def input_data(data, num=0, result=[], count=0):
    """
    Функція виводить запитання, де користувач повинен написати кількіс
    :param data: інформація де користувач повинен ввести дані по пунктах
    :param num:
    :param result:
    :param count:
    :return:
    """
    # result = []
    for index, i in enumerate(data[num:], num):
        if i["question"]:
            input_value = input(i["question"])
            if input_value == "reset":
                return input_data(data)
            elif input_value == "back":
                return input_data(data, 0, result[:len(result) - 1 - count]) \
                    if index == 0 else input_data(data, index - 1 - count,
                                                  result[:len(result) - 1 - count])  # index = 3
            if i["func"]:
                input_value = float(input_value)
            result.append(input_value)
        else:
            result.append(i["fixture"])
            count += 1
        print(result)
    return result


"""def input_data(data, num=0, result=[], count=0):
    # result = []
    while num < len(data):
            if data[num]["question"]:
                input_value = input(data[num]["question"])
                if input_value == "reset":
                    return input_data(data)
                elif input_value == "back":
                    if count == 0:
                        num -= 1
                        result = result[:len(result) - 1]
                        continue
                    else:
                        num = num - count - 1
                        result = result[:len(result) - count - 1]
                        count = 0
                        continue
                if data[num]["func"]:
                    input_value = float(input_value)
                result.append(input_value)
                num += 1
            else:
                result.append(data[num]["fixture"])
                num += 1
                count += 1
            print(result)
    return result"""


def table_exchange(cource):
    """
    Функція виводить табло у термінал
    :param cource: поточний курс
    :return:
    """
    print(f"{'':*^17}")
    print(f"{'* BUY':<5}{'':6}{'SELL *':>5}")
    print(f"*{cource['UAH']['buy']['EUR']:<5.2f}{'EUR':^5}{cource['UAH']['sell']['EUR']:>5.2f}*")
    print(f"*{cource['UAH']['buy']['USD']:<5.2f}{'USD':^5}{cource['UAH']['sell']['USD']:>5.2f}*")
    print(f"*{cource['UAH']['buy']['PLN']:<5.2f}{'PLN':^5}{cource['UAH']['sell']['PLN']:>5.2f}*")
    print(f"{'':*^17}")
    return

# TODO зробити валютний запас банку
def issuance_of_currency(input, dollar, bank, op):
    """

    :param input:
    :param dollar:
    :param bank:
    :param op:
    :return:
    """
    if op == 'sell':
        for key in bank:
            if bank[key] != 0 and float(key) <= dollar:
                bank[key] -= 1
                dollar -= float(key)
                dollar = issuance_of_currency(dollar, bank, op)
    else:
        for key in bank:
            if input != 0 and float(key) <= input:
                bank[key] += 1
                input -= float(key)
                input = issuance_of_currency(input, 0, bank, op)
    with open("data/bank.json", "w", encoding="utf-8") as file:
        json.dump(bank, file)
    return dollar


# TODO доробити коректний вивід
def result(op, amount, new_curr, new_ammount, old_curr):
    """
    Функція повинна вивести скількі користувач отримав валют при обмінні, також валютний запас банку
    :param amount: введена сумма користувача
    :param cource: поточний курс
    :param operation: вид угоди
    :param old_curr: валюта, яка була введена
    :param new_curr: валюта, яка буде отримана
    :return: вивід у консоль результату родоти обмінника
    """
    return f"we will {op} {amount} {new_curr} for {new_ammount} {old_curr}"
