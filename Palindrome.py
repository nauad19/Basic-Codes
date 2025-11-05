num_str = input("Enter a number to check for palindrome: ")

reversed_str = num_str[::-1]

if num_str == reversed_str:
    print(f"{num_str} is a palindrome.")
else:
    print(f"{num_str} is not a palindrome.")
