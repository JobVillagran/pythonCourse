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
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(3)

driver.switch_to.frame("mce_0_ifr")  # Switch to the iframe
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")

driver.switch_to.default_content()  # Switch back to the main content
print(driver.find_element(By.CSS_SELECTOR, "h3").text)


time.sleep(3)
