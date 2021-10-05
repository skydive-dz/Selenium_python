from selenium import webdriver
import unittest
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()

class TestReg(unittest.TestCase):
    def test_reg1(self):
        browser.implicitly_wait(1)
        browser.get(link1)
        input1 = browser.find_element_by_css_selector(".first:required").send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".second:required").send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".third:required").send_keys("IP@mail.ru")
        button = browser.find_element_by_css_selector("button.btn").click()
        welcome_text = browser.find_element_by_tag_name("h1").text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
    
    def test_reg2(self):
        browser.implicitly_wait(1)
        browser.get(link2)
        input1 = browser.find_element_by_css_selector("[required][class='form-control first']").send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[required][class='form-control second']").send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("[required][class='form-control third']").send_keys("IP@mail.ru")
        button = browser.find_element_by_css_selector("button.btn").click()
        welcome_text = browser.find_element_by_tag_name("h1").text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
if __name__ == "__main__":
    unittest.main()


