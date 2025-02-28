import time

from selenium.webdriver.support import expected_conditions as EC
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@given(u'Navigate to google.com')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.google.com/")
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'q'))
    )


@when(u'Type "{search_term}"')
def step_impl(context,search_term):
    search_box = context.driver.find_element(By.NAME, 'q')
    search_box.send_keys(search_term)


@when(u'click on search button')
def step_impl(context):
    # Wait until the search button is clickable
    search_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'btnK'))
    )
    search_button.click()




@then(u'title should be selenium with python - Google Search')
def step_impl(context):
    time.sleep(5)
    title = context.driver.title
    assert "Google Search" in title