from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")
time.time(5)
browser.close()