from math import comb

# Input data
p = float(input("Enter probability chance (%): ")) / 100
r = int(input("Enter target number of successes (r): "))
k_max = int(input("Enter maximum number of trials to calculate: "))

print("-" * 113)

# Calculate probabilities
cumulative = 0
for k in range(r, k_max + 1):
    probability = comb(k - 1, r - 1) * (p ** r) * ((1 - p) ** (k - r))
    cumulative += probability
    print(f"Trials needed: {k}  ---  Probability: {probability * 100} % | "
          f"Cumulative: {cumulative * 100} % | --> 1 in {1 / probability:_.2f}")

# Statistical characteristics
mean = r / p
variance = r * (1 - p) / (p ** 2)
std_dev = variance ** 0.5

print("-" * 113)
print(f"Mean --- {r} successes with {p * 100:.3f}% probability: {mean:.4f} trials")
print(f"Variance --- {r} successes with {p * 100:.3f}% probability: {variance:.4f}")
print(f"Standard deviation --- {r} successes with {p * 100:.3f}% probability: {std_dev:.4f}")
print("-" * 113)
