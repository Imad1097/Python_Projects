from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@given('Launch the chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when('Open HRM homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('Verify that the logo present on page')
def verify_logo(context):
    logo = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,"//img[@alt='company-branding']"))
    )
    assert logo.is_displayed() is True

@then('Close browser')
def close_browser(context):
    context.driver.close()

