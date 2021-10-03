from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    el_x = browser.find_element_by_id("input_value")
    x = el_x.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    browser.execute_script("window.scrollBy(0, 100);")
    b1 = browser.find_element_by_id("robotCheckbox").click()
    b2 = browser.find_element_by_id("robotsRule").click()
    b3 = browser.find_element_by_css_selector("button.btn").click()
finally:
    
    time.sleep(10)
    
    alert = browser.switch_to.alert
    
    browser.quit()
