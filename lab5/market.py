from data import POTIONS


def sell_potions(inventory):
    prices = dict(POTIONS)
    total = 0
    try:
        if not inventory:
            print("У тебе немає зіль для продажу.")
            return 0

        print("\n--- ТВОЇ ЗІЛЛЯ ---")
        for name, amount in inventory.items():
            print(f"{name}: {amount} шт. — {prices.get(name, 0)} золота за одне")

        answer = input("Продати всі зілля? (так/ні): ").strip().lower()
        if answer not in ("так", "т", "yes", "y"):
            print("Продаж скасовано.")
            return 0

        for name, amount in inventory.items():
            total += prices.get(name, 0) * amount
        inventory.clear()
        print(f"Продаж завершено! Ти отримав {total} золота.")
        return total
    except (TypeError, ValueError) as error:
        print(f"Помилка під час продажу: {error}")
        return 0
