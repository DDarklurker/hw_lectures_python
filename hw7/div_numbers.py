start = 8
end = 15

denominator = [2, 3]
div_count = []  # [[8,10], [3, 12]]

# ДЗ довести до кінця цю програму

for num in range(start, end):
    for denom_index in range(len(denominator)):
        if num % denominator[denom_index] == 0:
            if len(div_count) <= denom_index:
                div_count.append(list())
            div_count[denom_index].append(num)

for num in div_count:
    print(*num[0:10])

