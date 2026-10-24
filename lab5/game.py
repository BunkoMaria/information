from data import POTIONS
from inventory import add_ingredient
from alchemy import brew_potion, give_daily_ingredients
from market import sell_potions

MAX_DAYS = 10
GOAL_GOLD = 1000
LEGENDARY_POTION = "Легендарне зілля безсмертя"


def show_inventory(ingredients, potions, gold):
    try:
        print("\n========== ІНВЕНТАР ==========")
        print(f"Золото: {gold}")
        print(f"Інгредієнти: {len(ingredients)}/25 слотів")
        if ingredients:
            for name, amount in ingredients.items():
                print(f"  {name}: {amount}/25")
        else:
            print("  Порожньо")
        print(f"Зілля: {len(potions)}/10 слотів")
        if potions:
            for name, amount in potions.items():
                print(f"  {name}: {amount}/10")
        else:
            print("  Порожньо")
        print("==============================")
    except (TypeError, ValueError) as error:
        print(f"Не вдалося показати інвентар: {error}")


def start_game():
    ingredients = {}
    potions = {}
    gold = 0
    has_legendary = False
    print("=" * 48)
    print("       АЛХІМІК: ШЛЯХ ДО БЕЗСМЕРТЯ")
    print("=" * 48)
    print("Ти — молодий алхімік. Королівство охопила загадкова хвороба.")
    print("За 10 днів збери 1000 золота та створи легендарне зілля безсмертя.")
    print("Щодня ти отримуватимеш 5 випадкових інгредієнтів.")
    print("Пам'ятай: інгредієнти стакаються до 25, зілля — до 10.")
    print("Для перемоги потрібно виконати ОБИДВІ умови: 1000 золота і легендарне зілля.")

    for day in range(1, MAX_DAYS + 1):
        print(f"\n\n{'=' * 16} ДЕНЬ {day}/{MAX_DAYS} {'=' * 16}")
        give_daily_ingredients(ingredients)
        day_finished = False

        while not day_finished:
            print("\nЩо робитимеш?")
            print("1. Переглянути інвентар")
            print("2. Варити зілля")
            print("3. Продати зілля та завершити день")
            print("4. Завершити день без продажу")
            try:
                choice = input("Твій вибір: ").strip()
                if choice == "1":
                    show_inventory(ingredients, potions, gold)
                elif choice == "2":
                    brewed = brew_potion(ingredients, potions)
                    if brewed and potions.get(LEGENDARY_POTION, 0) > 0:
                        has_legendary = True
                elif choice == "3":
                    gold += sell_potions(potions)
                    day_finished = True
                elif choice == "4":
                    day_finished = True
                else:
                    print("Вибери число від 1 до 4.")
            except (EOFError, ValueError) as error:
                print(f"Некоректне введення: {error}. Спробуй ще раз.")

        print(f"\nКінець дня {day}. Твоє золото: {gold}.")
        if gold >= GOAL_GOLD and has_legendary:
            print("\n" + "=" * 48)
            print("ПЕРЕМОГА! Ти створив легендарне зілля і зібрав 1000 золота.")
            print("Королівство врятовано, а твоє ім'я стало легендою!")
            print("=" * 48)
            return

    print("\n" + "=" * 48)
    if gold >= GOAL_GOLD and has_legendary:
        print("ПЕРЕМОГА! Ти став найвідомішим алхіміком королівства!")
    else:
        print("ПОРАЗКА! Десять днів минули, а мету не виконано.")
        print(f"Ти зібрав {gold}/{GOAL_GOLD} золота.")
        print("Спробуй знову: плануй рецепти, бережи інгредієнти та продавай зілля.")
    print("=" * 48)
