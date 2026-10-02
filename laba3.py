products = [
    ["Ноутбук", 25000.00, 5],
    ["Мишка", 500.00, 10],
    ["Клавіатура", 1200.00, 7],
    ["Навушники", 1800.00, 8],
    ["Флешка", 400.00, 15]
]

cart = []

price = lambda x: f"{x:.2f} грн"


def show_products():
    print("\n--- КАТАЛОГ ---")

    for i in range(len(products)):
        print(
            i + 1,
            products[i][0],
            "-",
            price(products[i][1]),
            "Залишок:",
            products[i][2]
        )


def add_to_cart():
    show_products()

    number = int(input("\nВиберіть номер товару: "))
    number = number - 1

    if number >= 0 and number < len(products):
        count = int(input("Введіть кількість: "))

        if count > 0 and count <= products[number][2]:
            cart.append([
                products[number][0],
                products[number][1],
                count
            ])

            print("Товар додано в кошик!")
        else:
            print("Недостатня кількість товару.")
    else:
        print("Неправильний номер.")


def show_cart():
    print("\n--- КОШИК ---")

    if len(cart) == 0:
        print("Кошик порожній.")
        return

    total = 0

    for i in range(len(cart)):
        print(
            i + 1,
            cart[i][0],
            "-",
            cart[i][2],
            "шт."
        )

        total = total + cart[i][1] * cart[i][2]

    print("Загальна сума:", price(total))


def delete_from_cart():
    show_cart()

    if len(cart) > 0:
        number = int(input("Виберіть номер товару: "))

        if number > 0 and number <= len(cart):
            cart.pop(number - 1)
            print("Товар видалено!")
        else:
            print("Неправильний номер.")


def buy():
    if len(cart) == 0:
        print("Кошик порожній.")
        return

    show_cart()

    answer = input("Купити товари? (так/ні): ")

    if answer == "так":
        for item in cart:
            for product in products:
                if item[0] == product[0]:
                    product[2] = product[2] - item[2]

        cart.clear()

        print("Покупку здійснено!")
    else:
        print("Покупку скасовано.")


def admin():
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    if login == "admin" and password == "1234":
        print("\n--- ЗАЛИШКИ ---")

        for product in products:
            print(product[0], "-", product[2], "шт.")
    else:
        print("Неправильний логін або пароль.")


def main():
    while True:
        print("\n===== МІНІ-МАГАЗИН =====")
        print("1 - Переглянути каталог")
        print("2 - Додати товар у кошик")
        print("3 - Переглянути кошик")
        print("4 - Видалити товар з кошика")
        print("5 - Купити товари")
        print("6 - Увійти як адміністратор")
        print("0 - Вийти")

        choice = input("Виберіть дію: ")

        if choice == "1":
            show_products()

        elif choice == "2":
            add_to_cart()

        elif choice == "3":
            show_cart()

        elif choice == "4":
            delete_from_cart()

        elif choice == "5":
            buy()

        elif choice == "6":
            admin()

        elif choice == "0":
            print("До побачення!")
            break

        else:
            print("Неправильний вибір.")


if __name__ == ("__main__"):
    main()