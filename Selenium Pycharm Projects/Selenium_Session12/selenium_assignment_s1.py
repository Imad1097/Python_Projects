import time

from selenium.webdriver.support import expected_conditions as EC
import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait

# Initialize the Chrome browser
driver = webdriver.Chrome()  # No need to specify the executable_path since it's in PATH
#browser = webdriver.Firefox()

driver.maximize_window()

# Navigate to a website
driver.get('https://www.nestlehomeofgood.com.my/user/login')

password_locator = driver.find_element(By.XPATH, "//input[@id='edit-pass']")
email_locator = driver.find_element(locate_with(By.XPATH, "//input[@id='edit-name']").above(password_locator))

# Input data into both fields
email_locator.send_keys('m.imad')  # Replace with the desired email
password_locator.send_keys('aYeBTiMt89yc@sGE')    # Replace with the desired password
driver.implicitly_wait(30)
