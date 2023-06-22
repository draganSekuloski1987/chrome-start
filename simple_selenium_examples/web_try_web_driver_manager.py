from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()))
driver.get("http://way2automation.com/")
driver.maximize_window()
title = driver.title
print(f"title = {title}")
assert "Selenium" in title
driver.close()
driver.quit()
