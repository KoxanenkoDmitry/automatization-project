from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

"""Создание класса для действий на главной странице"""

class Main_page(Base):

    """указание родительского класса"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Локаторы"""

    authorization_button = "//button[@class='greyLink enterOpen']"
    email_field = "//input[@id='email']"
    password_field = "//input[@id='password']"
    login_button = "//input[@id='sign-in']"
    change_city_button = "//*[@id='city_open']"
    city_moscow = "/html/body/header/div[2]/form/div[2]/div/div[1]/a"

    """Способы получения получения локаторов (Get)"""

    def get_authorization_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.authorization_button)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_change_city_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.change_city_button)))

    def get_city_moscow(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_moscow)))


    """Создание действий (actions)"""

    def click_authorization_button(self):
        self.get_authorization_button().click()
        print("Нажата кнопка Вход")

    def send_keys_email(self, email):
        self.get_email_field().send_keys(email)
        print("Заполнено поле email")

    def send_keys_password(self, password):
        self.get_password_field().send_keys(password)
        print("заполнено поле пароль")

    def click_login_button(self):
        self.get_login_button().click()
        print("Нажата кнопка Войти")

    def click_change_city_button(self):
        self.get_change_city_button().click()

    def click_city_moscow(self):
        self.get_city_moscow().click()


    """Методы"""

    def enter_in_account(self, email, password):
        print("Начат Вход в аккаунт")
        self.click_authorization_button()
        self.send_keys_email(email)
        self.send_keys_password(password)
        self.click_login_button()
        print("Вход в аккаунт завершен успешно")

    def change_city(self):
        print("Процесс выбора города начат")
        self.click_change_city_button()
        self.click_city_moscow()
        print("Выбран город Москва")


