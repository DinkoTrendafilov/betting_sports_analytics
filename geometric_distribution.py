p = float(input("Success probability (%): ")) / 100
k_max = int(input("Maximum number of attempts for calculation: "))

print("-" * 113)

cumulative = 0
for k in range(1, k_max + 1):
    probability = ((1 - p) ** (k - 1)) * p
    cumulative += probability
    print(f"First success on attempt {k}: {probability * 100:.3f} % | "
          f"Cumulative: {cumulative * 100:.3f} % | 1 in {1 / probability:_.2f}")

# Statistical characteristics
mean = 1 / p
variance = (1 - p) / (p ** 2)
std_dev = variance ** 0.5

print("-" * 113)
print(f"STATISTICAL CHARACTERISTICS:")
print(f"Mean (μ): {mean:.4f} attempts")
print(f"Variance (σ²): {variance:.4f}")
print(f"Standard deviation (σ): {std_dev:.4f}")
print("-" * 113)
