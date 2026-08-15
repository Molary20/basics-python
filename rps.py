import random

CHOICES = ["камень", "ножницы", "бумага"]

rounds = int(input("Сколько раундов будем играть? "))

user_score = 0
comp_score = 0

for r in range(1, rounds + 1):
    print(f"\nРаунд {r}")

    user_select = ""
    while user_select not in CHOICES:
        user_select = input("Выбери (камень/ножницы/бумага): ").lower().strip()
        if user_select not in CHOICES:
            print("Некорректный выбор")

    comp_select = random.choice(CHOICES)
    print(f"Компьютер выбрал: {comp_select}")

    if user_select == comp_select:
        print("Ничья")

    elif (
            (user_select == "камень" and comp_select == "ножницы")
            or (user_select == "ножницы" and comp_select == "бумага")
            or (user_select == "бумага" and comp_select == "камень")
    ):
        print("Ты победил!")
        user_score += 1

    else:
        print("Компьютер выиграл")
        comp_score += 1

print("\n==== Итог игры ====")
print(f"Твой счет: {user_score}")
print(f"Счет компьютера: {comp_score}")

if user_score > comp_score:
    print("Ты победил в игре!")
elif user_score < comp_score:
    print("Компьютер победил!")
else:
    print("Ничья!")
