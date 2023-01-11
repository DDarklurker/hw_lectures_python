"""
Написати програму яка знаходить друге найменше число в списку.
1) з використанням методів списків, та вбудованих функцій
2) без використання методів списків
"""


def second_smallest(array):
    array.sort()
    return array[1]


def second_smallest(array):
    first_min = array[0]
    for i in range(len(array)):
        if first_min > array[i]:
            first_min = array[i]
    for i in range(len(array)):
        if first_min == array[0]:
            second_min = array[1]
        else:
            second_min = array[0]
    for i in range(len(array)):
        if second_min > array[i] and first_min != array[i]:
            second_min = array[i]
    return second_min


print(second_smallest([1, 2, 2, 3]))
print(second_smallest([-1, 10, -2, 2]))
assert second_smallest([1, 2, 2, 3]) == 2
assert second_smallest([-1, 10, -2, 2]) == -1
