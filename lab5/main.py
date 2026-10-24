from game import start_game

if __name__ == "__main__":
    try:
        start_game()
    except KeyboardInterrupt:
        print("\nГру завершено. До зустрічі, алхіміку!")
    except Exception as error:
        print(f"Сталася непередбачена помилка: {error}")
