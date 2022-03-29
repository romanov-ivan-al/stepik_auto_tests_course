import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



links =[
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"
]

#@pytest.mark.parametrize('links')
def find_message(links):
    for link in links:
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        browser.implicitly_wait(15)
        browser.get(link)
        
        answer = math.log(int(time.time()))
        text_input = browser.find_element_by_tag_name('textarea')
        text_input.send_keys(str(answer))
        
        button = browser.find_element(By.CLASS_NAME, "submit-submission")
        button.click()
        time.sleep(15)
        print("\nquit browser..")
        browser.quit()

find_message(links)