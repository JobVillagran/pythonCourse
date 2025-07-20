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
driver.get("https://the-internet.herokuapp.com/windows")

time.sleep(3)
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
newWindowText = driver.find_element(By.TAG_NAME, "h3")
assert "New Window" in newWindowText.text
print(newWindowText.text)
time.sleep(3)
driver.close()

driver.switch_to.window(windowsOpened[0])
print("Switching back to the original window")
print(driver.find_element(By.TAG_NAME, "h3").text)
assert "Opening a new window" in driver.find_element(By.TAG_NAME, "h3").text

time.sleep(3)
