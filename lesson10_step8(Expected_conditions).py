from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
browser.find_element_by_css_selector("button.btn").click()
el_x = browser.find_element_by_id("input_value")
x = el_x.text
y = calc(x)
in1 = browser.find_element_by_id("answer").send_keys(y)
# button = WebDriverWait(browser, 5).until(EC.element_to_be_clicable(BY.CSS_SELECTOR, "button.btn")).click()
browser.find_element_by_id("solve").click()
print(browser.switch_to.alert.text)

browser.quit()



