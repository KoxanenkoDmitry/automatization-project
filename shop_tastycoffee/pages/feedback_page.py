from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

"""Создание класса для действий на странице с обратной связью"""
class Feedback_page(Base):
    def __init__(self, driver):
        super().__init__(driver)

    """локаторы"""

    read_list = "/html/body/header/div[1]/div/div[8]/div[4]/a"
    read_list_often_question = "/html/body/header/div[1]/div/div[8]/div[4]/ul/li[2]/a"
    name_field = "//div[@class='input-wrap indent']/input[@placeholder='Имя']"
    telephone_of_email_field = "//div[@class='input-wrap indent']/input[@placeholder='Телефон или e-mail']"
    textarea = "//textarea[@placeholder='Ваш вопрос']"

    """Способы получения получения локаторов (Get)"""


    def get_read_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.read_list)))

    def get_read_list_often_question(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.read_list_often_question)))


    def get_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_field)))


    def get_telephone_of_email_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.telephone_of_email_field)))

    def get_textarea(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.textarea)))

    """Создание действий (actions)"""

    def click_read_list(self):
        self.get_read_list().click()
        self.get_read_list_often_question().click()
        print("Открыта старница обратной связи")

        print("емаил/телефон прописан")

    def send_name_in_form(self, name):
        self.get_name_field().send_keys(name)
        print("Имя вписано в форму")

    def send_get_telephone_of_email_field(self, email):
        self.get_telephone_of_email_field().send_keys(email)
        print("емаил/телефон прописан")

    def send_get_textarea(self, comment):
        self.get_textarea().send_keys(comment)
        print("Поле ввода вопроса заполнено")


    """Методы"""


    def fill_feedback_form(self, name, email, comment):
        self.click_read_list()
        self.send_name_in_form(name)
        self.send_get_telephone_of_email_field(email)
        self.send_get_textarea(comment)
        print("Форма обратной связи заполнена")


