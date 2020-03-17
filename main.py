from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

import time
import initialize
import constants

# Set up selenium
driver = webdriver.Chrome(constants.DRIVER)

def navigate_to(path):
    driver.get(path)
    time.sleep(3)

def add_post(course_tag,type="Notes",title = "Default title",content = "Place Holder"):
    navigate_to("https://nerdat.net/course/"+course_tag)
    write_post_button = driver.find_element_by_xpath("//*[@id='app']/div/main/div/div/div[1]/a[1]")
    write_post_button.click()
    time.sleep(3)
    # Set note type
    type_dropdown = driver.find_element_by_xpath("//*[@id='app']/div/main/div/form/div/article/div[1]/div[2]/div[1]/div/select")
    Select(type_dropdown).select_by_visible_text(type)

    # Fill title
    course_title = driver.find_element_by_xpath("//*[@id='app']/div/main/div/form/div/article/div[1]/div[2]/div[2]/input")
    course_title.send_keys(title)

    # Fill content
    course_content = driver.find_element_by_xpath("//*[@id='app']/div/main/div/form/div/article/div[1]/div[3]/div/div/p")
    course_content.send_keys(content)

    time.sleep(5)
    # Publish content
    course_publish = driver.find_element_by_xpath("//*[@id='app']/div/main/div/form/div/div/button[1]")
    course_publish.click()

def main():
    initialize.execute(driver)
    add_post("CPE200","Notes","This is a test title","This is test content")
main()