import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from pages.cart_page import Cart_page
from pages.coffee_page import Coffee_page
from pages.feedback_page import Feedback_page
from pages.main_page import Main_page
from pages.search_page import Search_page
from utilites.conftest import start_and_end_tests

def test_buy_coffee(start_and_end_tests):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\koxan\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    base_url = 'https://shop.tastycoffee.ru/'
    driver.get(base_url)
    driver.maximize_window()

    email = 'koxanenkodmitry@mail.ru'
    password = 'KoxanenkoDA'
    first_name_value = 'Dmitry '
    last_name_value = 'Koxanenko'
    telephone = '9605384164'
    comment = 'Test Test Test Test'
    metro_name = 'Волоколамская'
    address_field = 'Новотушинский проезд, д. 6, к. 1'
    price = '519 ₽'


    mp = Main_page(driver)
    mp.enter_in_account(email, password)
    time.sleep(1)

    cp = Coffee_page(driver)
    cp.buy_product_1_with_filters()

    cart = Cart_page(driver)
    cart.choose_pvz_and_assert_pricename(first_name_value, last_name_value, telephone, comment, metro_name, address_field, price)
    print("test 1 passed")

    driver.quit()

def test_feedback(start_and_end_tests):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\koxan\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    base_url = 'https://shop.tastycoffee.ru/'
    driver.get(base_url)
    driver.maximize_window()

    base_url = 'https://shop.tastycoffee.ru/'
    driver.get(base_url)
    driver.maximize_window()


    email = 'koxanenkodmitry@mail.ru'
    name = 'Dmitry '
    comment = 'Test Test Test Test'

    fb = Feedback_page(driver)
    fb.fill_feedback_form(name, email, comment)
    print("test 2 passed")


    driver.quit()

def test_search(start_and_end_tests):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\koxan\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    base_url = 'https://shop.tastycoffee.ru/'
    driver.get(base_url)
    driver.maximize_window()

    product_name = 'Гватемала'


    sp = Search_page(driver)
    sp.check_search(product_name)
    print("test 3 passed")

    driver.quit()

