from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector("button.btn").click()
    confirm = browser.switch_to.alert.accept()
    el_x = browser.find_element_by_id("input_value")
    x = el_x.text
    y = calc(x)
    in1 = browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_css_selector("button.btn").click()
    print(browser.switch_to.alert.text)
finally:

	browser.quit()

