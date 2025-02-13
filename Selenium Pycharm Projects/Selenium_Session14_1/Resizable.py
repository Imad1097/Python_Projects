import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://strml.github.io/react-resizable/examples/1.html")
time.sleep(2)

resizable_element = browser.find_element(By.XPATH, "//body/div[@id='content']/div/div[1]/span[2]")
time.sleep(5)

actions = ActionChains(browser)
actions.click_and_hold(resizable_element).move_by_offset(300, 100).release().perform()
time.sleep(5)