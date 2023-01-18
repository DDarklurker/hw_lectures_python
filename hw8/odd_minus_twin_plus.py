"""
В бескінечном уциклі ви вводите числа. кожне чьотне число додається до загальної суми. кожне нечьотне віднімається.
при написанні слова end цикл зупиняється і видається сума.

"""
sum = 0
while True:
    number = (input("Введіть чьотне або нечьотне число: "))
    if number.isdigit():
        number = int(number)
        if number % 2 == 0:
            sum += number
        else:
            sum -= number
    else:
        if number == 'end':
            break
        else:
            print('Не коректно введені дані, спробуйте ще!')

print(sum)
