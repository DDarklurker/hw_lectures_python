"""
Написати програму яка знаходить друге найменше число в списку.
1) з використанням методів списків, та вбудованих функцій
2) без використання методів списків
"""


def second_smallest(array):
    array.sort()
    return array[1]
test1 = [1, 2, 2, 3]
test2 = [-1, 10, -2, 2]





print(second_smallest([1, 2, 2, 3]))
print(second_smallest([-1, 10, -2, 2]))
assert second_smallest([1, 2, 2, 3]) == 2
assert second_smallest([-1, 10, -2, 2]) == -1
