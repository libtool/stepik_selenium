from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, value="input" )
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, value="last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, value="city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, value="country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    

finally:
     time.sleep(30)
     browser.quit()

