import json


def get_curr_course(path="data/currency_course.json"):
    with open(path, 'r') as file:
        return json.load(file)


def get_bank(path="data/bank.json"):
    with open(path, 'r') as file:
        return json.load(file)


# TODO має бути можливисть робити знижку чи змінною чи манімуляцією з mul
def cal_cell_course(cource, mul):
    for curr_name in cource.keys():
        for sec_curr, rate in cource[curr_name]["buy"].items():
            cource[curr_name]["sell"].update({sec_curr: round(rate * (1 + mul), 2)})
    return cource


def exchange(amount, cource, operation, old_curr, new_curr):
    return amount * cource[old_curr][operation][new_curr]


# TODO написати бек і переввезти минуле значення при цьому зберігаючи старе
# TODO якщо помилиться користувач то ввести знову.....
"""
Якось зманіпулювати перебігом ципклу, і повернутись на одну ітерацію назад +
while i < len(data):
for {i =0, i++, i < len(array)}{
    array[i]
}

while index < len(data):
do tms
if back()
index -1 і не зробив аппенд

рекрсивний ... .зберегти стан фунції ...  


"""


# TODO протестувати цю рекурсію... чи працює вона - не коректно
# TODO написати ітераційний розв'язовак

def input_data(data, num=0, result=[], count=0):
    # result = []
    for index, i in enumerate(data[num:]):
        if i["question"]:
            input_value = input(i["question"])
            if input_value == "reset":
                return input_data(data)
            elif input_value == "back":
                return input_data(data, index - 1 - count, result[:len(result) - 1 - count])  # index = 3
            if i["func"]:
                input_value = float(input_value)
            result.append(input_value)
        else:
            result.append(i["fixture"])
            count += 1
        print(result)
    return result
