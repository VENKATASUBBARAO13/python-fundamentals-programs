# Day 10 - Armstrong Number

n = int(input("Enter a number: "))

original = n
sum_digits = 0

while n > 0:
    digit = n % 10
    sum_digits = sum_digits + digit ** 3
    n = n // 10

if original == sum_digits:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")