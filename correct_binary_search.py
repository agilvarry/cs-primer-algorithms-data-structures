def search(arr, n):
    if len(arr) == 0: return -1
    i = 0
    j = len(arr)-1
    while i <= j:
        if arr[i] == n: return i
        elif arr[j] == n: return j
        
        m = ((j-i)//2) +i
        if arr[m] == n: return m
        if arr[m] < n: i = m+1
        else: j = m-1
    return -1

if __name__ == "__main__":
    assert search([], 1) == -1
    assert search([1], 1) == 0
    assert search([0], 0) == 0

    assert search([0,1,2], 1) == 1
    
    assert search([0,1,2,3,4], 1) == 1
    assert search([0,1,2,3,4], 5) == -1
    assert search([0,1,2,3,4], 3) == 3
    
    assert search([-4, -1, 0, 3, 4, 69, 3421], -4) == 0
    assert search([-4, -1, 0, 3, 4, 69, 3421], 78) == -1
    assert search([-4, -1, 0, 3, 4, 69, 3421], 3421) == 6
    assert search([-4, -1, 0, 3, 4, 69, 3421], 0) == 2
    assert search([-4, -1, 0, 3, 4, 69, 3421], 69) == 5
    
    print('ok')
