print("=" * 113)
print("📊 Z-SCORE АНАЛИЗ - СТАТИСТИЧЕСКА ЗНАЧИМОСТ")
print("=" * 113)

# Входни данни
observed_rate = float(input("Наблюдаван успех (%): ")) / 100
expected_rate = float(input("Очакван успех (%): ")) / 100
total_bets = int(input("Общ брой залози: "))

print("=" * 113)

# Изчисляване на Z-score
p = expected_rate
p_hat = observed_rate

standard_error = (p * (1 - p) / total_bets) ** 0.5
z_score = (p_hat - p) / standard_error

print(f"Z-SCORE: {z_score:.4f}")
print(f"Standard_error: {standard_error:.4f}")

# Интерпретация
print("=" * 113)
print("📈 СТАТИСТИЧЕСКА ЗНАЧИМОСТ:")

if abs(z_score) < 1.0:
    print("🎯 СЛАБА ЗНАЧИМОСТ - вероятно случайност")
elif 1.0 <= abs(z_score) < 1.96:
    print("⚠️  УМЕРЕНА ЗНАЧИМОСТ - потенциална разлика")
elif 1.96 <= abs(z_score) < 2.58:
    print("🔔 СИЛНА ЗНАЧИМОСТ - 95% сигурност")
else:
    print("🚨 МНОГО СИЛНА ЗНАЧИМОСТ - 99% сигурност")

print("=" * 113)

# Допълнителни статистики
observed_wins = total_bets * p_hat
expected_wins = total_bets * p
difference = observed_wins - expected_wins

print(f"Наблюдавани победи: {observed_wins:_.1f} от {total_bets:_}")
print(f"Очаквани победи: {expected_wins:_.1f} от {total_bets:_}")
print(f"Разлика: {difference:+.1f} победи")

print("=" * 113)

# Практическо приложение
edge = (observed_rate - expected_rate) * 100
if z_score > 1.96 and edge > 0:
    print(f"💰 РЕАЛЕН EDGE: +{edge:.2f}% (СТАТИСТИЧЕСКИ ЗНАЧИМ)")
    print(f"🎲 СТОЙНОСТЕН ЗАЛОГ: ДА")
else:
    print(f"📉 НЯМА СТАТИСТИЧЕСКИ ЗНАЧИМ EDGE")
    print(f"🎲 СТОЙНОСТЕН ЗАЛОГ: НЕ")

print("=" * 113)
