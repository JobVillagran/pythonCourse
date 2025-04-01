import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client/")
time.sleep(3)

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
driver.find_element(By.CSS_SELECTOR, "#userPassword").send_keys("Hello1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello1234")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(3)
