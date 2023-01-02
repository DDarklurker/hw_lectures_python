"""
Написати програму, яка розраховує індекс маси тіла
якщо користувач може ввести значення у різних системах виміру.
"""
height = input("Введіть свій зріст (m/cm):")  # input height
weight = input("Введіть свою вагу (kg/lb):")  # input weight
sep1 = height.index(" ")  # where the number ends
sep2 = weight.index(" ")
h_val = float(height[0:sep1])  # my number
w_val = float(weight[0:sep2])
if height.endswith("cm"):  # when cm
    h_val = h_val / 100
if weight.endswith("lb"):  # when lb
    w_val = w_val / 2.2

bmi = w_val / (h_val ** 2)  # result index
print(f"Ваш індекс маси тіла дорівнює: {bmi:.1f}")
