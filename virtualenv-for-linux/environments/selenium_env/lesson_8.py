from selenium import webdriver
import time
import os

with open("test.txt", "w") as file:
    content = file.write("automationpython")

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//input[@placeholder='Enter first name']")
    input1.send_keys("Firs name")
    
    input2 = browser.find_element_by_xpath("//input[@placeholder='Enter last name']")
    input2.send_keys("Last name")
    
    input3 = browser.find_element_by_xpath("//input[@placeholder='Enter email']")
    input3.send_keys("email.com")

    input_file = browser.find_element_by_xpath("//input[@id='file']")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    input_file.send_keys(file_path)

    button = browser.find_element_by_xpath("//button")
    button.click()


finally:
    time.sleep(5)
    browser.quit()

