from selenium import webdriver
import time

print("Launching Instagram...")
# Chrome driver must be installed
driver = webdriver.Chrome()
driver.get("https://instagram.com")
time.sleep(5)
print("Opened successfully.")
driver.quit()