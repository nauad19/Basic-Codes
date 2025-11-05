num = int(input("Enter a number: "))

if num < 2:
    is_prime = False
elif num == 2:
    is_prime = True
else:
    is_prime = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i = i + 1

if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
