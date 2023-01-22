"""
Написати функцію яка пертворює вкладений список на плоский

50 балів
"""


def flatten(array):
    flat = []

    def deep(array, flat):
        for i in range(len(array)):
            if type(array[i]) == list:
                deep(array[i], flat)
            else:
                flat.append(array[i])
        return flat

    return deep(array, flat)


assert flatten([1,[2], [3,[6]]]) == [1, 2, 3, 6]
assert flatten([[[[]]]]) == []
assert flatten([[[''],[[5],1]]]) == ['', 5, 1]
