import time
import select
from selenium.webdriver.support.select import Select
from datetime import datetime,timedelta
import driver
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
url = ("https://demo.automationtesting.in/Datepicker.html")
driver.get(url)

driver.find_element(By.ID,"datepicker2").click()
time.sleep(5)

current_date = datetime.now()
print(current_date)

next_day = current_date + timedelta(days=1)
print(next_day)

next_day_date_only = (str(next_day.day))
print(next_day_date_only)

current_month = datetime.now().month
print(current_month)

current_year = current_date.year
print(current_year)

next_monthh = (current_month % 12) + 1
print(next_monthh)

next_month_year = f"{next_monthh}/{current_year}"
print(next_month_year)

month_drop_down = driver.find_element(By.CSS_SELECTOR,"select[title='Change the month']")
select = Select(month_drop_down)
select.select_by_value(str(next_month_year))
time.sleep(3)
year_drop_down = driver.find_element(By.CSS_SELECTOR,"select[title='Change the year']")
select = Select(year_drop_down)
select.select_by_visible_text("2025")

driver.find_element(By.LINK_TEXT,next_day_date_only).click()
time.sleep(5)








