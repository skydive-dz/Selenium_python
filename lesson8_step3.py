from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x = browser.find_element_by_id("num1").text
	y = browser.find_element_by_css_selector("#num2").text
	sum = (int(x)+int(y))
	q = str(int(x)+int(y))
	b = browser.find_element_by_css_selector("select.custom-select").click()
	
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(q) # ищем элемент
	time.sleep(1)
	b1 = browser.find_element_by_css_selector("button.btn").click()

finally:
    
    time.sleep(10)
    
    alert = browser.switch_to.alert
    
    browser.quit()