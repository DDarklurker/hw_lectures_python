"""
В бескінечном уциклі ви вводите числа. кожне чьотне число додається до загальної суми. кожне нечьотне віднімається.
при написанні слова end цикл зупиняється і видається сума.

"""
sum = 0
while True:
    number = (input("Введіть чьотне або нечьотне число: "))
    if number.isdigit() or number.replace('-', '', 1).isdigit():
        number = int(number)
        sum = sum + number if number % 2 == 0 else sum - number

    else:
        if number == 'end':
            break
        else:
            print('Не коректно введені дані, спробуйте ще!')
print(sum)
