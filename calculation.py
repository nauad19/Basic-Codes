def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def is_perfect_number(n):
    if n <= 1:
        return False
    sum_divisors = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum_divisors = sum_divisors + i
            if i * i != n:
                sum_divisors = sum_divisors + n // i
        i = i + 1
    return sum_divisors == n

def is_armstrong(n):
    s = str(n)
    length = len(s)
    sum_of_powers = 0
    
    for digit_char in s:
        digit = int(digit_char)
        power = 1
        i = 0
        while i < length:
            power = power * digit
            i = i + 1
        sum_of_powers = sum_of_powers + power
        
    return sum_of_powers == n
