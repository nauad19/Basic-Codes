string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

s1_sorted = sorted(string1.lower().replace(" ", ""))
s2_sorted = sorted(string2.lower().replace(" ", ""))

if s1_sorted == s2_sorted:
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")
