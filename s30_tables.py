import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
time.sleep(2)

browserSorterVeggies = []

driver.find_element(By.CSS_SELECTOR, "th:nth-child(1)").click()

veggieList = driver.find_elements(By.XPATH, "//tr/td[1]")
for veggie in veggieList:
    browserSorterVeggies.append(veggie.text)
    browserSorterVeggies.sort()
print(browserSorterVeggies)

time.sleep(2)
