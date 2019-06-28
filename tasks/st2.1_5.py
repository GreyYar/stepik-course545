from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome('/chromedriver/chromedriver.exe')
browser.get(link)


# Ваш код, который заполняет обязательные поля
x = browser.find_element_by_id('input_value')
x = x_element.get_attribute('valuex')
x = calc(x)

input_field = browser.find_element_by_id('answer')
input_field.send_keys(x)

robo_check1 = browser.find_element_by_id('robotCheckbox')
robo_check1.click()

robo_check2 = browser.find_element_by_id('robotsRule')
robo_check2.click()

time.sleep(1)

button1 = browser.find_element_by_css_selector('button.btn-default')
button1.click()

time.sleep(5)
browser.quit()
