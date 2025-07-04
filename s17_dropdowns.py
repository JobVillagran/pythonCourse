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

driver.find_element(By.ID, "autosuggest").send_keys("gua")
time.sleep(1)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
# print(len(countries))  # show you the number of countries in the list
for country in countries:
    if country.text == "Guatemala":
        country.click()
        break

time.sleep(3)
# This is how you can verify the selected country
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
# Comparison using assert
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "Guatemaalla"
