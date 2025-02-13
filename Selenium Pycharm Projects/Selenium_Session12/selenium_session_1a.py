import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Initialize the Chrome browser
driver = webdriver.Chrome()  # No need to specify the executable_path since it's in PATH
#browser = webdriver.Firefox()

driver.maximize_window()

# Navigate to a website
driver.get('https://www.nestlehomeofgood.com.my/user/login')

title = driver.title
print(title)
assert "Log in | Nestlé Home of Good" in title

driver.find_element(By.XPATH,"//a[@role='button'][normalize-space()='Good Deals']").click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)

