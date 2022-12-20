from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import logging

from tests.base_test import BaseTest





class TestLogin(BaseTest):

    # def test_username(self):
    #     self.loginPage.user_nm()
    # def test_password(self):
    #     self.loginPage.user_nm2()
    #
    #
    # #
    # # def test_driverh(self):
    # #     self.loginPage.driv()
    # #     time.sleep(2)
    #
    # def test_send_keysuser(self):
    #     self.loginPage.user_nm_keys()
    # def test_pass(self):
    #     self.loginPage.user_nm2_keys()
    #
    # time.sleep(5)

    def test_clear(self):
        self.loginPage.usrename_clear()
        time.sleep(3)

    def test_loginbutton(self):
        self.loginPage.login_button1()


    def test_drop_list(self):
        self.loginPage.drop()

    def test_hover(self):
        self.loginPage.mousehover_catalog1()
        time.sleep(2)

    def test_hover2(self):
        self.loginPage.mousehover_catalog1()
        time.sleep(2)

    def test_hover3(self):
        self.loginPage.mousehover_cataloggg()
        time.sleep(2)

    def test_h(self):
        self.loginPage.hover_pro()
        time.sleep(2)

    def test_h2(self):
        self.loginPage.hover_ca()
        time.sleep(2)




