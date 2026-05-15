# Day 13 - Average of N Numbers

n = int(input("Enter how many numbers: "))

sum_numbers = 0

for i in range(1, n + 1):
    num = int(input("Enter number: "))
    sum_numbers = sum_numbers + num

average = sum_numbers / n

print("Sum:", sum_numbers)
print("Average:", average)