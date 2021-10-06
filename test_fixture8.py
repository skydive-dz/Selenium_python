import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")
def browser():
	print("\nstart browser for test..")
	browser = webdriver.Chrome()
	yield browser
	print("\nquit browser..")
	browser.quit()

class TestMainPage1():
	@pytest.mark.smoke
	@pytest.mark.win10
	def test_guest_should_see_login_link(self, browser):
		browser.get(link)
		browser.find_element_by_css_selector("#login_link")

	@pytest.mark.regression
	def test_guest_should_see_basket_link_on_the_main_page(self, browser):
		browser.get(link)
		browser.find_element_by_css_selector(".basket-mini .btn-group >a")

# Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку:
# pytest -s -v -m smoke test_fixture8.py
# Если всё сделано правильно, то должен запуститься только тест с маркировкой smoke.
# Как же регистрировать метки?
# Создайте файл pytest.ini в корневой директории вашего тестового проекта и добавьте в файл следующие строки:

# [pytest]
# markers =
#     smoke: marker for smoke tests
#     regression: marker for regression tests
# Текст после знака ":" является поясняющим — его можно не писать.
# pytest -s -v -m "not smoke" test_fixture8.py Инверсия
# pytest -s -v -m "smoke or regression" test_fixture8.py Запуск тестов с разными метками

# Предположим, у нас есть smoke-тесты, которые нужно запускать только для определенной операционной системы, например, для Windows 10.
# Зарегистрируем метку win10 в файле pytest.ini, а также добавим к одному из тестов эту метку.
# pytest.ini:
# [pytest]
# markers =
#     smoke: marker for smoke tests
#     regression: marker for regression tests
#     win10

# Чтобы запустить только smoke-тесты для Windows 10, нужно использовать логическое И:

# pytest -s -v -m "smoke and win10" test_fixture81.py