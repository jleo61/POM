from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest


# @pytest.fixture(autouse=True)
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()



    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.implicitly_wait(20)
    driver.maximize_window()
    request.cls.loginPage = LoginPage(driver)
    request.cls.homePage = HomePage(driver)

    request.cls.driver = driver
    request.cls.basePage = BasePage(driver)

    yield
    driver.close()



