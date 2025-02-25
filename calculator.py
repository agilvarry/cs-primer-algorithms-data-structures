"""
scope:
 - assume fully parenthesized, and valid
 - assume single digit integers
 - support +, -

 s = []
 for ch in expr:
 if digit: push equivalent int to stack
 if op: push equivalent fuction to stack
 if ')':
    pop last 3 values from sack,eval, push res to stack
else:  
    continue

"""
def calculator(expr):
    return 0

if __name__ == '__main__':

    assert calculator("(1 + (1 - 1))") == 1
    assert calculator("(1 - (2 - 3))") == 2