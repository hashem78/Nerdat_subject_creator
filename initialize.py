import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import constants

def execute():
    # Set up selenium
    driver = webdriver.Chrome(constants.DRIVER)


    # Navigate to website
    driver.get(constants.WEBSITE)

    # Find login button on main page and click it
    login_button = driver.find_element_by_xpath(constants.MAINLOGIN)
    login_button.click()


    # Find user name and password boxes in login page
    username_box = driver.find_element_by_xpath(constants.UNAME_BOX)
    password_box = driver.find_element_by_xpath(constants.PASS_BOX)
    user_login_button = driver.find_element_by_xpath(constants.ULOGIN_BUTTON)


    # Input user details
    username_box.send_keys(constants.USERNAME)
    password_box.send_keys(constants.PASSWORD)
    user_login_button.click()
    time.sleep(3)


    # Main page stuff
    faculty_drop_down = driver.find_element_by_xpath(constants.FACULTY_DROPDOWN)
    department_drop_down = driver.find_element_by_xpath(constants.DEPART_DROPDOWN)
    go_button = driver.find_element_by_xpath(constants.GO_BUTTON)


    # Load available options
    faculty_options = []
    faculty = constants.FACULTY
    faculty_drop_down_options = Select(faculty_drop_down).options


    department_options = []
    department = constants.DEPARTMENT
    for el in faculty_drop_down_options:
        faculty_options.append(el.text)
    print(faculty_options)
    # Make faculty selection
    if faculty in faculty_options:
        sel = Select(faculty_drop_down)
        sel.select_by_visible_text(faculty)


    # Make department selection
    sel = Select(department_drop_down)
    time.sleep(1)
    sel = sel.options


    for el in sel:
        department_options.append(el.text)
    if department in department_options:
        sel = Select(department_drop_down)
        print(sel.select_by_visible_text(department))
    go_button.click()