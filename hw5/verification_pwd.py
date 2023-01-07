"""
0)  Пользователь воодит пароль - ми кажемо чи беспечний цей пароль чи ні. Пароль беспечний, якщо він джовший за 12
символів. Має 1 букву в верхньому регистрі, 1 в нижньому, 1 цифру, 1 спецсимвол(?/!@)
"""

your_pwd = input(f"Введіть пароль для перевірки: ")
spec_ch = "?/!@"
has_spec = False
has_lower = False
has_upper = False
has_range = False
has_int = False
for i in range(len(your_pwd)):
    if your_pwd[i] in spec_ch:
        has_spec = True
    if your_pwd[i].lower() in your_pwd[i]:
        has_lower = True
    if your_pwd[i].upper() in your_pwd[i]:
        has_upper = "True"
    if your_pwd[i].isdigit():
        has_int = True
if len(your_pwd) >= 12:
    has_range = True
if has_lower and has_range and has_upper and has_int:
    print("Пароль безпечний")
else:
    print("Пароль не безпечний")
