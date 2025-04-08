import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
time.sleep(3)

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(1)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
# print(len(countries))  # show you the number of countries in the list
for country in countries:
    if country.text == "India":
        country.click()
        break

time.sleep(3)