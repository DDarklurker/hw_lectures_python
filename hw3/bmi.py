"""
Написати програму, яка розраховує індекс маси тіла
якщо користувач може ввести значення у різних системах виміру.
"""
height = input("Введіть свій зріст (m/cm)(за замовченням m):")  # input height
weight = input("Введіть свою вагу (kg/lb)(за замовченням kg):")  # input weight
sep1 = height.find(" ")  # where the number ends
sep2 = weight.find(" ")
if sep1 != -1 and sep2 != -1:
    h_val = float(height[0:sep1])  # my number
    w_val = float(weight[0:sep2])
    if height.endswith("cm"):  # when cm
        h_val = h_val / 100
    if weight.endswith("lb"):  # when lb
        w_val = w_val / 2.2

    bmi = w_val / (h_val ** 2)  # result index
    print(f"Ваш індекс маси тіла дорівнює: {bmi:.1f}")
else:
    print("Введіть коректно одиницю вимірювання.")
