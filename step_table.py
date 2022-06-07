
from msilib.schema import tables
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    time.sleep(3)
    button1.click()
    #print("ТЫК")
    
    #table = browser.window_handles

    new_table = browser.window_handles[1]
    
    browser.switch_to.window(new_table)



    x = browser.find_element(By.ID, "input_value").text
    print(f"x = {x}")
    y = calc(int(x))

    input = browser.find_element(By.NAME, "text")
    input.send_keys(y)

    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

        

finally:
     time.sleep(10)
     browser.quit()

