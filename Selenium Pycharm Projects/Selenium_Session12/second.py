import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Initialize the Chrome browser
driver = webdriver.Chrome()  # No need to specify the executable_path since it's in PATH
#browser = webdriver.Firefox()

driver.maximize_window()
driver.get("https://www.selenium.dev/")
title = driver.title
print(title)

assert "Selenium" in title
driver.quit()
