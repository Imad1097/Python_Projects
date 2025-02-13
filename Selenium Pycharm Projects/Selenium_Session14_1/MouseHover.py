import time
import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.apple.com/au/iphone")
time.sleep(2)

#hover_element = browser.find_element(By.CSS_SELECTOR,"a[aria-label='Store'] span[class='globalnav-link-text-container']")
hover_element1 = browser.find_element(By.CLASS_NAME,"globalnav-link-text-container")

actions = ActionChains(browser)

actions.move_to_element(hover_element1).perform()
time.sleep(5)

