import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


screen_size = [(1920,1080), (1366,768), (1440,900)]
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/")

for x,y in screen_size:
    print(x,y)
    driver.set_window_size(x,y)
    if x == 1920 and y == 1080:
#        #assertion
    elif x == 1366 and y == 768:
#        #assertion
    else:
#        #assertion
    time.sleep(3)
