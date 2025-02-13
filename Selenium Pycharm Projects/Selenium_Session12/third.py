import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Initialize the Chrome browser
driver = webdriver.Chrome()  # No need to specify the executable_path since it's in PATH
#browser = webdriver.Firefox()

driver.maximize_window()
driver.get("https://www.selenium.dev/")

driver.find_element(By.XPATH, "//a[@href='/downloads']").click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
driver.quit()