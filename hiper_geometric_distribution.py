from math import comb
from collections import defaultdict

# Input parameters
print("Enter hypergeometric distribution parameters:")
N = int(input("Total number of items (N): "))
K = int(input("Total number of defective items (K): "))
n = int(input("Sample size (n): "))

# Validation check
if K > N or n > N or any(x < 0 for x in [N, K, n]):
    print("Error: Invalid input parameters")
    exit()

print("-" * 112)
# Calculate probabilities
probabilities = defaultdict(float)

for k in range(min(K, n) + 1):
    prob = (comb(K, k) * comb(N - K, n - k)) / comb(N, n)
    probabilities[k] = prob
    print(f"-- Defective items: {k} -- {prob * 100} % | --> 1 in {1 / prob:_.2f}")

# Calculate statistics
mean = sum(k * prob for (k, prob) in probabilities.items())
variance = sum((k - mean) ** 2 * prob for (k, prob) in probabilities.items())
std_dev = variance ** 0.5

print("-" * 112)
# Output statistics to console
print("\nStatistical characteristics:")
print(f"Mean (μ): {mean:.4f}")
print(f"Variance (σ²): {variance:.4f}")
print(f"Standard deviation (σ): {std_dev:.4f}")

print("-" * 112)
print(f"Total combinations: {comb(N, n):_}")
print("-" * 112)
another_average_way = (K / N) * n
print(another_average_way)
print("-" * 112)
