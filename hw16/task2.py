#Написати таку функцію
import re

def inc_str(string):
    search = re.search(r'\d+$', string)
    if search is None:
        return string + "1"
    else:
        num = int(search.group()) + 1
        num_len = len(search.group())
        num_zero = ""
        for i in range(num_len - len(str(num))):
            num_zero += "0"
        return string[:-num_len] + num_zero + str(num)

print(inc_str("1fo2obar"))
print(inc_str("fo2obar"))
print(inc_str("fo2obar9"))
print(inc_str("foobar001019"))
print(inc_str("foobar"))
print(inc_str("foobar9"))
assert inc_str("foobar") == "foobar1"
assert inc_str("foobar0") == "foobar1"
assert inc_str("foobar00") == "foobar01"
assert inc_str("foobar00001") == "foobar00002"
assert inc_str("foobar0010") == "foobar0011"
assert inc_str("foobar00101") == "foobar00102"