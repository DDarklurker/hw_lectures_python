"""
згенерувати квадратну матрицю 'око' - всі значення 0-лі а по діагоналі 1ки

"""


def eye_matrix(size):
    eye = []
    count = 0
    for i in range(size):
        matrix = []
        for j in range(size):
            if count == j:
                matrix.append(1)
            else:
                matrix.append(0)
        eye.append(matrix)
        count += 1
    return eye


print(eye_matrix(3))
print(eye_matrix(4))

assert eye_matrix(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
assert eye_matrix(4) == [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
