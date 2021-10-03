from selenium import webdriver
browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/wait1.html")
button = browser.find_element_by_id("verify").click()
message = browser.find_element_by_id("verify_message")
assert "successful" in message.text

print('successful')

browser.quit()

#Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.
#Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился, то получим StaleElementReferenceException.
#Например, мы нашли элемент Кнопка и через какое-то время решили выполнить с ним уже известный нам метод click. 
#Если кнопка за это время была скрыта скриптом, то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение.
#Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры),
# и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.