from behave import *
from selenium.webdriver.common.by import By
import time

# background
@given(u'User is not logged in')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.ID, "personaltools-login")

@given(u'a web browser at Use Cases page')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".use-cases > a:nth-child(1)").click()

@when(u'user clicks at use case page "UC1 Trespassing Monitoring & Enforcing System"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "UC1 Trespassing Monitoring & Enforcing System").click()

@then(u'informations about use case are filled')
def step_impl(context):
    for row in context.table:
        if row["informations"] == "Use Case Number":
            assert row['filled'] == (context.driver.find_element(By.CSS_SELECTOR, "#form-widgets-use_case_number > span:nth-child(1)")).text
        elif row["informations"] == "Use Case Domain":
            assert row['filled'] == (context.driver.find_element(By.CSS_SELECTOR, "#form-widgets-use_case_domain > span:nth-child(1)")).text
        elif row["informations"] == "Use Case Provider":
            assert row['filled'] == (context.driver.find_element(By.XPATH, "/html/body/div/div[3]/main/div[1]/div/div/article/div[2]/div[3]/span/div/ul/li/span/a/span[1]")).text

@given(u'web page with all use cases private')
def step_impl(context):

    # prihlaseni
    context.driver.find_element(By.CSS_SELECTOR, "#personaltools-login").click()
    context.driver.find_element(By.ID, "__ac_name").send_keys("admin")
    context.driver.find_element(By.ID, "__ac_password").send_keys("admin")
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()
    # vyber UC
    time.sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, ".use-cases > a:nth-child(1)").click()
    context.driver.find_element(By.LINK_TEXT, "UC1 Trespassing Monitoring & Enforcing System").click()
    # ukryti obsahu
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-workflow").click()
    context.driver.find_element(By.CSS_SELECTOR, "li.plonetoolbar-workfow-transition:nth-child(2)").click()
    # odhlaseni
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
    context.driver.find_element(By.CSS_SELECTOR, "#personaltools-logout").click()

@when(u'user open a web browser at Use Cases page')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".use-cases > a:nth-child(1)").click()

@then(u'web page does not contain any use case')
def step_impl(context):
    assert (context.driver.find_element(By.XPATH, "./html/body/div[1]/div[3]/main/div[1]/div/div/article/div[2]/p")).text == "There are currently no items in this folder."

    # clean
    # prihlaseni
    context.driver.find_element(By.CSS_SELECTOR, "#personaltools-login").click()
    context.driver.find_element(By.ID, "__ac_name").send_keys("admin")
    context.driver.find_element(By.ID, "__ac_password").send_keys("admin")
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()
    # vyber UC
    time.sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, ".use-cases > a:nth-child(1)").click()
    context.driver.find_element(By.LINK_TEXT, "UC1 Trespassing Monitoring & Enforcing System").click()
    # publikace
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-workflow").click()
    context.driver.find_element(By.CSS_SELECTOR, "li.plonetoolbar-workfow-transition:nth-child(2)").click()
    # odhlaseni
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
    context.driver.find_element(By.CSS_SELECTOR, "#personaltools-logout").click()

@given(u'a web browser at Home page')
def step_impl(context):
    pass

@when(u'user clicks on Methods link')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".methods > a:nth-child(1)").click()

@then(u'only "Combinatorial Testing" method is visible')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Combinatorial Testing")

@when(u'user clicks on Tools link')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".tools > a:nth-child(1)").click()

@then(u'only "Testos / Combine" method is visible')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Testos / Combine")