import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

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

"""
@pytest.mark.parametrize('links')
def find_message(links):
    for link in links:
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        browser.get(link)
        answer = math.log(int(time.time()))
        text_input = browser.find_elements_by_id("ember97")
        text_input.send_keys(str(answer))
        time.sleep(2)
        button = browser.find_element_css_selector("[class=summit-submission]")
        print("\nquit browser..")
        browser.quit()
"""

def find_message(links):
    for link in links:
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        browser.implicitly_wait(30)
        browser.get(link)
        
        answer = math.log(int(time.time()))
        #text_input = browser.find_element_by_id("ember98")
        text_input = browser.find_element(By.ID, "ember98")
        text_input.send_keys(answer)
        
        button = browser.find_element_css_selector("[class=summit-submission]")
        print("\nquit browser..")
        browser.quit()

find_message(links)