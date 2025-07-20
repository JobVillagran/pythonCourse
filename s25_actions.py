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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0, 300);")

action = ActionChains(driver)
# action.context_click(driver.find_element(By.ID, "mousehover")).perform()
# action.double_click(driver.find_element(By.ID, "mousehover")).perform()
# action.drag_and_drop()
# action.click_and_hold(driver.find_element(By.ID, "mousehover")).perform()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
WebDriverWait(driver, 5)
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
WebDriverWait(driver, 5)


time.sleep(3)
