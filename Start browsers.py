from selenium import webdriver
import time

# Microsoft Edge browser
driver1 = webdriver.Edge()
driver1.get("https://nadirdev.com")
driver1.maximize_window()
print(driver1.title)
print(driver1.current_url)
time.sleep(2)
driver1.close()

# Firefox Mozilla browser
driver2 = webdriver.Firefox()
driver2.get("https://nadirdev.com")
driver2.maximize_window()
print(driver2.title)
print(driver2.current_url)
time.sleep(2)
driver2.close()

# Google Chrome browser
driver3 = webdriver.Chrome()
driver3.get("https://nadirdev.com")
driver3.maximize_window()
print(driver3.title)
print(driver3.current_url)
time.sleep(2)
driver3.close()
