import time

import driver
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/broken_images")

images = driver.find_elements(By.TAG_NAME,"img")
broken_images = []

for image in images:
    All_images = image.get_attribute("src")
    if All_images:
        response = requests.get(All_images)
        if response.status_code!=200:
            broken_images.append(All_images)
            print("broken image found")

if broken_images:
    print("list of broken images")
    for brk_img in broken_images:
        print(brk_img)

else:
    print("No broken image found")

driver.close()