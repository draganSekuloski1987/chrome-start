import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
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


driver = browser("firefox")
page_open(driver, "https://mail.google.com/")

# Elements and actions
username_input = driver.find_element(By.ID, "identifierId")
username_input.send_keys("trainer@way2automation.com")

input_next_button = driver.find_element(By.CSS_SELECTOR, "#identifierNext button")
input_next_button.click()

time.sleep(3)
password_input = driver.find_element(By.CSS_SELECTOR, "[id='password'] input")
password_input.send_keys("hello test")

password_next_button = driver.find_element(By.CSS_SELECTOR, "#passwordNext button")
password_next_button.click()

wrong_password_error_message_text = driver.find_element(By.XPATH, "//span[contains(text(),'Wrong password')]").text
assert wrong_password_error_message_text == "Wrong password. Try again or click Forgot password to reset it."

# Xpath selector of next button with ID contain partial text
# next_button = driver.find_element(By.XPATH, "//*[contains(@id, 'Next')]//button")
