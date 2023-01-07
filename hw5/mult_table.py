"""
4*)Користувач вводить число від 6 до 16. Вивести таблицю множення на числа від n - 4  до n + 3(Як на зошитах).

 В d випадку з 6 від 2 до 9. 16 - від 12 до 19

"""
while True:
    num = int(input("Введіть число від 6 до 16: "))
    if 5 < num < 17:
        break
    print("Не правильне введення, спробуйте ще")
line = ''
for j in range(1, 11, 1):
    for i in range(num - 4, num, 1):
        line += f" {j:>3} x {i:>2} = {j * i:>3}"
    print(line)
    line = ''
print("\n")
for j in range(1, 11, 1):
    for i in range(num, num + 4, 1):
        line += f" {j:>3} x {i:>2} = {j * i:>3}"
    print(line)
    line = ''
