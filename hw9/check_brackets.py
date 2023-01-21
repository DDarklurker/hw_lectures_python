"""
перевірити коректнсть дужок.
"""


def brackets(string):
    stack = []
    for i in string:
        if len(stack) == 0 and i == ')':
            return False
        if i == '(':
            stack.append(i)
        elif len(stack) != 0 and i == ')':
            stack.pop()
    return True



assert brackets("())") == False
assert brackets("())(") == False
assert brackets("(s(sss)sssssssssssssssssssssssssss)") == True
