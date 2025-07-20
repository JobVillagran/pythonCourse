import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(3)

driver.find_element(By.XPATH, "/html/body/a").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
newWindowText = driver.find_element(By.XPATH, "//*/strong/a").text
assert "mentor@rahulshettyacademy.com" in newWindowText
print(newWindowText)

driver.switch_to.window(windowsOpened[0])
time.sleep(2)
driver.find_element(By.ID, "username").send_keys(newWindowText)
driver.find_element(By.ID, "password").send_keys("Test123!")
driver.find_element(By.ID, "signInBtn").click()
try:
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-danger"))
    )
    error_text = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    print(error_text)
except:
    print("Error message did not appear in time.")
assert "Incorrect username/password." in error_text, "Unexpected error message"

time.sleep(3)
