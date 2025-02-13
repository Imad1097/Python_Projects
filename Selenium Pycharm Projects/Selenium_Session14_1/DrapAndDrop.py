import time
import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://drag-and-drop-tricks.webflow.io/")
time.sleep(5)

source = driver.find_element(By.CSS_SELECTOR,"div[class='draggable correct ui-draggable ui-draggable-handle'] div[class='draggable_fill']")
target =driver.find_element(By.CSS_SELECTOR, ".quiz-option.is-drop")

action = ActionChains(driver)

action.drag_and_drop(source,target).perform()
time.sleep(5)