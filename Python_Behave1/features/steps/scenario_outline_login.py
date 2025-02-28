# import time
#
# from behave import *
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# @given('I launch chrome browser')
# def step_impl(context):
#     context.driver= webdriver.Chrome()
#
#
# @when('i open orange HRM homepage')
# def step_impl(context):
#     context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     time.sleep(3)
#
#
# @when('enter username "{user}" & password "{pwd}"')
# def step_impl(context, user, pwd ):
#     context.driver.find_element(By.NAME,"username").send_keys(user)
#     context.driver.find_element(By.NAME, "password").send_keys(pwd)
#
#
# @when('Click on login button')
# def step_impl(context):
#     context.driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()
#     time.sleep(5)
#
# @then(u'User must successfully login to the dashboard page')
# def step_impl(context):
#     try:
#         text = context.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").text
#     except:
#         context.driver.close()
#         assert False,"Test Failed"
#     if text == "Dashboard":
#         context.driver.close()
#         assert True,"Test Passed"