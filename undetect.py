from time import sleep
import undetected_chromedriver as uc
if __name__ == "__main__":

    driver = uc.Chrome()


    driver.get('https://abrahamjuliot.github.io/creepjs/')
    sleep(100)