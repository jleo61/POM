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


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    username = By.XPATH, "//*[@id='Email']"
    password = By.XPATH, "//*[@id='Password']"
    login_button = By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    invalid_credential = By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p"

    catalog = By.XPATH, "//*[@id='nopSideBarPusher']"

    catalogg = By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/a"

    productt = By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[1]/a"

    catagories = By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[2]/a/p"

    dashboard_list = By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li"









    # def drag_n_drop(self):
    #     self.mouse_action_dragdrop(source, destination)

    def select_from_list(self):
        self.select_list(self.select_list1)

    def window_switch(self):
        current_handle1 = self.driver.current_window_handle
        print(current_handle1)

        # self.click(self.windo_switch_button)

        all_handles = self.driver.window_handles

        self.windowa_handle(current_handle1, all_handles, self.windo_switch_button)




        self.driver.close()

        self.driver.switch_to.window(current_handle1)

    def window_switch2(self):
        current_handle1 = self.driver.current_window_handle
        print(current_handle1)

        # self.click(self.windo_switch_button)

        all_handles = self.driver.window_handles

        self.windowa_handle(current_handle1, all_handles, self.windo_switch_button)

        self.click(self.close_button)
        self.click(self.course_button)
        time.sleep(2)




        self.driver.close()

        self.driver.switch_to.window(current_handle1)




    def switch_to_iframe1(self):

        self.switch_to_iframe(self.iframe_xpath1)

        # clicking a button inside iframe
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.iframe_button_check))

        self.click(self.iframe_button_check)

        time.sleep(2)


    def logger1(self):
        loger = self.logger("critical")
        loger.critical("sdsdaf")
        loger.warning("ggggg")



    def date_picker1(self):
        self.date_picker(self.datebutton, self.datetry2, self.nextdaye)
        self.click(self.date_choice)
        self.click(self.done_button)
        time.sleep(5)


    def usrename_clear(self):
        self.clear(self.username)
        self.send_keys(self.username, "admin@yourstore.com")
        self.clear(self.password)
        self.send_keys(self.password, "admin")

    def mousehover_catalog1(self):
        self.click(self.catalog)
        time.sleep(2)

    def login_button1(self):
        self.click(self.login_button)

    def mousehover_catalog(self):
        self.click(self.catalog)
        time.sleep(2)

    def mousehover_cataloggg(self):
        self.click(self.catalogg)
        time.sleep(2)


    def hover_pro(self):
        self.mouse_to_element(self.productt)

    def drop(self):
        self.drop_down_lists_get(self.dashboard_list)


    def hover_ca(self):
        self.mouse_to_element(self.catagories)
        loger = self.logger("critical")
        loger.critical("sdsdaf")
        loger.warning("ggggg")
        loger.warning('%s raised an error', "kkkkkkkkkkkk")

























































