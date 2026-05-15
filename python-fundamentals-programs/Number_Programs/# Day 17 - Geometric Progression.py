# Day 17 - Geometric Progression

start = int(input("Enter starting value: "))
ratio = int(input("Enter common ratio: "))
n = int(input("Enter number of terms: "))

print("Geometric Progression:")

for i in range(n):
    term = start * (ratio ** i)
    print(term)