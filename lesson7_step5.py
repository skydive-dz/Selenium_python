from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_xpath("//*[@id='treasure']")
    x_element_a = x_element.get_attribute("valuex")
    x = x_element_a
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    b1 = browser.find_element_by_id("robotCheckbox").click()
    b2 = browser.find_element_by_id("robotsRule").click()
    b3 = browser.find_element_by_css_selector("button.btn").click()
finally:
    
    time.sleep(10)
    
    alert = browser.switch_to.alert
    
    browser.quit()
