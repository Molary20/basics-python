expenses = [500, 1200, 300, 750, 900, 400, 650]

total = sum(expenses)
average = total / len(expenses)
minimum = min(expenses)
maximum = max(expenses)

result = (minimum, maximum, total)

print("Сумма:", total)
print("Среднее:", average)
print("Минимум:", minimum)
print("Максимум:", maximum)
print("Кортеж:", result)
