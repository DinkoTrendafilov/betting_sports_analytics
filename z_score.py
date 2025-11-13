from scipy import stats

observed_rate = float(input("Наблюдаван успех (%): ")) / 100
expected_rate = float(input("Очакван успех (%): ")) / 100
total_bets = int(input("Общ брой залози: "))

print("=" * 112)


p = expected_rate
p_hat = observed_rate

standard_error = (p * (1 - p) / total_bets) ** 0.5
z_score = (p_hat - p) / standard_error
p_value_one_tail = stats.norm.sf(abs(z_score))
p_value_two_tails = 2 * p_value_one_tail

print(f"Z-SCORE: {z_score:.4f}")
print(f"Pi-Value: {p_value_two_tails * 100:.10f} %") # 1 trillion = 1000 mrld
print(f"Standard_error: {standard_error:.4f}")

