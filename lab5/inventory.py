INGREDIENT_SLOT_LIMIT = 25
INGREDIENT_STACK_LIMIT = 25
POTION_SLOT_LIMIT = 10
POTION_STACK_LIMIT = 10


def ingredient_slots(inventory):
    """Повертає кількість зайнятих слотів інгредієнтів."""
    return sum(1 for amount in inventory.values() if amount > 0)


def add_ingredient(inventory, name, amount=1):
    """Додає інгредієнт, дотримуючись обмежень слотів і стаків."""
    try:
        if amount <= 0:
            print("Кількість має бути більшою за нуль.")
            return False

        current = inventory.get(name, 0)
        free_capacity = INGREDIENT_STACK_LIMIT - current
        if current > 0:
            if free_capacity <= 0:
                print(f"Стак інгредієнту «{name}» уже повний.")
                return False
            added = min(amount, free_capacity)
            inventory[name] = current + added
            if added < amount:
                print(f"Додано {added}. Зайві предмети не помістилися.")
            return added > 0

        if ingredient_slots(inventory) >= INGREDIENT_SLOT_LIMIT:
            print("Інвентар інгредієнтів заповнений: усі 25 слотів зайняті.")
            return False

        added = min(amount, INGREDIENT_STACK_LIMIT)
        inventory[name] = added
        if added < amount:
            print(f"Додано {added}. Зайві предмети не помістилися.")
        return True
    except (TypeError, ValueError) as error:
        print(f"Помилка додавання інгредієнту: {error}")
        return False


def remove_ingredient(inventory, name, amount=1):
    try:
        if inventory.get(name, 0) < amount:
            return False
        inventory[name] -= amount
        if inventory[name] == 0:
            del inventory[name]
        return True
    except (TypeError, ValueError) as error:
        print(f"Помилка вилучення інгредієнту: {error}")
        return False


def add_potion(inventory, name):
    """Додає зілля; однакові зілля стакаються до 10."""
    try:
        if name in inventory and inventory[name] < POTION_STACK_LIMIT:
            inventory[name] += 1
            return True
        if name in inventory and inventory[name] >= POTION_STACK_LIMIT:
            print("Стак цього зілля повний.")
            return False
        if len(inventory) >= POTION_SLOT_LIMIT:
            print("Інвентар зіль заповнений: усі 10 слотів зайняті.")
            return False
        inventory[name] = 1
        return True
    except (TypeError, ValueError) as error:
        print(f"Помилка додавання зілля: {error}")
        return False
