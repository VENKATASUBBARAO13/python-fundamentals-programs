# Day 19 - Sum and Average of AP, GP, HP

start = int(input("Enter starting value: "))
difference = int(input("Enter common difference: "))
ratio = int(input("Enter common ratio: "))
n = int(input("Enter number of terms: "))

ap_sum = 0
gp_sum = 0
hp_sum = 0

for i in range(n):
    ap_term = start + i * difference
    gp_term = start * (ratio ** i)
    hp_term = 1 / ap_term

    ap_sum = ap_sum + ap_term
    gp_sum = gp_sum + gp_term
    hp_sum = hp_sum + hp_term

print("AP Sum:", ap_sum)
print("AP Average:", ap_sum / n)

print("GP Sum:", gp_sum)
print("GP Average:", gp_sum / n)

print("HP Sum:", hp_sum)
print("HP Average:", hp_sum / n)