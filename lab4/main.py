from builtin_math import test_math
from builtin_datetime import test_datetime
from builtin_json import test_json
from builtin_random import test_random
from builtin_os import test_os

from lib_requests import test_requests
from lib_pandas import test_pandas
from lib_numpy import test_numpy
from lib_matplotlib import test_matplotlib
from lib_bs4 import test_bs4
from lib_rich import test_rich
from lib_jinja2 import test_jinja2
from lib_colorama import test_colorama
from lib_click import test_click
from lib_pillow import test_pillow

if __name__ == "__main__":
    print("=== ЗАПУСК ВБУДОВАНИХ БІБЛІОТЕК ===")
    test_math()
    test_datetime()
    test_json()
    test_random()
    test_os()

    print("\n=== ЗАПУСК СТОРОННІХ БІБЛІОТЕК ===")
    test_requests()
    test_pandas()
    test_numpy()
    test_matplotlib()
    test_bs4()
    test_rich()
    test_jinja2()
    test_colorama()
    test_click()
    test_pillow()