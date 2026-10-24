import random
from data import INGREDIENTS, POTIONS
from inventory import add_potion, remove_ingredient

# Рецепти генеруються з пулу 200 інгредієнтів для кожного з 50 видів зіль.
# Для легендарного зілля потрібні рідкісні складники.
RECIPES = {}
for index, (potion_name, price) in enumerate(POTIONS):
    first = INGREDIENTS[(index * 3) % len(INGREDIENTS)]
    second = INGREDIENTS[(index * 7 + 11) % len(INGREDIENTS)]
    third = INGREDIENTS[(index * 13 + 29) % len(INGREDIENTS)]
    RECIPES[potion_name] = {first: 2, second: 1, third: 1}

legendary = "Легендарне зілля безсмертя"
RECIPES[legendary] = {
    "Кров дракона": 2,
    "Перо фенікса": 2,
    "Есенція життя": 3,
    "Золотий пил": 1
}


def show_recipes():
    print("\n--- КНИГА РЕЦЕПТІВ ---")
    for index, (name, price) in enumerate(POTIONS, start=1):
        ingredients = ", ".join(
            f"{ingredient} x{amount}"
            for ingredient, amount in RECIPES[name].items()
        )
        print(f"{index}. {name} | ціна: {price} золота")
        print(f"   Потрібно: {ingredients}")


def brew_potion(ingredient_inventory, potion_inventory):
    try:
        show_recipes()
        choice = input("\nВведи номер зілля (0 — скасувати): ").strip()
        if not choice.isdigit():
            print("Потрібно ввести номер.")
            return False
        number = int(choice)
        if number == 0:
            return False
        if not 1 <= number <= len(POTIONS):
            print("Немає такого рецепта.")
            return False

        name = POTIONS[number - 1][0]
        recipe = RECIPES[name]

        for ingredient, amount in recipe.items():
            if ingredient_inventory.get(ingredient, 0) < amount:
                print(f"Не вистачає: {ingredient} (потрібно {amount}).")
                return False

        # Перевіряємо слот до витрати інгредієнтів.
        if name not in potion_inventory and len(potion_inventory) >= 10:
            print("Немає вільного слота для нового виду зілля.")
            return False
        if potion_inventory.get(name, 0) >= 10:
            print("Стак цього зілля вже повний.")
            return False

        for ingredient, amount in recipe.items():
            remove_ingredient(ingredient_inventory, ingredient, amount)

        if add_potion(potion_inventory, name):
            print(f"Успіх! Ти зварив: {name}.")
            return True
        print("Зілля не вдалося додати до інвентарю.")
        return False
    except (ValueError, KeyError, TypeError) as error:
        print(f"Помилка під час алхімії: {error}")
        return False


def give_daily_ingredients(inventory):
    received = []
    try:
        for _ in range(5):
            name = random.choice(INGREDIENTS)
            if inventory.get(name, 0) < 25 and (name in inventory or len(inventory) < 25):
                if name in inventory:
                    inventory[name] += 1
                else:
                    inventory[name] = 1
                received.append(name)
        print("\nТи отримав інгредієнти за день:")
        if received:
            for name in received:
                print(f"  + {name}")
        else:
            print("Немає місця в інвентарі.")
    except (TypeError, ValueError) as error:
        print(f"Не вдалося отримати інгредієнти: {error}")
