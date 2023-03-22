from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')

session = driver.get("https://reqres.in")

time.sleep(40)

element = session.find_element_by_xpath("//li[@data-id='users-single-not-found']")

element.click()