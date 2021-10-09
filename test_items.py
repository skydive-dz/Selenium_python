import time
def test_user_should_find_busket_button(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	browser.get(link)
	time.sleep(3)
	browser.implicitly_wait(10)
	assert browser.find_element_by_css_selector(".add-to-basket .btn"), "Button is not defined"
	