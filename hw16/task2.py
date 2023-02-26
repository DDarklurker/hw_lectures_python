#Написати таку функцію
import re

def inc_str(string):
    search = re.search(r'\d+$', string)
    if search is None:
        return string + "1"
    else:
        num = int(search.group()) + 1
        return re.sub(r'\d+$', str(num).zfill(len(search.group())), string)

print(inc_str("fo2obar001019"))
print(inc_str("foobar001019"))
print(inc_str("foobar"))
print(inc_str("foobar9"))
assert inc_str("foobar") == "foobar1"
assert inc_str("foobar0") == "foobar1"
assert inc_str("foobar00") == "foobar01"
assert inc_str("foobar00001") == "foobar00002"
assert inc_str("foobar0010") == "foobar0011"
assert inc_str("foobar00101") == "foobar00102"