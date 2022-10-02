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


    username = By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    password = By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    login_button = By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    invalid_credential = By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p"



    radio_button_xpath = By.XPATH, "//div[@id = 'radio-btn-example']/fieldset/label[2]/input"
    seggestion1_xpath = By.XPATH, "//*[@id='autocomplete']"
    dro_down_optio = By.XPATH, "//*[@id='dropdown-class-example']"
    check_box1 = By.XPATH, "//*[@id='checkBoxOption1']"
    windo_switch = By.XPATH, "//*[@id='openwindow']"
    choice = ["us", "eth", "au", "eng", "eri"]
    alert_xpath = By.XPATH, "//*[@id='alertbtn']"
    table_amount = By.XPATH, "//div[@class = 'tableFixHead']/table/tbody/tr/td[4]"
    mouse_hover = By.XPATH, "/html/body/div[4]/div/fieldset/div"
    new_tab = By.XPATH, "//*[@id='opentab']"
    iframe_xpath = By.XPATH, "//*[@id='courses-iframe']"
    select_list1 = By.XPATH, "//*[@id='dropdown-class-example']"


    windo_switch_button = By.XPATH, "//*[@id='openwindow']"
    new_window_button = By.XPATH, "//*[@id='homepage']/div[4]/div[2]/div/div/div/span/div/div[6]/div/div/button"
    course_button = By.XPATH, "//*[@id='homepage']/header/div[2]/div/nav/ul/li[2]/a"
    close_button =By.XPATH, "//*[@id='homepage']/div[4]/div[2]/div/div/div/span/div/div[7]/div/div/div[2]"


    hide_element = By.XPATH, "//*[@id='hide-textbox']"
    show_element = By.XPATH, "//*[@id='show-textbox']"


    open_new_tab = By.XPATH, "//*[@id='opentab']"

    table_column_data = By.XPATH, "//*[@id='product']/tbody/tr/td[4]"

    iframe_xpath1 = By.XPATH, "//*[@id='courses-iframe']"
    iframe_button_check = By.XPATH, "/html/body/div/header/div[2]/div/div/div[2]/div[2]/a"
    mentorship_button = By.XPATH, "/html/body/div/header/div[3]/div/div/div[2]/nav/div[2]/ul/li[5]/a"


    datebutton = By.XPATH, "//*[@id='date_form_field-btn']"
    datetry = By.XPATH, "//h2[@class = 'uitk-date-picker-month-name uitk-type-medium']"
    nextdaye = By.XPATH, "//*[@id='lodging_search_form']/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/button[2]"
    datetry2 = By.XPATH, "//*[@id='lodging_search_form']/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[1]/h2"
    date_choice = By.XPATH, "//*[@id='lodging_search_form']/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[2]/td[3]/button"
    done_button = By.XPATH, "//*[@id='lodging_search_form']/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/button"

    confirm_date = By.XPATH, "//*[@id='submit_button']"




    log = By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"


    #orangehrm login test

    new_tab_course_button = By.XPATH, "/html/body/div/header/div[3]/div/div/div[2]/nav/div[2]/ul/li[2]/a"

    iterable_table_xpath = By.XPATH, "//div[@class='left-align']/fieldset/table/tbody/tr[2]/td[1]"
    col_num = By.XPATH, "//div[@class='left-align']/fieldset/table/tbody/tr[2]/td"
    row_num = By.XPATH, "//div[@class='left-align']/fieldset/table/tbody/tr"








    def print_title(self):
        print(self.driver_title())
        assert self.driver_title() == "Practice Page"

    def check_box(self):
        self.click(self.check_box1)


    def radio_button_options(self):
        self.click(self.radio_button_xpath)
        time.sleep(2)



    def mouse_hover_element(self):
        self.mouse_action_hover(self.mouse_hover)
        time.sleep(2)

    # def drag_n_drop(self):
    #     self.mouse_action_dragdrop(source, destination)

    def select_from_list(self):
        self.select_list(self.select_list1)

    def alert_box(self):
        self.alert_box_check(self.alert_xpath)

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

    def back_towin(self):

        time.sleep(2)
        self.click(self.hide_element)
        time.sleep(2)

    def show_element_button(self):
        time.sleep(2)
        self.click(self.show_element)
        time.sleep(3)

    def open_tab(self):
        self.click(self.open_new_tab)

    def new_win(self):
        self.click(self.windo_switch_button)

    def new_wind_course_button(self):

        time.sleep(10)
        self.click(self.new_window_button)
        time.sleep(5)

    def new_wind_course_button2_course_button(self):

        time.sleep(10)
        self.click(self.course_button)
        time.sleep(5)

    def add_table_column_data(self):
        self.add_table_column(self.table_column_data)

    def switch_to_iframe1(self):

        self.switch_to_iframe(self.iframe_xpath1)

        # clicking a button inside iframe
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.iframe_button_check))

        self.click(self.iframe_button_check)

        time.sleep(2)

    def click_membership_inside_frame(self):
        self.click(self.mentorship_button)
        time.sleep(3)

    def switch_to_default_content1(self):
        self.switch_to_default_content()

    def get_count_len(self):
        self.get_len_count(self.table_column_data)
        self.logger("get_count_len").warning("Couldn't get the length")
        self.save_screenshot("try.png")


    def logger1(self):
        loger = self.logger("critical")
        loger.critical("sdsdaf")
        loger.warning("ggggg")

    def getall_cookies(self):
        self.get_cookies()
        self.logger("Number of cookies").info(self.get_cookies())

    def delet_all_cookies1(self):
        self.delet_all_cookies()

    def get_len_count1(self):
        self.get_len_count()


    def date_picker1(self):
        self.date_picker(self.datebutton, self.datetry2, self.nextdaye)
        self.click(self.date_choice)
        self.click(self.done_button)
        time.sleep(5)

    def excel_row_count(self):

        self.excel_get_row_count(self.excel_path)

    def excel_coluumn_count(self):

        self.excel_get_column_count(self.excel_path)

    def excel_table_scraping(self):
        self.table_data_scrapping_to_excel()

    def link_text_search(self):
        self.link_text("LOG IN")

    def login_new(self):
        self.click(self.log)



    def login_multiple_excel(self):

        self.simple_login_from_Excel()

    def get_att(self):
        self.get_attribute(self.seggestion1_xpath)

    def backspace(self):
        loc = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.seggestion1_xpath))
        self.back_space(loc)

    def auto_sugggest(self):
        self.click(self.seggestion1_xpath)
        self.send_keys(self.seggestion1_xpath, "123456")

        time.sleep(2)
        self.backspace()
        time.sleep(2)

    def radio_b(self):
        self.click(self.radio_button_xpath)

    def aauto(self):
        self.send_keys(self.seggestion1_xpath, "eth")
        time.sleep(2)
        self.clear_text_box(self.seggestion1_xpath)

    def dro_dn(self):
        self.select_list(self.dro_down_optio).select_by_visible_text("Option3")

    def wn(self):
        current_handle1 = self.driver.current_window_handle
        print(current_handle1)
#click new window button
        # self.click(self.windo_switch_button)

        all_handles = self.driver.window_handles


#switch to tne new window or tab using the basepage function
        self.windowa_handle(current_handle1, all_handles, self.new_tab)


# new window interaction
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.new_tab_course_button)).click()

        self.driver.close()
        self.driver.switch_to.window(current_handle1)

    def alrt(self):
        self.alert_box_accept(self.alert_xpath)

    def exc(self):
        self.excel_table_data_scrapping_to_excel()


    def scroll_windowto(self):
        self.scroll_window("1110")
        time.sleep(2)

    def swit(self):
        self.switch_to_iframe(self.iframe_xpath)

    def fr(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.iframe_button_check)).click()

    def switch_to_default_contentl1(self):

        self.switch_to_default_content()
















































