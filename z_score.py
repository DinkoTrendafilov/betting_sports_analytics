# Input data
observed_rate = float(input("Observed success rate (%): ")) / 100
expected_rate = float(input("Expected success rate (%): ")) / 100
total_bets = int(input("Total number of bets: "))

print("=" * 113)

# Calculate Z-score
p = expected_rate
p_hat = observed_rate

standard_error = (p * (1 - p) / total_bets) ** 0.5
z_score = (p_hat - p) / standard_error

print(f"Z-SCORE: {z_score:.4f}")
print(f"Standard error: {standard_error:.4f}")

# Interpretation
print("=" * 113)
print("STATISTICAL SIGNIFICANCE:")

if abs(z_score) < 1.0:
    print("WEAK SIGNIFICANCE - likely random chance")
elif 1.0 <= abs(z_score) < 1.96:
    print("MODERATE SIGNIFICANCE - potential difference")
elif 1.96 <= abs(z_score) < 2.58:
    print("STRONG SIGNIFICANCE - 95% confidence")
else:
    print("VERY STRONG SIGNIFICANCE - 99% confidence")

print("=" * 113)

# Additional statistics
observed_wins = total_bets * p_hat
expected_wins = total_bets * p
difference = observed_wins - expected_wins

print(f"Observed wins: {observed_wins:_.1f} out of {total_bets:_}")
print(f"Expected wins: {expected_wins:_.1f} out of {total_bets:_}")
print(f"Difference: {difference:+.1f} wins")

print("=" * 113)

# Practical application
edge = (observed_rate - expected_rate) * 100
if z_score > 1.96 and edge > 0:
    print(f"REAL EDGE: +{edge:.2f}% (STATISTICALLY SIGNIFICANT)")
    print(f"VALUE BET: YES")
else:
    print(f"NO STATISTICALLY SIGNIFICANT EDGE")
    print(f"VALUE BET: NO")

print("=" * 113)
