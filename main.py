import calculation

number = 371
number_2 = 121
number_3 = 28
number_4 = 13

print(f"Checking number {number}:")
print("Is Prime:", calculation.is_prime(number))
print("Is Palindrome:", calculation.is_palindrome(number))
print("Is Perfect Number:", calculation.is_perfect_number(number))
print("Is Armstrong:", calculation.is_armstrong(number))

print(f"\nChecking number {number_2}:")
print("Is Palindrome:", calculation.is_palindrome(number_2))

print(f"\nChecking number {number_3}:")
print("Is Perfect Number:", calculation.is_perfect_number(number_3))

print(f"\nChecking number {number_4}:")
print("Is Prime:", calculation.is_prime(number_4))
