import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# driver.find_element(By.ID,"my-text-id").send_keys("python")
# time.sleep(5)

# driver.find_element(By.LINK_TEXT, "Return to index").click()
# time.sleep(5)
email_locator = driver.find_element(locate_with(By.ID, "my-text-id").above({By.NAME: "my-password"}))
email_locator.send_keys("python")
password_locator = driver.find_element(locate_with(By.TAG_NAME, "input").below({By.ID: "my-text-id"}))
password_locator.send_keys("python")
time.sleep(5)




driver.close()