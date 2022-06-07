import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "#treasure")
    #print(f"Значение поля - {input1.text}")
    sunduk = input1.get_attribute("valuex")
    print(f"Значение сундука - {sunduk}")
    y = calc(sunduk)
    input2 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input2.send_keys(y)
    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
  
    

finally:
     time.sleep(30)
     browser.quit()

