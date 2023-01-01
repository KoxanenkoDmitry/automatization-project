import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

"""Создание класса для действий на главной странице"""

class Search_page(Base):

    """указание родительского класса"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Локаторы"""
    search = "//*[@id='openSearch_h']"
    product_to_choose = "//div[@class ='nameTovar']/a[@ href='https://shop.tastycoffee.ru/coffee/espresso-guatemala-isauro-solares']"
    search_field = "//*[@id='search_h']"


    """Способы получения получения локаторов (Get)"""

    def get_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search)))

    def get_product_to_choose(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_to_choose)))

    def get_search_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field)))



    """Создание действий (actions)"""

    def click_search(self):
        self.get_search().click()
        print("Нажата кнопка поиска")

    def click_product_to_choose(self):
        self.get_product_to_choose().click()
        print("Открыта страница заданного товара")

    def send_search_field(self, product_name):
        self.get_search_field().send_keys(product_name)
        self.get_search_field().send_keys(Keys.RETURN)
        print("Осуществляется поиск")



    """Методы"""

    def check_search(self, product_name):
        print("Проверка поиска")
        self.click_search()
        self.send_search_field(product_name)
        time.sleep(3)
        self.click_product_to_choose()
        self.assert_url('https://shop.tastycoffee.ru/coffee/espresso-guatemala-isauro-solares')
        print("Товар найден в поиске")




