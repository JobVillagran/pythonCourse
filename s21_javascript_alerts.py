import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "name").send_keys("Job")
time.sleep(2)
driver.find_element(By.ID, "alertbtn").click()
# On Line 23 we are verifying that the name we entered is in the alert text.
# This checks if the alert text contains the correct name.
name = "Job"

# Here we are switching to the alert that pops up
# and then we can interact with it
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
time.sleep(2)
alert.accept()


# To dismiss the alert instead of accepting it you can use:
# alert.dismiss()

time.sleep(3)
