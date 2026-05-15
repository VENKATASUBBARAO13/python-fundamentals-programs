# Day 24 - Sum of First N Prime Numbers

n = int(input("Enter how many prime numbers: "))

count = 0
num = 2
sum_prime = 0

while count < n:
    factors = 0

    for i in range(1, num + 1):
        if num % i == 0:
            factors = factors + 1

    if factors == 2:
        print(num)
        sum_prime = sum_prime + num
        count = count + 1

    num = num + 1

print("Sum of prime numbers:", sum_prime)