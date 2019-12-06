from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\Python Projects\Project 1\chromedriver.exe")

def test_wikipedia():
    driver.get("https://en.wikipedia.org")
    search = driver.find_element_by_id("searchInput")
    search.clear()

    search.send_keys("wake tech")
    search.send_keys(Keys.RETURN)
    time.sleep(5)

    title = driver.title

    # print(title)
    assert title == "Wake Technical Community College - Wikipedia"
    driver.close()
