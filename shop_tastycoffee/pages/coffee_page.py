import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

"""Создание класса для действий на странице с выбором кофе"""


class Coffee_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver




        """локаторы"""


    coffee_catalog = "/html/body/header/div[1]/div/div[10]/div[1]/a"
    other_filters = "//*[@id='form-catalog-left']/div[1]/div[4]"
    filter_price = "//*[@id='form-catalog-left']/div[1]/div[1]/div/button/div"
    filter_price_to_decrease = "//*[@id='bs-select-1-1']/span[1]"
    filter_degree_of_roast = "//*[@id='form-catalog-left']/div[1]/div[2]/div[2]/button/div"
    filter_degree_of_roast_medium = "//*[@id='bs-select-2-1']/span[1]"
    filter_acidity = "//*[@id='form-catalog-left']/div[2]/div/div[3]/div[2]/button/div"
    filter_acidity_low = "//*[@id='bs-select-6-0']/span[1]"
    filter_acidity_medium = "//*[@id='bs-select-6-1']/span[1]"
    filter_processing_method = "//*[@id='form-catalog-left']/div[2]/div/div[6]/div[2]/button/div"
    filter_processing_method_washed = "//*[@id='bs-select-9-0']/span[1]"
    link_to_product = '//*[@id="catalog-products"]/div[1]/div[1]/form/div[3]/a'
    price_product_1 = "/html/body/div[2]/div[1]/div[2]/form/div/div/div/div/div[5]/div[4]/div[1]/label/a"
    name_product_1 = "/html/body/div[2]/div[1]/div[2]/form/div/div/div/div/h1"
    buy_product_1 = "/html/body/div[2]/div[1]/div[2]/form/div/div/div/div/div[5]/div[5]/a"
    continue_shopping = '/html/body/div[7]/div/button'
    go_to_cart_button = "//*[@id='openBasket']/span[1]"



    """Способы получения получения локаторов (Get)"""

    def get_coffee_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.coffee_catalog)))

    def get_other_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.other_filters)))

    def get_filter_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price)))

    def get_filter_price_to_decrease(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_to_decrease)))

    def get_filter_degree_of_roast(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_degree_of_roast)))

    def get_filter_degree_of_roast_medium(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_degree_of_roast_medium)))

    def get_filter_acidity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_acidity)))

    def get_filter_acidity_low(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_acidity_low)))

    def get_filter_acidity_medium(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_acidity_medium)))

    def get_filter_processing_method(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_processing_method)))

    def get_filter_processing_method_washed(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_processing_method_washed)))

    def get_name_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product_1)))

    def get_buy_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_product_1)))

    def get_go_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_button)))

    def go_to_product_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_to_product)))

    def go_to_continue_shopping(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_shopping)))

    """Создание действий (actions)"""

    def click_get_coffee_catalog(self):
        self.get_coffee_catalog().click()
        time.sleep(2)
        self.get_coffee_catalog().click()

    def click_get_other_filters(self):
        self.get_other_filters().click()

    def click_get_filter_price(self):
        self.get_filter_price().click()

    def click_get_filter_price_to_decrease(self):
        self.get_filter_price_to_decrease().click()

    def click_get_filter_degree_of_roast(self):
        self.get_filter_degree_of_roast().click()

    def click_get_filter_degree_of_roast_medium(self):
        self.get_filter_degree_of_roast_medium().click()

    def click_get_filter_acidity(self):
        self.get_filter_acidity().click()

    def click_get_filter_acidity_low(self):
        self.get_filter_acidity_low().click()

    def click_get_filter_acidity_medium(self):
        self.get_filter_acidity_medium().click()

    def click_get_filter_processing_method(self):
        self.get_filter_processing_method().click()

    def click_get_filter_processing_method_washed(self):
        self.get_filter_processing_method_washed().click()

    def text_price_product_1(self):
        find_price = self.driver.find_element(By.XPATH, self.price_product_1)
        read_price = find_price.text
        print("Цена товара " + read_price)
        return read_price


    def text_name_product_1(self):
        find_name = self.driver.find_element(By.XPATH, self.name_product_1)
        read_name = find_name.text
        print("Название товара " + read_name)

    def click_get_buy_product_1(self):
        self.get_buy_product_1().click()

    def click_go_to_cart_button(self):
        self.get_go_to_cart_button().click()

    def click_go_to_product_link(self):
        self.go_to_product_link().click()

    def click_go_to_continue_shopping(self):
        self.go_to_continue_shopping().click()





    """Методы"""

    def buy_product_1_with_filters(self):
        print("открытие каталога кофе")
        self.click_get_coffee_catalog()
        time.sleep(2)
        self.assert_url("https://shop.tastycoffee.ru/coffee")
        self.click_get_other_filters()
        self.click_get_filter_price()
        self.click_get_filter_price_to_decrease()
        self.click_get_filter_degree_of_roast()
        self.click_get_filter_degree_of_roast_medium()
        self.click_get_filter_acidity()
        self.click_get_filter_acidity_low()
        self.click_get_filter_acidity_medium()
        self.click_get_filter_processing_method()
        self.click_get_filter_processing_method_washed()
        self.click_get_filter_processing_method()
        time.sleep(2)
        self.click_go_to_product_link()
        self.text_price_product_1()
        self.text_name_product_1()
        self.click_get_buy_product_1()
        self.click_go_to_continue_shopping()
        self.click_go_to_cart_button()
        print("Открыта корзина")


