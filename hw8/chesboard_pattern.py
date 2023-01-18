"""
згенерувати матрицю chesboard_pattern

"""


def chesboard_pattern(width, height):
    chesboard = []
    for i in range(height):
        pattern = []
        for j in range(width):
            if i % 2 == 0:
                if j % 2 == 0:
                    pattern.append(0)
                else:
                    pattern.append(1)
            else:
                if j % 2 == 0:
                    pattern.append(1)
                else:
                    pattern.append(0)
        chesboard.append(pattern)
    return chesboard


assert chesboard_pattern(2, 2) == [[0, 1], [1, 0]]
assert chesboard_pattern(4, 3) == [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
