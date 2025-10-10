from math import factorial, comb
from collections import defaultdict

n = int(input("Enter number of events: "))
win = float(input(f"Enter probability for win: "))
draw = float(input(f"Enter probability for draw: "))
loss = float(input(f"Enter probability for loss: "))

if win + draw + loss != 100:
    print("-" * 113)
    print(f"Win + Draw + Loss must be 100: ")
    print(f"Enter correct data please: ")
    print("-" * 113)
    exit()

win /= 100
draw /= 100
loss /= 100

# a = 50%  / 0.5   b = 30% / 0.3  c = 20% / 0.2   k = 3
k = 3
d = defaultdict(float)
TOTAL_EVENTS_FACTORIAL = factorial(n)

for a in range(n + 1):
    for b in range(n + 1):
        for c in range(n + 1):
            if a + b + c == n:
                coefficient = TOTAL_EVENTS_FACTORIAL // (factorial(a) * factorial(b) * factorial(c))
                result = (win ** a) * (draw ** b) * (loss ** c) * coefficient
                res = (a, b, c)
                d[res] += result
                print(res, coefficient)

sorted_d = dict(sorted(d.items(), key=lambda kvp: (-kvp[1], kvp[0])))

print("-" * 112)
print("The combinations and their probabilities are:")
counter = 0
for (key, value) in sorted_d.items():
    counter += 1
    print(f"#{counter:_} ({key[0]}, {key[1]}, {key[2]}) -> {value * 100} %")
print()
print(f"Total unique combinations is: {comb(n + k - 1, n):_}")
print("-" * 112)
