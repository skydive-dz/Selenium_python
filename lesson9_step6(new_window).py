from selenium import webdriver
import math
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_css_selector("button.btn").click()
new_window = browser.window_handles[1]
#first_window = browser.window_handles[0] #Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться
browser.switch_to.window(new_window)
el_x = browser.find_element_by_id("input_value")
x = el_x.text
y = calc(x)
in1 = browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_css_selector("button.btn").click()
print(browser.switch_to.alert.text)

browser.quit()
