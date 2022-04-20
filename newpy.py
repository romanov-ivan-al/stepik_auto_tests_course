from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox("/home/ria/stepik_auto_tests_course/programs_for_linux")

driver.get("https://stepik.org/lesson/25969/step/8")