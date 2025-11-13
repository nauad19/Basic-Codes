def reverse_num(n, rev=0):
    if n == 0:
        return rev
    return reverse_num(n // 10, rev * 10 + n % 10)

num = int(input("Enter a number: "))

if num == reverse_num(num):
    print("Palindrome")
else:
    print("Not a palindrome")
