from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the careers page
driver.get("https://www.shahsons.com/careers")  # Change to actual URL

def fill_form(driver, first_name, last_name, email, address, phone, category, resume_path):
    """Function to fill and submit the form"""
    driver.find_element(By.NAME, "fname").send_keys(first_name)
    driver.find_element(By.NAME, "lname").send_keys(last_name)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "address").send_keys(address)
    driver.find_element(By.NAME, "contact").send_keys(phone)

    # Wait for dropdown to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "category"))
    )

    # Select a category from dropdown
    category_dropdown = Select(driver.find_element(By.NAME, "category"))

    # Get available options
    options = [opt.text.strip() for opt in category_dropdown.options]
    print("Dropdown options:", options)

    if category in options:
        category_dropdown.select_by_visible_text(category)
    else:
        print(f"⚠️ Category '{category}' not found! Available options: {options}")
        return  # Exit function if category is invalid

    # Upload a file
    driver.find_element(By.NAME, "CV").send_keys(resume_path)

    # Wait for submit button to be clickable and scroll to it
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    time.sleep(3)  # Wait for submission

# Example data (Updated category)
test_data = [
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
    ("Test1", "User1", "test1@example.com", "123 Street", "1234567890", "IT", "C:/dummy.pdf"),
]

# Loop through test data
for data in test_data:
    fill_form(driver, *data)
    time.sleep(5)  # Pause before next submission

# Close the browser
driver.quit()
