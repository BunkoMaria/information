import matplotlib.pyplot as plt

def test_matplotlib():
    # Просто створює і зберігає графік у файл, щоб не блокувати виконання
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.savefig("plot.png")
    print("[Matplotlib] График збережено у файл plot.png")