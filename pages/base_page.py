from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def logger(self, title):
        logger = logging.getLogger(title)
        fileHandler = logging.FileHandler('m43.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        formatter.datefmt="%Y-%m-%d %H:%M:%S"
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger


    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).click()

    def send_keys(self, locator, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).send_keys(value)

    def select_list(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        select = Select(element)
        select.select_by_visible_text("Option2")

    def get_attribute(self, locator):
        att_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).get_attribute("value")
        print(att_text)

    def autosuggest(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).send_keys("ga")

    def driver_title(self):
        return self.driver.title

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def mouse_action_hover(self, locator):
        mouse_action = ActionChains(self.driver)
        mouse_action.move_to_element(locator).perform()

    def alert_box_check(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()
        alert_obj = Alert(self.driver)
        time.sleep(3)
        alert_obj.accept()

    def scroll_window(self, value):
        self.driver.execute_script("window.scrollTo(0,"+value+")")

    # def mouse_action_dragdrop(self, source, destination):
    #     self.driver.find_element(source)
    #     self.driver.find_element(destination)
    #
    #     mouse_action = ActionChains(self.driver)
    #     mouse_action.drag_and_drop(source, destination)

    def windowa_handle(self, current_handle, all_handles, locator):
        current_handle = self.driver.current_window_handle

        for ac in all_handles:
            print(ac)
            if ac != current_handle:
                self.driver.switch_to.window(ac)

                time.sleep(3)
                print(self.driver.title)
                time.sleep(2)

    def add_table_column(self, locator):

        total = 0
        data = self.driver.find_elements(*locator)

        for i in data:
            total += int(i.text)
        print(total)

    def get_window_size(self):
        size = self.driver.get_window_size()
        print(size)

    def switch_to_iframe(self, locator):

        WebDriverWait(self.driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it(locator))

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def get_len_count(self, locator):
        data = self.driver.find_elements(*locator)
        print(len(data))


















































