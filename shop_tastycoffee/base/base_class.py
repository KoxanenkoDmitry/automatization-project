import datetime

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


"""Создание класса Base, куда будут вноситься основные действия вне зависимости от страницы"""

class Base():

    """Указание обязательных аттрибутов"""

    def __init__(self, driver):
        self.driver = driver


    def get_url(self):
        current_url = self.driver.get.current_url
        print("Current URL : " + current_url)

    def assert_url(self, url):
        self.url = url
        get_current_url = self.driver.current_url
        assert get_current_url == self.url
        print("url assert is ok")


    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\koxan\\PycharmProjects\\shop_tastycoffee\\screenshots\\' + name_screenshot)


    def exit_account(self):

        """Выход из аккаунта, не знал куда его определить"""
        exit_account_button = self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div[7]/div/a[3]")
        exit_account_button.click()

