import re
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
import random
from locators import *

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_driver_path = '/Users/shahardvora/PycharmProjects/homeAssignment/Assignment/chromedriver'
service = Service(chrome_driver_path)


def choose_user():
    filename = open('/Users/shahardvora/PycharmProjects/homeAssignment/Assignment/users.json')
    user_file = json.load(filename)
    return random.choice(user_file)


def only_numbers_list(my_list):
    numbers = []
    for var in my_list:
        found_numbers = re.findall(r'[\d,]+\.?\d*', var.text)
        numbers.extend(float(num.replace(',', '')) for num in found_numbers)

    return numbers


def is_ascending(my_list):
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            return False

    return True


def assignment():
    counter = 0
    user = choose_user()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver=driver, timeout=30)
    driver.get('https://www.terminalx.com/')
    print("Enter to website.")
    connect = wait.until(EC.visibility_of_element_located((By.XPATH, connect_title)))
    connect.click()
    email_ = wait.until(EC.visibility_of_element_located((By.XPATH, email_field)))
    email_.click()
    email_.send_keys(user['username'])
    password_ = wait.until(EC.visibility_of_element_located((By.XPATH, password_field)))
    password_.click()
    password_.send_keys(user['password'])
    driver.find_element(By.XPATH, connect_button).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, greeting_text)))
    wait.until(EC.invisibility_of_element_located((By.XPATH, loader_screen)))
    search_btn = wait.until(EC.visibility_of_element_located((By.XPATH, search_button)))
    search_btn.click()
    search_txt = wait.until(EC.visibility_of_element_located((By.XPATH, search_text)))
    search_txt.click()
    search_txt.send_keys('hello')
    wait.until(EC.visibility_of_element_located((By.XPATH, search_results)))
    search_res = driver.find_elements(By.XPATH, search_results)
    counter_search_results = search_res.__len__()
    price_res = driver.find_elements(By.XPATH, price_results)
    price_list = only_numbers_list(price_res)
    list_is_ascending = is_ascending(price_list)

    for result in search_res:
        if "hello kitty" in result.text.lower():
            counter += 1

    print(f'===> Search results for hello kitty {counter} from {counter_search_results}.')
    print(f'===> Alerts is ascending by price ? = {list_is_ascending}.')
    info_res = driver.find_elements(By.XPATH, picture_results)
    info_res[2].click()
    price_text = wait.until(EC.visibility_of_element_located((By.XPATH, price_page)))
    font_size = price_text.value_of_css_property('font-size')

    if font_size == '1.8rem':
        print(f'===> Yes the font size of the text price is: {font_size}.')
    else:
        print(f'===> No the font size of the text price is: {font_size}.')

    print('===> Assignment tested successfully.')


assignment()
