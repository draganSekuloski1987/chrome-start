from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.python.org/")
print(driver.title)
assert "Python" in driver.title
submit = driver.find_element(By.ID, "submit")
submit.click()