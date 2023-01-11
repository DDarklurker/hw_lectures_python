"""
Із списку, цілі числа з'єднати в одне число
варіант із зірочкою - заборонено переведення із строкового в числовий тип і навпаки
"""


def join_ints(my_list):
    result = ''
    for i in range(len(my_list)):
        if str(my_list[i]).isdigit():
            result += str(my_list[i])
    result = int(result)
    return result


def join_ints(my_list):
    result = 0
    count = 0

    for i in range(len(my_list) - 1, -1, -1):
        if (type(my_list[i])) is int:
            result += my_list[i] * (10 ** count)
            count += 1

    return result


print(join_ints([1, 2, 3]))
print(join_ints([1, "foo", 2.5, 1, 1, 4, "abr", 3]))
assert join_ints([1, 2, 3]) == 123
assert join_ints([1, "foo", 2.5, 1, 1, 4, "abr", 3]) == 11143
