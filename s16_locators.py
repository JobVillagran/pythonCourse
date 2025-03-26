import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(3)

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234")
driver.find_element(By.ID, "exampleCheck1").click()

print(driver.title)
time.sleep(5)
