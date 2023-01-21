"""
складати і скорочуавти раціональні дроби .
"""
import math

"""
окей працює, був би це код в продакшені - я б сказав все переробити,
якби ви почитали документацію по типу флоат ви би могли зробити програму майже однострочніком.

float.as_integer_ratio() чи щось на шквалт рітко вживане, але доки варто читати, щоб знаи про існування можливостей.
"""
def divide(a, b):
    c = []
    if len(a) != 2 or len(b) != 2:
        print('Вказані не вірні значення.')
        return None
    if a[1] == 0 or b[1] == 0:
        return None
    if a[1] != b[1]:
        c.append(a[0] * b[1] + a[1] * b[0])
        c.append(a[1] * b[1])
    else:
        c.append(b[0] + a[0])
        c.append(a[1])

    def rational(num):
        if num[0] == -2 or num[0] == 2:
            if num[1] % 2 == 0:
                num[1] = num[1] // int(math.fabs(num[0]))
                num[0] = num[0] // int(math.fabs(num[0]))
            return num
        else:
            index = int(math.ceil(num[0] // 2))
        for i in range(2, index + 1, 1):
            if num[0] == 1:
                return num
            if num[0] % i == 0:
                num[1] = num[1] // i
                num[0] = num[0] // i
                num = rational(num)
        return num

    c = tuple(rational(c))
    return c


"1/8 + 3/16"
assert divide((1, 8), (3, 8)) == (1, 2)  # 1\8 + 3\8 = 4\8 = 1\2
assert divide((1, 0), (3, 8)) == None  # 1\0 + 3\8 - not valid
