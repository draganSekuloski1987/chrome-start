from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://mail.google.com/")
driver.maximize_window()
title = driver.title
username_input = driver.find_element(By.ID, "identifierId")
username_input.send_keys("trainer@way2automation.com")
next_button = driver.find_element(By.CSS_SELECTOR, "#identifierNext button")
next_button.click()



# //*[@id="identifierNext"]/div/button/span