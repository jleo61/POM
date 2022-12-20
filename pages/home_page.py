from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import logging
import openpyxl


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    log = By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    hide_options = By.XPATH, "//*[@id='nopSideBarPusher']"
    catalog_hover = By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/a/p"

    linkk = By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]"

    lisr = By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li/a/p"
    list2 = By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/ul/li/a/p"


    def move_to_catalog(self):
        j = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.catalog_hover))
        self.mouse_to_element(j)


    def clik(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.catalog_hover))
        self.driver.find_element(By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/a/p").click()
        time.sleep(2)

    def lnk(self):
        self.link_text(self.catalog_hover)

    # def l(self):
    #     lis = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.lisr))
    #
    #     for ac in lis:
    #         print(ac.text)

    def dr(self):
        self.drop_down_lists_get(self.lisr)


    def move_to_catal(self):
        j = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.linkk))
        self.mouse_to_element(j)

    def cl(self):
        time.sleep(2)
        self.click(self.linkk)
        time.sleep(2)

    def dr2(self):
        self.drop_down_lists_get(self.list2)















