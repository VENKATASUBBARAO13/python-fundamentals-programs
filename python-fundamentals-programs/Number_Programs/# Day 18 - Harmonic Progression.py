# Day 18 - Harmonic Progression

start = int(input("Enter starting value: "))
difference = int(input("Enter common difference: "))
n = int(input("Enter number of terms: "))

print("Harmonic Progression:")

for i in range(n):
    ap_term = start + i * difference
    hp_term = 1 / ap_term
    print(hp_term)