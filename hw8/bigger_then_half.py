"""
Знайти число яке більше 50% елементів списку.
"""

def bigger_then_half(array):
    one_element_persent = 100 / len(array)
    count = 0
    for i in range(len(array)):
        print(array[i])
        if one_element_persent > 50:
            return array[i]
        count += one_element_persent

print(bigger_then_half([1, 2, 3]))
assert bigger_then_half([1, 2, 3]) == 3# bigger then 2 out of 3
assert bigger_then_half([1, 2, 2, 3]) == 3# bigger then 3 out of 4
assert bigger_then_half([1, 1, 1, 2, 3]) == 2# bigger then 3 out of 5