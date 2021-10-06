from selenium import webdriver
import pytest
import time
import math

hidden_text = ''

@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print(hidden_text)  # напечатать ответ в конце теста


@pytest.mark.parametrize('links', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_find_hidden_text(browser, links):
    global hidden_text
    link = f'https://stepik.org/lesson/{links}/step/1'
    browser.implicitly_wait(10)
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element_by_css_selector('textarea').send_keys(str(answer))
    browser.find_element_by_css_selector('.submit-submission ').click()
    find_text = browser.find_element_by_css_selector('.smart-hints__hint').text
    try:
        assert 'Correct!' == find_text
    except AssertionError:
        hidden_text += find_text  # собираем ответ с каждой ошибкой