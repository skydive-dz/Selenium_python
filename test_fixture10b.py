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

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        # Поменяем селектор
        browser.find_element_by_css_selector("input.btn.btn-default")

# Здесь мы добавили символ X в параметр -r, чтобы получить подробную информацию по XPASS-тестам:

# pytest -rX -v test_fixture10b.py
# -v - режим verbous (многословный). Детально расскажет о прохождении.
# -rA - вывод дополнительных сообщений
# -rx - report on XFAIL (отчитаться о наличии метки XFAIL). В целом, даже без (remark = "") покажет в каком тесте была метка.