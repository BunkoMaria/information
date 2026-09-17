users = {
    "masha": {
        "password": "1234",
        "grades": [12, 10, 8, 11, 7, 4, 3, 9]
    },
    "danya": {
        "password": "5678",
        "grades": [11, 12, 10, 9, 5, 3, 2]
    },
    "anna": {
        "password": "1111",
        "grades": [8, 7, 10, 12, 6, 4, 3]
    },
    "max": {
        "password": "2222",
        "grades": [12, 11, 9, 6, 5, 4, 2, 1]
    }
}

login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login in users and users[login]["password"] == password:

    print("\nВхід успішний!")

    grades = users[login]["grades"]

    print("Ваші оцінки:")
    print(grades)

    satisfactory = 0
    unsatisfactory = 0

    for grade in grades:
        if 5 <= grade <= 12:
            satisfactory += 1
        elif 1 <= grade <= 4:
            unsatisfactory += 1

    print("\nКількість задовільних оцінок (5-12):", satisfactory)
    print("Кількість незадовільних оцінок (1-4):", unsatisfactory)

else:
    print("\nНеправильний логін або пароль!")