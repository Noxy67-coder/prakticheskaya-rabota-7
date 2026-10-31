import math

print("=== АНАЛИЗ РЕЗУЛЬТАТОВ ИЗМЕРЕНИЙ ===")

# Ввод количества измерений
while True:
    try:
        n = int(input("Введите количество измерений (5-20): "))
        if 5 <= n <= 20:
            break
        print("Количество измерений должно быть от 5 до 20.")
    except ValueError:
        print("Введите целое число.")

# Ввод результатов измерений
measurements = []

for i in range(n):
    while True:
        try:
            value = float(
                input(f"Измерение {i + 1}: ").replace(",", ".")
            )
            measurements.append(value)
            break
        except ValueError:
            print("Введите корректное число.")

# Статистические вычисления
average = sum(measurements) / n
minimum = min(measurements)
maximum = max(measurements)
data_range = maximum - minimum

# Среднеквадратичное отклонение
std_dev = math.sqrt(
    sum((x - average) ** 2 for x in measurements) / n
)

# Относительная погрешность
relative_error = (
    abs(std_dev / average * 100) if average != 0 else 0
)

# Фильтрация выбросов
filtered = [
    x for x in measurements
    if abs(x - average) <= 2 * std_dev
]

# Вывод результатов
print("\n=== РЕЗУЛЬТАТЫ АНАЛИЗА ===")
print(f"Количество измерений: {n}")
print(f"Среднее значение: {average:.3f}")
print(f"Минимум: {minimum:.3f}")
print(f"Максимум: {maximum:.3f}")
print(f"Размах: {data_range:.3f}")
print(f"Среднеквадратичное отклонение: {std_dev:.3f}")
print(f"Относительная погрешность: {relative_error:.1f}%")

print("\n=== ФИЛЬТРАЦИЯ ВЫБРОСОВ ===")
print("Отфильтрованные данные:")

for value in filtered:
    print(f"{value:.3f}")

print(f"Осталось измерений: {len(filtered)}")
