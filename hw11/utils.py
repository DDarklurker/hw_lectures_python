import json
from typing import  Union

def get_curr_course(path="data/currency_course.json") -> dict:
    """
    Функція витягує з файлу купівлю валют.
    :param path: шлях, де знаходиться json з курсом валют
    :return: дані з файлу
    """
    with open(path, 'r') as file:
        return json.load(file)


def get_bank(path="data/bank.json") -> dict:
    """
    Функція витягує з файлу наявні валюти з банку.
    :param path: шлях, де знаходиться json з банком
    :return: дані з файлу
    """
    with open(path, 'r') as file:
        return json.load(file)


def cal_cell_course(cource: dict, mul: Union[int, float]) -> dict:
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


def exchange(amount: Union[int, float], cource: dict, operation: str, old_curr: str, new_curr: str) -> Union[
    int, float]:
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


def input_data(data: dict, num=0, result=[], count=0) -> list:
    """
    Функція виводить запитання, де користувач повинен написати: сумму, операцію, види валют.
    :param data: інформація де користувач повинен ввести дані по пунктах
    :param num: рахує кільксть правильних відповідей
    :param result: список відповідей користувача
    :param count: рахує скільки пунктів було пропущено (приховані пункти)
    :return: список відповідей користувача
    """
    for index, i in enumerate(data[num:], num):
        if i["question"]:
            input_value = input(i["question"])
            if input_value == "reset":
                return input_data(data)
            elif input_value == "back":
                return input_data(data, 0, result[:len(result) - 1 - count]) \
                    if index == 0 else input_data(data, index - 1 - count,
                                                  result[:len(result) - 1 - count])
            if i["func"]:
                input_value = float(input_value)
            result.append(input_value)
        else:
            result.append(i["fixture"])
            count += 1
        print(result)
    return result


def table_exchange(cource: dict) -> None:
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
    pass


# TODO зробити валютний запас банку
def issuance_of_currency(curr: Union[int, float], new_curr: Union[int, float], bank: dict, op: str) -> Union[
    int, float]:
    """
    Функція видає або приймає наявні купюри з банку, та вираховує решту, якщо цих банкнот немає.
    :param curr: 
    :param new_curr: сума грошей 
    :param bank: кількості валют у банку
    :param op: вид торгівлі
    :return: решту, на суму яких не було банкнот
    """
    if op == 'sell':
        for key in bank:
            if bank[key] != 0 and float(key) <= new_curr:
                bank[key] -= 1
                new_curr -= float(key)
                new_curr = issuance_of_currency(new_curr, bank, op)
    else:
        for key in bank:
            if curr != 0 and float(key) <= curr:
                bank[key] += 1
                curr -= float(key)
                curr = issuance_of_currency(curr, 0, bank, op)
    with open("data/bank.json", "w", encoding="utf-8") as file:
        json.dump(bank, file)
    return new_curr


# TODO доробити коректний вивід
def result(op: str, amount: Union[float, int], new_curr: str, new_ammount: Union[int, float], old_curr: str) -> str:
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
