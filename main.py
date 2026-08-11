parts = input().lower().split()

try:
    if len(parts) == 2 and parts[1] == "руб":
        rubles = int(parts[0])
        kopecks = 0

    elif (
            len(parts) == 4
            and parts[1] == "руб"
            and parts[3] == "коп"
    ):
        rubles = int(parts[0])
        kopecks = int(parts[2])

    else:
        raise ValueError

    if rubles < 0 or not 0 <= kopecks <= 99:
        raise ValueError

    print(f"{rubles}.{kopecks:02d} ₽")

except ValueError:
    print("Некорректный формат суммы")
