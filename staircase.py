from functools import cache

@cache
def staircase(n):
    if n == 2:
        return 2
    if n <= 1:
        return 1
    return staircase(n-1) + staircase(n-2) + staircase(n-3)

if __name__ == "__main__":  
    assert staircase(1) == 1
    assert staircase(2) == 2
    assert staircase(3) == 4
    assert staircase(4) == 7 #2
    assert staircase(5) == 13 #5
    print('ok')