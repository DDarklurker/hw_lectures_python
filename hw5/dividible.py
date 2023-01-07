"""
 Вивести всі числа між числами a, b , 1 < (a,b) < 200
 що діляться на 2, 3, 4, 5, 6. Кожна группа має бути виведена окремою групою, зі строкою не більше 10 чисел
"""

a = int(input(f"Введіть a між 1 та 200: "))
b = int(input(f"Введіть b між 1 та 200: "))
line = ''
count = 0
if 0 < a < 200 and 0 < b <= 200:
    if a + 1 < b:
        for j in range(2, 7, 1):
            for i in range(a + 1, b, 1):
                if count == 10:
                    break
                if i % j == 0:
                    line += f" {i},"
                    count += 1
            print(f"Dividible by {j}:{line}")
            line = ''
            count = 0
    elif a > b + 1:
        for j in range(2, 7, 1):
            for i in range(b + 1, a, 1):
                if count == 10:
                    break
                if i % j == 0:
                    line += f" {i},"
                    count += 1
            print(f"Dividible by {j}:{line}")
            line = ''
            count = 0
    else:
        print("Між a та b не має цілих чисел")
else:
    print("Вкажіть коректний діапазон")
