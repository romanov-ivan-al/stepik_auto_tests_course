from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_id("book")
    button.click()

    x = int(browser.find_element_by_id("input_value").text)
    func = math.log(abs(12*math.sin(x)))

    s = browser.find_element_by_id("answer")
    s.send_keys(str(func))

    button2 = browser.find_element_by_id("solve")
    button2.click()

finally:
    time.sleep(5)
    browser.quit()

