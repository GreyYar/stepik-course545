from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)

text_selector = browser.find_element_by_class_name('price_color')
print(text_selector.text)


# price_time = WebDriverWait(browser, 15).until(
#     expected_conditions.text_to_be_present_in_element((By.ID, "price"), '10000')
# )
# browser.find_element_by_id('book').click()
#
#
# button1 = browser.find_element_by_id('solve')
# browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
# x = browser.find_element_by_id('input_value').text
#
# browser.find_element_by_id('answer').send_keys(calc(x))
#
# button1.click()



# alerty = browser.switch_to.alert
# alerty.accept()

# time.sleep(0.5)
#
# first_window = browser.window_handles[0]
# second_window = browser.window_handles[1]
#
# browser.switch_to.window(second_window)
#
# x = browser.find_element_by_id('input_value').text
#
# fill_field = browser.find_element_by_id('answer')
# fill_field.send_keys(calc(x))

# req_name = browser.find_element_by_name('firstname')
# req_surname = browser.find_element_by_name('lastname')
# req_email = browser.find_element_by_name('email')
#
# req_name.send_keys('name')
# req_surname.send_keys('surname')
# req_email.send_keys('em@i.l')
#
# current_dir = os.path.abspath(os.path.dirname(__file__))
# file_path = os.path.join(current_dir, 'empty.txt')
# print(file_path)
#
# upload_button = browser.find_element_by_id('file')
# upload_button.send_keys(file_path)
#
# button1 = browser.find_element_by_css_selector('button.btn')
# browser.execute_script("return arguments[0].scrollIntoView(true);", button1)

# button2 = browser.find_element_by_css_selector('button.btn')
# button2.click()

time.sleep(50)
browser.quit()
