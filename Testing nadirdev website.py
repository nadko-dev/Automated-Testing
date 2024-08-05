from selenium import webdriver
from selenium.webdriver.common.by import By

# Assigning Chrome driver
driverChrome = webdriver.Chrome()
driverChrome.implicitly_wait(5)
driverChrome.get("https://nadirdev.com")

# Disable smooth scroll
disable_smooth_scroll_js = """
document.documentElement.style.scrollBehavior = 'auto';
window.onload = function() {
  const styles = `
    html {
      scroll-behavior: auto !important;
    }
  `;
  const styleSheet = document.createElement("style");
  styleSheet.type = "text/css";
  styleSheet.innerText = styles;
  document.head.appendChild(styleSheet);
}
"""

driverChrome.execute_script(disable_smooth_scroll_js)
driverChrome.maximize_window()
print(driverChrome.title)

# Checking logo
driverChrome.find_element(By.CLASS_NAME, "NZlogo").click()

# Adding menu items to a list
menu_item = driverChrome.find_elements(By.CSS_SELECTOR, ".nav-link")

# Adding buttons to the list
buttons = driverChrome.find_elements(By.XPATH, "//center/a/button")

# First menu item "Resume"
menu_item[0].click()

# Assigning original tab to return later
window_original = driverChrome.window_handles[0]

# Resume button
buttons[0].click()

# Assigning new tab
window_resume = driverChrome.window_handles[1]

# Switch to original page
driverChrome.switch_to.window(window_original)

# Contact button
buttons[1].click()
driverChrome.execute_script("window.scrollTo(0, document.body.scrollTop);")

# Second menu item "Portfolio"
menu_item[1].click()

# Testing Portfolio section arrows
driverChrome.find_element(By.XPATH, "//span[@class='carousel-control-next-icon']").click()
driverChrome.find_element(By.XPATH, "//span[@class='carousel-control-next-icon']").click()
driverChrome.find_element(By.XPATH, "//span[@class='carousel-control-next-icon']").click()

# Testing button
element = driverChrome.find_element(By.XPATH, "//div/a/h5")
driverChrome.execute_script("arguments[0].scrollIntoView();", element)
element.click()
window_portfolio = driverChrome.window_handles[2]
driverChrome.switch_to.window(window_original)

# Third menu item "Contact"
driverChrome.execute_script("window.scrollTo(0, document.body.scrollTop);")
menu_item[2].click()

# Testing form
driverChrome.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Test User")
driverChrome.find_element(By.XPATH, "//input[@id='Email']").send_keys("test@test.com")
driverChrome.find_element(By.XPATH, "//textarea[@id='Message']").send_keys("Test")
# driverChrome.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Scrolling down to the footer
driverChrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Testing LinkedIn button
driverChrome.find_element(By.XPATH, "//footer/a[1]").click()
window_linkedin = driverChrome.window_handles[3]
driverChrome.switch_to.window(window_original)

# Testing GitHub button
driverChrome.find_element(By.XPATH, "//footer/a[2]").click()
window_git = driverChrome.window_handles[4]
driverChrome.switch_to.window(window_original)

# Close browser
driverChrome.close()
print("Test has been successfully complete")
