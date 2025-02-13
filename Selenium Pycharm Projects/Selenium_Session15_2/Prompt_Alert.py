import time

import driver
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"button[onclick='jsPrompt()']").click()
alert = Alert(driver)
print(alert.text)
text = "This is selenium python training"
alert.send_keys(text)
alert.accept()
time.sleep(3)