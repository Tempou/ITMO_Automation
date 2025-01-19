from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

def sauce_demo():
    login = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    submit = driver.find_element(By.XPATH, '//*[@id="login-button"]')

    if login is None and password is None and submit is None:
        print('Элементы не найдены')
    else:
        print('Элементы найдены')


sauce_demo()