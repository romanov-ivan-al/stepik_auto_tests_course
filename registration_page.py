from selenium import webdriver
import time


def chek_page(link):
    #link = "ссылка на страницу"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

        # мой код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
    first_name.send_keys("Ivan")

    last_name = browser.find_element_by_css_selector("input[placeholder='Input your last name']")
    last_name.send_keys("Romanov")

    email = browser.find_element_by_css_selector("input[placeholder='Input your email']")
    email.send_keys("romanov@gmail.com")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

        # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

        # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
        # закрываем браузер после всех манипуляций
    browser.quit()

    return welcome_text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # ожидаемый результат assert "Congratulations! You have successfully registered!" == chek_page("http://suninjuly.github.io/registration1.html")


