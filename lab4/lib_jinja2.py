from jinja2 import Template

def test_jinja2():
    template = Template("Привіт, {{ name }}!")
    result = template.render(name="Студенте")
    print(f"[Jinja2] Результат шаблонізації: {result}")