import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def google_login(email, psw):
    url = 'https://accounts.google.com'
    driver = webdriver.Chrome()
    driver.get(url)
    button = driver.find_element(By.CLASS_NAME, 'VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ')
    try:
        # Sent email
        driver.find_element(By.ID, 'identifierId').send_keys(email)
        button.click()
        time.sleep(5)
        # Sent psw
        driver.find_element(By.CLASS_NAME, 'whsOnd.zHQkBf').send_keys(psw)
        button.click()
    except NoSuchElementException:
        print('Something going wrong')
