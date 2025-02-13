import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Initialize the Chrome browser
driver = webdriver.Chrome()  # No need to specify the executable_path since it's in PATH
#browser = webdriver.Firefox()

driver.maximize_window()

# Navigate to a website
#driver.get('https://www.selenium.dev/selenium/web/web-form.html')
driver.get('https://www.selenium.dev/documentation/webdriver/elements/locators/')

#driver.find_element(By.CLASS_NAME,"form-control").send_keys("python")
driver.find_element(By.PARTIAL_LINK_TEXT,"test practices").click()
time.sleep(3)