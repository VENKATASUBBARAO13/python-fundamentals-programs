# Day 6 - Palindrome Number

n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
