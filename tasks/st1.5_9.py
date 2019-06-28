from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome('/chromedriver/chromedriver.exe')
browser.get(link)


# Ваш код, который заполняет обязательные поля
req_name = browser.find_element_by_css_selector('.first_block .first[required]')
req_surname = browser.find_element_by_css_selector('.first_block .second[required]')
req_email = browser.find_element_by_css_selector('.first_block .third[required]')

req_name.send_keys('name')
req_surname.send_keys('surname')
req_email.send_keys('em@i.l')

# Отправляем заполненную форму
time.sleep(2)
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

time.sleep(3)
browser.quit()
