from bs4 import BeautifulSoup

def test_bs4():
    html = "<html><body><h1>Hello BeautifulSoup</h1></body></html>"
    soup = BeautifulSoup(html, 'html.parser')
    print(f"[BeautifulSoup] Знайдений текст заголовка: {soup.h1.string}")