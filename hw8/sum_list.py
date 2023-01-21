"""знайти сумму всіх чисел в лісті

Спойлер:
якщо ви уважно почитали документацію до типу флоат, то можливо умова на тип для вас не така і складна
Якщо ні - if-else.....
"""
import math


def sum_list(array):
    sum = 0
    for i in range(len(array)):
        if type(array[i]) == str:
            if str(math.fabs(float(array[i]))).replace('.', '', 1).isdigit():
                array[i] = float(array[i])
            else:
                print('У лісті є строки!')
                break
        sum += array[i]
    if str(sum).endswith('.0'):
        sum = int(sum)
    return sum


assert sum_list([1, 2, "1"]) == 4
assert type(sum_list([1, 2, "1"])) == int
assert sum_list([1, 2, "1", "1.1"]) == 5.1
assert type(sum_list([1, 2, "1", "1.1"])) == float
assert sum_list([1, 2, "1", "-1.0"]) == 3
assert type(sum_list([1, 2, "1", "-1.0"])) == int
