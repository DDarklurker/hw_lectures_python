# 1)Зменшити складність алгоритму

def chessboard_pattern_new(width, height):
    chessboard = []
    for i in range(height):
        pattern = [int(j % 2 != i % 2) for j in range(width)] # Перевіряємо на інверсію  та переводимо boolean у int та записуємо у шаблон
        chessboard.append(pattern)
    return chessboard


assert chessboard_pattern_new(4,5) == [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
