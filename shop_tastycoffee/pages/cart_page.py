import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

"""Создание класса для действий на главной странице"""

class Cart_page(Base):

    """указание родительского класса"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Локаторы"""

    send_friend_button = "/html/body/div[2]/div[2]/div/div[1]/div[1]/form[1]/div/div[7]/label/span"
    first_name_and_last_name_friend_field = '/html/body/div[2]/div[2]/div/div[1]/div[1]/form[1]/div/div[8]/div[1]/input[1]'
    telephone_friend_field = '/html/body/div[2]/div[2]/div/div[1]/div[1]/form[1]/div/div[8]/div[2]/input'
    comment_to_order = "//textarea[@placeholder='Комментарий к заказу ']"
    courier_button = "//label[contains(@class,'shipTab__link shipTab__link-courier ')]"
    post_button = "//label[contains(@class,'shipTab__link shipTab__link-pvz')]"
    pick_point_button_open = "//*[@id='shipTop']/div[4]/div[2]/label/div/div"
    pickpoint_button = "//a[@data-pvz='pickpoint']"
    choose_metro_pickpoint_field = "//input[@placeholder='Метро']"
    search_address_pickpoint_field = "//input[@placeholder = 'поиск...']"
    choose_place_button = "//*[@id='mCSB_7_container']/div/div[4]/div[2]/a[2]"
    price_in_cart = "//*[@id='basket-products']/div[1]/div/form/div/div[4]/p"
    name_in_cart = "//*[@id='basket-products']/div[1]/div/form/div/div[2]/p/a"
    clear_cart = "//*[@id='basket-products']/div[2]/a"

    """Способы получения получения локаторов (Get)"""

    def get_send_friend_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.send_friend_button)))

    def get_first_name_and_last_name_friend_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name_and_last_name_friend_field)))

    def get_telephone_friend_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.telephone_friend_field)))

    def get_comment_to_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.comment_to_order)))

    def get_courier_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.courier_button)))

    def get_post_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.post_button)))

    def get_pick_point_button_open(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_point_button_open)))


    def get_pickpoint_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pickpoint_button)))

    def get_choose_metro_pickpoint_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_metro_pickpoint_field)))

    def get_search_address_pickpoint_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_address_pickpoint_field)))

    def get_choose_place_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_place_button)))

    def get_price_in_cart(self):
        return self.driver.find_element(By.XPATH, self.price_in_cart)

    def get_name_in_cart(self):
        return self.driver.find_element(By.XPATH, self.name_in_cart)

    def get_clear_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clear_cart)))


    """Создание действий (actions)"""

    def click_send_friend_button(self):
        self.get_send_friend_button().click()
        print("Нажата кнопка отправить другу")

    def send_first_name_and_last_name_friend_field(self, first_name_friend, last_name_friend):
        self.get_first_name_and_last_name_friend_field().send_keys(first_name_friend, last_name_friend)
        print("введены данные Имя и Фамилия друга")

    def send_telephone_friend_field(self, telephone):
        self.get_telephone_friend_field().send_keys(telephone)
        print("ввод телефона друга в поле")

    def send_comment_to_order(self, comment):
        self.get_comment_to_order().send_keys(comment)
        print("Комментарий к заказу прописан")

    def click_courier_button(self):
        self.get_courier_button().click()
        self.get_courier_button().click()
        print("Выбрана доставка курьером")

    def click_post_button(self):
        self.get_post_button().click()
        self.get_post_button().click()
        print("Выбрана доставка в ПВЗ")

    def click_pick_point_button_open(self):
        self.get_pick_point_button_open().click()
        print("Выбрано поле ПВЗ Пикпоинт")

    def click_pickpoint_button(self):
        self.get_pickpoint_button().click()
        print("Открыто окно доставки Пикпоинт")

    def send_choose_metro_pickpoint_field(self, metro_name):
        self.get_choose_metro_pickpoint_field().send_keys(metro_name)
        self.driver.send_keys(Keys.RETURN)
        print("Заполнено поле Метро")

    def send_search_address_pickpoint_field(self, address):
        self.get_search_address_pickpoint_field().send_keys(address)
        self.driver.send_keys(Keys.RETURN)
        print("заполнено поле Адрес")

    def click_choose_place_button(self):
        self.get_choose_place_button().click()
        print("Выбран адрес доставки")

    def text_price_in_cart(self):
        cost_in_cart = self.get_price_in_cart().text
        print("Цена в корзине: " + cost_in_cart)
        return cost_in_cart


    def text_name_in_cart(self):
        name_in_cart = self.get_name_in_cart().text
        print("Цена в корзине: " + name_in_cart)

    def click_clear_cart(self):
        self.get_clear_cart().click()
        print("Корзина очищена")



    """Methods"""

    def choose_pvz_and_assert_pricename(self, first_name_value, last_name_value, telephone, comment, metro_name, address_field, price):
        time.sleep(4)
        self.assert_url("https://shop.tastycoffee.ru/basket")
        self.text_price_in_cart()
        self.text_name_in_cart()
        assert self.text_price_in_cart() == price      # цена указывается на странице теста искомого продукта
        self.click_send_friend_button()
        self.send_first_name_and_last_name_friend_field(first_name_value, last_name_value)
        self.send_telephone_friend_field(telephone)
        self.send_comment_to_order(comment)
        self.click_courier_button()
        self.click_post_button()
        self.get_screenshot()
        self.driver.refresh()
        self.click_clear_cart()
        self.driver.refresh()
        self.exit_account()

        # self.click_pickpoint_button()
        # self.send_choose_metro_pickpoint_field(metro_name) В данном локаторе опять присутствует элемент внутри #documents (писал Вам на почту насчет рекламы на прошлом сайте))
        # self.send_search_address_pickpoint_field(address_field)
        # self.click_choose_place_button()
        print("Заказ готов к оформлению")


