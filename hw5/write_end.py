"""
1) У нескінченному циклі користувач вводить числа.

 Коли ви пишете слово end цикл припиняється і програма видає сумму числел.
"""
count = 0
while True:
    load = input(f"Введіть ціле число: ")
    if load.isdigit():
        count += int(load)
    if load == "end":
        break
print(f"Сумма числел {count}")
