from math import comb

# Input data
p = float(input("Enter probability chance (%): ")) / 100
n = int(input("Enter range of Set: "))

print("-" * 112)

# Calculate probabilities
for k in range(n + 1):
    probability = (p ** k) * ((1 - p) ** (n - k)) * comb(n, k)
    print(f"Success attempts: {k}  ---  Probability: {probability * 100} % | --> 1 in {1 / probability:_.2f}")

# Statistical characteristics
mean = n * p
variance = n * p * (1 - p)
std_dev = variance ** 0.5

print("-" * 112)
print(f"Mean --- [{p * 100:.3f} % / {n:_}] events is: {mean:.4f}")
print(f"Variance --- [{p * 100:.3f} % / {n:_}] events is: {variance:.4f}")
print(f"Standard deviation --- [{p * 100:.3f} % / {n:_}] events is: {std_dev:.4f}")
print("-" * 112)
