import math
import time
from tkinter import Button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()


    x = browser.find_element(By.ID, "input_value").text
    
    y = calc(int(x))

    input = browser.find_element(By.NAME, "text")
    input.send_keys(y)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

        

finally:
     time.sleep(30)
     browser.quit()

