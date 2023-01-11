"""
написати програму яка перетворює список на строку
"""


def list_to_string(array):
    list = ''
    for i in range(len(array)):
        list += str(array[i])
    return list


test1 = ["l", "i", "s", "t"]
test2 = ["l", "i", "s", "t", 5, 1.1]
print(list_to_string(test1))
print(list_to_string(test2))
assert list_to_string(["l", "i", "s", "t"]) == "list"
assert list_to_string(["l", "i", "s", "t", 5, 1.1]) == "list51.1"

