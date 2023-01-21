"""
згенерувати матрицю chesboard_pattern

"""

# def chesboard_pattern(width, height):
#     chesboard = []
#     for i in range(height):
#         pattern = []
#         for j in range(width):
#             if i % 2 == 0:
#                 if j % 2 == 0:
#                     pattern.append(0)
#                 else:
#                     pattern.append(1)
#             else:
#                 if j % 2 == 0:
#                     pattern.append(1)
#                 else:
#                     pattern.append(0)
#         chesboard.append(pattern)
#     return chesboard

"""
взяли задачку в лоб. В принципі вона розєязана але можна було б хитріше. Через те що 1 if значно легше читається.
"""
def chesboard_pattern(width, height):
    chesboard = []
    line = [0 if index % 2 == 0 else 1 for index in range(width+1)]
    for row in range(height):
        if row % 2:
            pattern = line[1:]
        else:
            pattern = line[:-1]
        chesboard.append(pattern)
    return chesboard

assert chesboard_pattern(2, 2) == [[0, 1], [1, 0]]
assert chesboard_pattern(4, 3) == [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
