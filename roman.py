thousands = {0:'', 1: 'M', 2: 'MM', 3: 'MMM'}
hundreds = {0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
tens = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
ones = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV',  5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
def roman(n):
    M = n // 1000
    H = (n%1000)//100
    T = (n%100) //10
    O = n%10
    return f"{thousands[M]}{hundreds[H]}{tens[T]}{ones[O]}"

if __name__ == "__main__":  
    assert roman(39) == 'XXXIX'
    assert roman(246) == 'CCXLVI'
    assert roman(789) == 'DCCLXXXIX'
    assert roman(2421) == 'MMCDXXI'
    assert roman(160) == 'CLX'
    assert roman(207) == 'CCVII'
    assert roman(1009) == 'MIX'
    assert roman(1066) == 'MLXVI'
    assert roman(1776) == 'MDCCLXXVI'
    assert roman(1918) == 'MCMXVIII'
    assert roman(1944) == 'MCMXLIV'
    assert roman(2024) == 'MMXXIV'
    assert roman(3999) == 'MMMCMXCIX'
    