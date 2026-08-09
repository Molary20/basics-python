category = input("Выберите категорию (напиток, суп, десерт): ").lower()

match category:
    case "напиток":
        print("Чай, кофе, сок")
        dish = input("Что выбираете? ").lower()

        match dish:
            case "чай":
                print("Цена: 100 рублей")
            case "кофе":
                print("Цена: 150 рублей")
            case "сок":
                print("Цена: 120 рублей")
            case _:
                print("Такого напитка нет.")

    case "суп":
        print("Борщ, щи, суп-пюре")
        dish = input("Что выбираете? ").lower()

        match dish:
            case "борщ":
                print("Цена: 250 рублей")
            case "щи":
                print("Цена: 220 рублей")
            case "суп-пюре":
                print("Цена: 270 рублей")
            case _:
                print("Такого супа нет.")

    case "десерт":
        print("Торт, мороженое, фрукты")
        dish = input("Что выбираете? ").lower()

        match dish:
            case "торт":
                print("Цена: 300 рублей")
            case "мороженое":
                print("Цена: 180 рублей")
            case "фрукты":
                print("Цена: 200 рублей")
            case _:
                print("Такого десерта нет.")

    case _:
        print("Такой категории нет.")
