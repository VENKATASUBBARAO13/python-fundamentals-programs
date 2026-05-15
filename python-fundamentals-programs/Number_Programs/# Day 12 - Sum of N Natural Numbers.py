# Day 12 - Sum of N Natural Numbers

n = int(input("Enter n value: "))

sum_numbers = 0

for i in range(1, n + 1):
    sum_numbers = sum_numbers + i

print("Sum:", sum_numbers)