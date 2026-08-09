price = float(input("Введите цену товара: "))
discount = float(input("Введите процент скидки: "))

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Цена со скидкой:", final_price)
