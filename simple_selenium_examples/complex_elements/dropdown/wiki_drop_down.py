import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select


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
page_open(driver, "https://www.wikipedia.org/")
wait = WebDriverWait(driver, 10)

# Dropdown form as standard "select" html element
dropdown = driver.find_element(By.ID, "searchLanguage")
select = Select(dropdown)
select.select_by_visible_text("Eesti")
select.select_by_value("hi")

# print all selected options from a dropdown from a select
# for option in select.options:
#     print(option.text)


# find all elements within the select element
all_language_dropdown_options = driver.find_elements(By.CSS_SELECTOR, "#searchLanguage option")
for option in all_language_dropdown_options:
    pass
    # print(f"option text: {option.text} - attribute value: {option.get_attribute('value')} - attribute lang: {option.get_attribute('lang')}")
print(f"total dropdown values count {len(all_language_dropdown_options)}")


# find all elements within the select element
all_links = driver.find_elements(By.CSS_SELECTOR, "a[href]")
for link in all_links:
    pass
    # print(f"link text: {link.text} - attribute value: {link.get_attribute('href')}")
print(f"total links count {len(all_links)}")


project_block = driver.find_element(By.CSS_SELECTOR, "div.other-projects")
project_links = project_block.find_elements(By.TAG_NAME, "a")

print(f"project links count {len(project_links)}")

first_link = project_links.__getitem__(0).text
print(f"First link: {first_link}")


for link in project_links:
    print(f"link text: {link.text} - attribute value: {link.get_attribute('href')}")
driver.quit()
