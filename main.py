import time
import math
import os

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from math import *


link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(log(abs(12*sin(int(x)))))

try:
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element(By.ID, 'book').click()

    x_val = browser.find_element(By.ID, 'input_value')
    x = x_val.text

    input_2 = browser.find_element(By.CSS_SELECTOR, '[name="text"]')
    input_2.send_keys(calc(x))

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(15)
    browser.quit()




















# link = 'http://suninjuly.github.io/redirect_accept.html'
#
# browser = webdriver.Chrome()
# browser.get(link)
#
# def calc(x):
#     return str(log(abs(12*sin(int(x)))))
#
# try:
#     button_1 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#
#     window_2 = browser.window_handles[1]
#     browser.switch_to.window(window_2)
#
#     x_val = browser.find_element(By.ID, 'input_value')
#     x = x_val.text
#
#     input_2 = browser.find_element(By.CSS_SELECTOR, '[name="text"]')
#     input_2.send_keys(calc(x))
#
#     browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#
# finally:
#     time.sleep(20)
#     browser.quit()


















# link = 'http://suninjuly.github.io/alert_accept.html'
#
# browser = webdriver.Chrome()
# browser.get(link)
#
# def calc(x):
#     return str(log(abs(12*sin(int(x)))))
#
# try:
#     button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#
#     alert = browser.switch_to.alert
#     alert.accept()
#
#     x_val = browser.find_element(By.ID, 'input_value')
#     x = x_val.text
#
#     input_2 = browser.find_element(By.CSS_SELECTOR, '[name="text"]')
#     input_2.send_keys(calc(x))
#
#     browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#
# finally:
#     time.sleep(20)
#     browser.quit()





















# link = 'http://suninjuly.github.io/file_input.html'
#
# browser = webdriver.Chrome()
# browser.get(link)
#
# try:
#     first_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
#     first_name.send_keys('Georgiy')
#
#     last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
#     last_name.send_keys('Zakirov')
#
#     email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
#     email.send_keys('granmawinter@gmail.com')
#
#     with open("some_txt.txt", "w") as file:
#         file.write("Некий случайный никому не нужный текст")
#
#     folder_path = os.path.abspath(os.path.dirname(__file__))
#     file_path = os.path.join(folder_path, 'some_txt.txt')
#
#     send_file = browser.find_element(By.CSS_SELECTOR, '[name="file"]')
#     send_file.send_keys(file_path)
#
#     browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#
# finally:
#     time.sleep(20)
#     browser.quit()












# link = 'https://SunInJuly.github.io/execute_script.html'
#
# browser = webdriver.Chrome()
# browser.get(link)
#
#
# def calc(x):
#     return str(log(abs(12*sin(int(x)))))
#
#
# try:
#     find_x = browser.find_element(By.ID, 'input_value')
#     x = find_x.text
#
#     input_search = browser.find_element(By.TAG_NAME, 'input')
#     browser.execute_script("return arguments[0].scrollIntoView(true)", input_search)
#     input_search.send_keys(calc(x))
#
#     browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()
#
#     browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()
#
#     browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#
# finally:
#     time.sleep(20)
#     browser.quit()

















# link = 'https://suninjuly.github.io/selects1.html'
#
# browser = webdriver.Chrome()
# browser.get(link)
#
# try:
#     num1 = browser.find_element(By.ID, 'num1')
#     num1_val = num1.text
#     num2 = browser.find_element(By.ID, 'num2')
#     num2_val = num2.text
#
#     dropdown = Select(browser.find_element(By.TAG_NAME, 'select'))
#     sum_nums = int(num1_val) + int(num2_val)
#
#     dropdown.select_by_value(str(sum_nums))
#
#     button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
#     button.click()
# finally:
#     time.sleep(20)
#     browser.quit()
















# link = 'http://suninjuly.github.io/get_attribute.html'
#
#
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     search_elem = browser.find_element(By.ID, 'treasure')
#     x = search_elem.get_attribute('valuex')
#
#     sin_x = calc(x)
#
#     input_1 = browser.find_element(By.ID, 'answer')
#     input_1.send_keys(sin_x)
#
#     search_checkBox = browser.find_element(By.ID, 'robotCheckbox')
#     search_checkBox.click()
#
#     search_radio = browser.find_element(By.ID, 'robotsRule')
#     search_radio.click()
#
#     button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
#     button.click()
#
# finally:
#     time.sleep(30)
#     browser.quit()












# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.TAG_NAME, 'input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, 'last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, 'country')
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     time.sleep(30)
#     browser.quit()


