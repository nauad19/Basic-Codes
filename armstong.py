num_str = input("Enter a number: ")
original_num = int(num_str)
n = len(num_str)
sum_of_powers = 0

for digit_char in num_str:
    digit = int(digit_char)
    power = 1
    i = 0
    while i < n:
        power = power * digit
        i = i + 1
    sum_of_powers = sum_of_powers + power

if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")
