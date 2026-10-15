from colorama import Fore, init

def test_colorama():
    init(autoreset=True)
    print(Fore.RED + "[Colorama] Цей текст червоний")