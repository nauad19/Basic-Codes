n = 5
print("Pattern 1: Right Angle Triangle")
i = 1
while i <= n:
    j = 1
    row = ""
    while j <= i:
        row = row + "*"
        j = j + 1
    print(row)
    i = i + 1

print("\n Pattern 2: Square ")
i = 1
while i <= n:
    print("*" * n)
    i = i + 1

print("\n Pattern 3: Inverted Right Angle Triangle")
i = n
while i >= 1:
    print("*" * i)
    i = i - 1
