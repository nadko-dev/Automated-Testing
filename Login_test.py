import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
waiting = WebDriverWait(driver, 5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

driver.find_element(By.ID, "username").send_keys("TestUser")
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("password123@")
driver.find_element(By.ID, "signInBtn").click()
time.sleep(3)
alertText = driver.find_element(By.CLASS_NAME, "alert-danger").text
print(alertText)
assert "Incorrect" in alertText

driver.close()
