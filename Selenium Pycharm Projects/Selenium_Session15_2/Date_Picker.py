import time
import driver
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice-automation.com/calendars/")
wait = WebDriverWait(driver,10)
date_picker = wait.until(EC.element_to_be_clickable((By.ID,"g1065-2-selectorenteradate")))
date_picker.click()



time.sleep(2)