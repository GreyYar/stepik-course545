from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


# Ваш код, который заполняет обязательные поля
req_name = browser.find_element_by_name('firstname')
req_surname = browser.find_element_by_name('lastname')
req_email = browser.find_element_by_name('email')

req_name.send_keys('name')
req_surname.send_keys('surname')
req_email.send_keys('em@i.l')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'empty.txt')
print(file_path)

upload_button = browser.find_element_by_id('file')
upload_button.send_keys(file_path)

button1 = browser.find_element_by_css_selector('button.btn')
browser.execute_script("return arguments[0].scrollIntoView(true);", button1)

button1.click()

time.sleep(50)
browser.quit()
