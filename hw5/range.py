"""
2)  користувач вводить числа a, b  вивиести всі цілі числа між ними
"""

a = int(input(f"Введіть a: "))
b = int(input(f"Введіть b: "))
line = ''
if a + 1 < b:
    for i in range(a + 1, b, 1):
        line += f" {i}"
    print(line)
elif a > b + 1:
    for i in range(b + 1, a, 1):
        line += f" {i}"
    print(line)
else:
    print("Між a та b немає цілих чисел")
