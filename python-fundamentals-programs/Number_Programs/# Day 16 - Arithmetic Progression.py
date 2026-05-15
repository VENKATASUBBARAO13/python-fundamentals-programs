# Day 16 - Arithmetic Progression

start = int(input("Enter starting value: "))
difference = int(input("Enter common difference: "))
n = int(input("Enter number of terms: "))

print("Arithmetic Progression:")

for i in range(n):
    term = start + i * difference
    print(term)