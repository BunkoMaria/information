from PIL import Image

def test_pillow():
    img = Image.new('RGB', (100, 100), color='red')
    img.save('test_image.png')
    print("[Pillow] Створено та збережено тестове зображення test_image.png")