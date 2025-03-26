import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Crea el servicio usando el driver automático
service = Service(ChromeDriverManager().install())

# Crea una instancia del navegador
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Abre Google
driver.get("https://www.google.com")

# Imprime el título de la página
print(driver.title)
time.sleep(5)

# # Cierra el navegador
# driver.quit()
