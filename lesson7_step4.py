from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    b1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    b1.click()
    b2 = browser.find_element_by_css_selector("[for='robotsRule']")
    b2.click()
    b3 = browser.find_element_by_css_selector("button.btn")
    b3.click()
finally:
    
    time.sleep(10)
    
    alert = browser.switch_to.alert
    
    browser.quit()

