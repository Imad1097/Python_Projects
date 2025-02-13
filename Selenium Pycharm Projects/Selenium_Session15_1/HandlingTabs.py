import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.selenium.dev/")
driver.switch_to.new_window()
driver.get("https://playwright.dev/")

total_tabs = driver.window_handles
print(total_tabs)

current_tab = driver.current_window_handle
print(current_tab)

driver.find_element(By.CLASS_NAME,"getStarted_Sjon").click()
time.sleep(3)

first_tab = driver.window_handles[0]
#driver.switch_to.window(first_tab)
if current_tab != first_tab:
    driver.switch_to.window(first_tab)

driver.find_element(By.XPATH,"//span[normalize-space()='Downloads']").click()
