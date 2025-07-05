import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

# Implicitly wait for elements to be present
# It's not usefule because all the lines of code will wait for the same amount
# of time
#  Use it with flaky tests or when you are not sure about the element's
#  presence
driver.implicitly_wait(5)


driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
time.sleep(2)  # Wait for the results to load on the list of products
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

time.sleep(3)
