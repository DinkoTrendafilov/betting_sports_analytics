from math import factorial, exp, e

lambda_ = float(input("Enter λ (mean value): "))
k_min = int(input("Enter initial value for k: "))
k_max = int(input("Enter maximum value for k: "))

print("-" * 113)

cumulative = 0
for k in range(k_min, k_max + 1):
    p = (exp(-lambda_) * (lambda_ ** k)) / factorial(k)
    cumulative += p
    print(f"P(X={k}) = {p * 100} % | Cumulative P(X≤{k}) = {cumulative * 100} %  | (1 IN {(1 / p):_.2f})")

# Statistical characteristics
mean = lambda_
variance = lambda_
std_dev = variance ** 0.5

print("-" * 113)
print(f"Euler number e is: {e}")
print("-" * 113)
