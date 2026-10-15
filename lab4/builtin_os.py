import os

def test_os():
    cwd = os.getcwd()
    print(f"[OS] Поточна робоча директорія: {cwd}")