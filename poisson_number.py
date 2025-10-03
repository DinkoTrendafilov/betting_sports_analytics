from math import factorial, exp, e

lambda_ = float(input("Въведете λ (средна стойност): "))
k_min = int(input("Въведете начална стойност за k: "))
k_max = int(input("Въведете максимална стойност за k: "))

print("-" * 113)

cumulative = 0
for k in range(k_min, k_max + 1):
    p = (exp(-lambda_) * (lambda_ ** k)) / factorial(k)
    cumulative += p
    print(f"P(X={k}) = {p * 100} % | Кум. P(X≤{k}) = {cumulative * 100} %  | (1 FROM {(1 / p):_.2f})")


# Статистически характеристики
mean = lambda_
variance = lambda_
std_dev = variance ** 0.5

print("-" * 113)
print(f"Euler number e is: {e}")
print("-" * 113)
