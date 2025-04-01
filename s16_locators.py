import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Larry King")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
time.sleep(3)

# Static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message


driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

print(driver.title)
time.sleep(5)
