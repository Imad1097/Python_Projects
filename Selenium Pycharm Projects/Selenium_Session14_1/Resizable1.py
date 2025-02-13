import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
browser = webdriver.Chrome()
browser.maximize_window()

# Open the webpage
browser.get("https://strml.github.io/react-resizable/examples/1.html")
time.sleep(2)

# Wait for the resizable element to be present
wait = WebDriverWait(browser, 10)
resizable_element = wait.until(
    EC.presence_of_element_located((By.XPATH, "//body/div[@id='content']/div/div[1]/span[2]"))
)

# Scroll the element into view if necessary
browser.execute_script("arguments[0].scrollIntoView(true);", resizable_element)

# Use ActionChains to resize the element
actions = ActionChains(browser)

try:
    # Click and hold the element, move it by a smaller offset
    actions.click_and_hold(resizable_element).move_by_offset(100, 100).release().perform()
    print("Element resized successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

# Optional: Pause to observe the result
time.sleep(5)

# Close the browser
browser.quit()
