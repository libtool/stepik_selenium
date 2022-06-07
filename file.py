import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'res.txt')


try:
    browser = webdriver.Chrome()
    browser.get(link)

    fname = browser.find_element(By.NAME, "firstname")
    fname.send_keys("Yuriy")
    lname = browser.find_element(By.NAME, "lastname")
    lname.send_keys("Istomin")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("yu.istomin@gmail.com")
    file = browser.find_element(By.ID, "file")
    file.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
 
        

finally:
     time.sleep(30)
     browser.quit()

