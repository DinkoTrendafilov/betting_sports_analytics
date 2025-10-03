from math import comb
from collections import defaultdict

# Въвеждане на параметри
print("Въведете параметрите на хипергеометричното разпределение:")
N = int(input("Общ брой изделия (N): "))
K = int(input("Общ брой дефектни изделия (K): "))
n = int(input("Размер на извадката (n): "))

# Проверка за валидност
if K > N or n > N or any(x < 0 for x in [N, K, n]):
    print("Грешка: Невалидни входни параметри")
    exit()

print("-" * 112)
# Изчисляване на вероятностите
probabilities = defaultdict(float)

for k in range(min(K, n) + 1):
    prob = (comb(K, k) * comb(N - K, n - k)) / comb(N, n)
    probabilities[k] = prob
    print(f"-- Дефектни изделия: {k} -- {prob * 100} % | --> 1 to {1 / prob:_.2f}")

# Изчисляване на статистики
mean = sum(k * prob for (k, prob) in probabilities.items())
variance = sum((k - mean) ** 2 * prob for (k, prob) in probabilities.items())
std_dev = variance ** 0.5

print("-" * 112)
# Извеждане на статистиките в конзолата
print("\nСтатистически характеристики:")
print(f"Средна стойност (μ): {mean:.4f}")
print(f"Дисперсия (σ²): {variance:.4f}")
print(f"Стандартно отклонение (σ): {std_dev:.4f}")

print("-" * 112)
print(f"Total combinations: {comb(N, n):_}")
print("-" * 112)
another_average_way = (K / N) * n
print(another_average_way)
print("-" * 112)

