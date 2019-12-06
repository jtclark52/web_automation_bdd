import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pytest_bdd import scenario, given, when, then, parsers


driver = webdriver.Chrome("C:\Python Projects\Project 1\chromedriver.exe")

@given('The Wikipedia Home Page is displayed')
def wikipedia_home():
    driver.get("https://en.wikipedia.org")

@then('find search field')
def find_input():
    search = driver.find_element_by_id("searchInput")
    search.clear()

@then('Search "wake tech"')
def search():
    search.send_keys("wake tech")
    search.send_keys(Keys.RETURN)
    time.sleep(5)

    title = driver.title

    # print(title)
    assert title == "Wake Technical Community College - Wikipedia"
    driver.quit()
