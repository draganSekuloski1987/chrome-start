import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.firefox import GeckoDriverManager


def browser(web_browser):
    web_driver = ""
    if web_browser == "firefox":
        web_driver = webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()))
    else:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        web_driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    return web_driver


def page_open(web_driver, url):
    web_driver.get(url)
    web_driver.maximize_window()
    web_driver.implicitly_wait(20)

driver = browser("chrome")
page_open(driver, "https://echoecho.com/htmlforms11.htm")
wait = WebDriverWait(driver, 10)

# Dropdown form as standard "select" html element
example_dropdown = driver.find_element(By.NAME, "dropdownmenu")
example_dropdown.send_keys("Cheese")





