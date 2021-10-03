import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"
try:
	browser = webdriver.Chrome()
	browser.get(link)

	firstname = "Frodo"
	lastname = "Beggins"
	emale = "Sheer@fb.mrd"
	browser.find_element_by_name("firstname").send_keys(firstname)
	browser.find_element_by_name("lastname").send_keys(lastname)
	browser.find_element_by_name("email").send_keys(emale)

	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_name = "file_example.txt"
	file_path = os.path.join(current_dir, file_name)
	element = browser.find_element_by_id("file")
	element.send_keys(file_path)

	bt = browser.find_element_by_css_selector("button.btn").click()

finally:

    time.sleep(10)

    alert = browser.switch_to.alert

    browser.quit()