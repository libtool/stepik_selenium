import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
def calc(x, y):
  return int(x) + int(y)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    print(f"Значение x - {x}")
    print(f"Значение y - {y}")
    answer = calc(x, y)
    print(f"Значение answer - {answer}")
   
    selectes = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    selectes.select_by_value(str(answer))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
  
    

finally:
     time.sleep(30)
     browser.quit()

