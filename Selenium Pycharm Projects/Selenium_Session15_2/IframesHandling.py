import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.practice-automation.com/iframes/")

iframe = driver.find_element(By.ID,"iframe-1")
driver.switch_to.frame(iframe)
time.sleep(2)
driver.find_element(By.XPATH,"//a[@class='navbar__item navbar__link']").click()
time.sleep(2)

driver.switch_to.default_content()
driver.find_element(By.CSS_SELECTOR,"a[href='https://www.youtube.com/watch?v=4spQdcXWtzQ']").click()
time.sleep(2)