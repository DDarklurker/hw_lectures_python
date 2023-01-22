# task3
"""
На зірочку
написати фунцію переводу з римськох системи числення до десятичної
Асерти пишите самі.
"""
roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'M': 1000}


def verify(num):
    for i in num:
        isverify = False
        for key in roman_num.keys():
            isverify = True
        if not isverify:
            return False
    return True


def roman_to_num(num):
    number = 0
    if verify(num):
        for i in range(len(num) - 1):
            if roman_num.get(num[i]) < roman_num.get(num[i + 1]):
                number += (roman_num.get(num[i + 1]) - roman_num.get(num[i]))
                i += 1
            elif i+1 == len(num) - 1:
                return number + (roman_num.get(num[i + 1]) + roman_num.get(num[i]))
            else:
                number += roman_num.get(num[i])
        return number
    else:
        return "Введено не правильне значееня"



assert roman_to_num('VII') == 7
assert roman_to_num('XL') == 40
assert roman_to_num('CI') == 101
assert roman_to_num('MLM') == 1950
