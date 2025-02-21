def isBalanced(symbols):
    stack = []
    matcher = {')': '(', ']': '[', '}': '{'}
    ends=['(', '[', '{']
    
    for s in symbols:
        if s in ends:
            stack.append(s)
        else:
            if len(stack) == 0 or matcher[s] != stack.pop(): return False

    if len(stack) != 0: return False

    return True

if __name__ == '__main__':
    assert isBalanced('') == True
    assert isBalanced('()') == True
    assert isBalanced('()[]') == True
    assert isBalanced('([{}])') == True
    assert isBalanced('(') == False
    assert isBalanced(')') == False
    assert isBalanced('([)]') == False
    print('ok')