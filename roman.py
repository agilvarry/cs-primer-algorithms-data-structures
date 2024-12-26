

def roman(n=2421):
    M = n // 1000
    print(M)
    n = n%1000
    H = n //100
    n = n%100
    print(H)
    T = n //10
    n= n%10
    print(T)
    print(n)
    return ''

if __name__ == "__main__":  
    roman()
    # assert roman(39) == 'XXXIX'
    # assert roman(246) == 'CCXLVI'
    # assert roman(789) == 'DCCLXXXIX'
    # assert roman(2421) == 'MMCDXX'
    
    # assert roman(160) == 'CLX'
    # assert roman(207) == 'CCVII'
    # assert roman(1009) == 'MIX'
    # assert roman(1066) == 'MLXVI'
    
    # assert roman(1776) == 'MDCCLXXVI'
    # assert roman(1918) == 'MCMXVIII'
    # assert roman(1944) == 'MCMXLIV'
    # assert roman(2024) == 'MMXXIV'
    
    # assert roman(3999) == 'MMMCMXCIX'
    
    