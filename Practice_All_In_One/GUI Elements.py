import time
from webbrowser import Chrome

from datetime import datetime,timedelta
import wait
from selenium import webdriver
import driver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")


# name = driver.find_element(By.ID,"name")
# name.send_keys("imad")
# email = driver.find_element(By.ID,"email")
# email.send_keys("muhammad.imad@thedigitz.com")
# phone = driver.find_element(By.ID,"phone")
# phone.send_keys("03082502035")
#
# time.sleep(2)
#
# radio_button = driver.find_element(By.XPATH,"//input[@id='male']")
# radio_button.click()
#
# if radio_button.is_selected():
#     print("Radio button 'Male' is selected.")
# else:
#     print("Radio button selection failed.")
#
# time.sleep(2)
#
# check_boxes1 = driver.find_element(By.XPATH,"//input[@id='sunday']")
# check_boxes1.click()
# check_boxes2 = driver.find_element(By.XPATH,"//input[@id='saturday']")
# check_boxes2.click()
#
# if check_boxes1.is_selected() and check_boxes2.is_selected():
#     print("Checkboxes for 'Sunday' and 'Saturday' are selected.")
# else:
#     print("Checkbox selection failed.")
#
# time.sleep(2)
#
# driver.execute_script("window.scrollBy(0, 500);")  # Scroll down by 500 pixels
#
# country_drop_drown = driver.find_element(By.ID,"country")
# time.sleep(2)
# select = Select(country_drop_drown)
# select.select_by_visible_text("Canada")
# time.sleep(2)
# selected_option = select.first_selected_option.text
#
# if selected_option == "Canada":
#     print("Dropdown 'Canada' is selected successfully")
# else:
#     print("Dropdown 'Canada' is not selected")
#
#
# options = driver.find_elements(By.TAG_NAME,"option")
# Option_length = len(options)
# print(Option_length)
#
# list = driver.find_element(By.ID,"colors")
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", list)
# time.sleep(2)
# select = Select(list)
# select.select_by_visible_text("White")
# time.sleep(2)
# selected_list = select.first_selected_option.text
# print(selected_list)
#
#
# wait = WebDriverWait(driver, 10)
# Sorted_list = wait.until(EC.presence_of_element_located((By.ID, "animals")))
# option = driver.find_element(By.XPATH, "//option[@value='elephant']")
# driver.execute_script("arguments[0].scrollIntoView();", option)
# time.sleep(2)
# select = Select(Sorted_list)
# select.select_by_visible_text("Elephant")
# time.sleep(2)
# selected_list = select.first_selected_option.text
# print(selected_list)
# time.sleep(2)


# driver.execute_script("window.scrollBy(0, 800);")  # Scroll down by 500 pixels
# time.sleep(2)  # Wait to see the effect
#
#
# Date_Field = wait.until(EC.element_to_be_clickable((By.ID,"datepicker")))
# Date_Field.click()
# time.sleep(2)
#
# Select_Date = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='25']")))
# Select_Date.click()
# Date_Field = wait.until(EC.element_to_be_clickable((By.ID,"datepicker")))
# Date_Field.click()
# time.sleep(2)
# current_date = datetime.now()
# print(current_date)
# date_format = current_date.strftime("%m/%d/%y")
# print(date_format)
#
# Date_Field = wait.until(EC.element_to_be_clickable((By.ID,"datepicker")))
# Date_Field.click()
# time.sleep(2)

driver.execute_script("window.scrollBy(0, 800);")
Date_Field = wait.until(EC.element_to_be_clickable((By.ID,"datepicker")))
Date_Field.click()
time.sleep(2)

wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='ui-datepicker-div']")))
#next_month_year = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']")))
#previous_month_year = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']")))


# next_month_year = driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']")
# next_month_year.click()
# time.sleep(2)
# previous_month_year = driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']")
# previous_month_year.click()
# time.sleep(2)



# Date_Field = wait.until(EC.element_to_be_clickable((By.ID,"datepicker")))
# Date_Field.click()
# time.sleep(2)

for a in range(10):
    next_month_year = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']")))
    next_month_year.click()
    time.sleep(1)  # Short wait after clicking
    print(f"Clicked Next Month {a + 1} time(s)")

# Click Previous Month 10 times
for b in range(10):
    previous_month_year = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']")))
    previous_month_year.click()
    time.sleep(1)  # Short wait after clicking
    print(f"Clicked Previous Month {b + 1} time(s)")

print("All test cases executed successfully.")