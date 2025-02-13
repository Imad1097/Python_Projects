import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://seleniumbase.io/demo_page")
time.sleep(2)

slider = browser.find_element(By.CSS_SELECTOR,"#mySlider")

actions = ActionChains(browser)
actions.drag_and_drop_by_offset(slider,60,  0).perform()
time.sleep(5)


