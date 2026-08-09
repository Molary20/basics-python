food = float(input("Расходы на еду: "))
transport = float(input("Расходы на транспорт: "))
entertainment = float(input("Расходы на развлечения: "))

total = food + transport + entertainment
average = total / 3

print("Общая сумма:", total)
print("Средние расходы:", average)
