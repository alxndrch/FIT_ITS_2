from behave import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

IS_ADMIN = False

@given(u'User is logged in as admin')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    global IS_ADMIN
    if not IS_ADMIN:
        context.driver.find_element(By.CSS_SELECTOR, "#personaltools-login").click()
        context.driver.find_element(By.ID, "__ac_name").send_keys("admin")
        context.driver.find_element(By.ID, "__ac_password").send_keys("admin")
        context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()
        IS_ADMIN = True
        time.sleep(5)

@given(u'user clicks "Add new Evaluation Scenario"')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories").click()
    context.driver.find_element(By.CSS_SELECTOR, "li.plonetoolbar-contenttype:nth-child(3)").click()

@when(u'"Add Evaluation Scenario" page is shown')
def step_impl(context):
    assert (context.driver.find_element(By.CSS_SELECTOR, ".documentFirstHeading")).text == "Add Evaluation Scenario"

@when(u'user fill ES fields')
def step_impl(context):
    for row in context.table:
        if row["name"] == "Title":
            context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys(row["data"])
        elif row["name"] == "Id":
            context.driver.find_element(By.ID, "form-widgets-evaluation_secnario_id").send_keys(row["data"])
        elif row["name"] == "Evaluation Scenario Textual Description":
            context.driver.find_element(By.ID, "form-widgets-evaluation_scenario_textual_description").send_keys(row["data"])

    context.driver.find_element(By.CSS_SELECTOR, "#form-buttons-save").click()

@then(u'evaluation scenario has been created')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".portalMessage")

@then(u'is private')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".label-state-private")

@given(u'user clicks on "Add new Use Case"')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories").click()
    context.driver.find_element(By.CSS_SELECTOR, "li.plonetoolbar-contenttype:nth-child(17)").click()

@when(u'"Add Use Case" page is shown')
def step_impl(context):
    assert (context.driver.find_element(By.CSS_SELECTOR, ".documentFirstHeading")).text == "Add Use Case"

@when(u'user fill UC fields')
def step_impl(context):
    for row in context.table:
        if row["name"] == "Title":
            context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys(row["data"])
        elif row["name"] == "Use Case Provider":
            context.driver.find_element(By.CSS_SELECTOR, "#s2id_autogen5 > ul:nth-child(1)").click()
            time.sleep(1)
            context.driver.find_element(By.CSS_SELECTOR, ".pattern-relateditems-result-browse").click()
            time.sleep(1)
            context.driver.find_element(By.ID, "s2id_autogen6").send_keys(row["data"])
            time.sleep(1)
            context.driver.find_element(By.CSS_SELECTOR, ".pattern-relateditems-result-select").click()

        elif row["name"] == "Use Case Description":
            # vytvoreni pomoci Selenium IDE
            context.driver.switch_to.frame(0)
            context.driver.find_element(By.CSS_SELECTOR, "html").click()
            element = context.driver.find_element(By.ID, "tinymce")
            context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>test</p>'}", element)
            context.driver.switch_to.default_content()

    context.driver.find_element(By.CSS_SELECTOR, "#form-buttons-save").click()

@then(u'use case has been created')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".portalMessage")

@given(u'a web browser at "UC2_test" page')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".use-cases > a:nth-child(1)").click()
    context.driver.find_element(By.LINK_TEXT, "UC2_test").click()

@when(u'state of use case is set to published by admin')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-workflow").click()
    context.driver.find_element(By.CSS_SELECTOR, "li.plonetoolbar-workfow-transition:nth-child(2)").click()

@then(u'use case "UC2_test" is visible for not logged in user')
def step_impl(context):
    global IS_ADMIN
    try:
        # odhlaseni
        context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
        context.driver.find_element(By.CSS_SELECTOR, "#personaltools-logout").click()
        IS_ADMIN = False
    except NoSuchElementException:
        IS_ADMIN = True

    context.driver.find_element(By.CSS_SELECTOR, ".use-cases > a:nth-child(1)").click()
    context.driver.find_element(By.LINK_TEXT, "UC2_test")

@given(u'a web browser at page "Edit Use Case" of use case "UC2_test"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".use-cases > a:nth-child(1)").click()
    context.driver.find_element(By.LINK_TEXT, "UC2_test").click()
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit").click()

@when(u'user select "Use case Evaluation Scenarios" bar')
def step_impl(context):
    context.driver.find_element(By.ID, "autotoc-item-autotoc-1").click()

@when(u'select evaluation scenario "ES1_test"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#s2id_autogen1 > ul:nth-child(1)").click()
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-relateditems-result-browse").click()
    time.sleep(1)
    context.driver.find_element(By.ID, "s2id_autogen2").send_keys("ES1_test")
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-relateditems-result-select").click()

    context.driver.find_element(By.CSS_SELECTOR, "#form-buttons-save").click()

@then(u'scenario "ES1_test" is visible in "Evaluation Scenarios List" of "UC2_test"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".use-cases > a:nth-child(1)").click()
    context.driver.find_element(By.LINK_TEXT, "UC2_test").click()

    assert (context.driver.find_element(By.CSS_SELECTOR, "span.contenttype-evaluation_scenario")).text == "ES1_test"

@then(u'is marked as private')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#form-widgets-evaluation_scenario > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > span:nth-child(1) > a:nth-child(1)").click()
    context.driver.find_element(By.CSS_SELECTOR, ".label-state-private")

@when(u'user do not fill required fields:')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#form-buttons-save").click()

@then(u'warning is displayed')
def step_impl(context):
    assert (context.driver.find_element(By.CSS_SELECTOR, ".portalMessage > dt:nth-child(1)")).text == "Error"

@given(u'a web browser at Organisations page')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".organisations > a:nth-child(1)").click()

@given(u'user clicks "Add new Organisation"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories").click()
    context.driver.find_element(By.CSS_SELECTOR, "li.plonetoolbar-contenttype:nth-child(11)").click()

@when(u'"Add Organization" page is shown')
def step_impl(context):
    assert (context.driver.find_element(By.CSS_SELECTOR, ".documentFirstHeading")).text == "Add Organization"

@when(u'user fill organisation fields')
def step_impl(context):
    for row in context.table:
        if row["name"] == "Title":
            context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys(row["data"])
        elif row["name"] == "Acronym":
            context.driver.find_element(By.ID, "form-widgets-organization_acronym").send_keys(row["data"])

    context.driver.find_element(By.CSS_SELECTOR, "#form-buttons-save").click()

@then(u'organisation has been created')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".portalMessage")

@given(u'a web browser at page "Edit Use Case" of use case "UC1 Trespassing Monitoring & Enforcing System"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".use-cases > a:nth-child(1)").click()
    context.driver.find_element(By.LINK_TEXT, "UC1 Trespassing Monitoring & Enforcing System").click()
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit").click()

@when(u'user try to add another Use Case Provider')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#s2id_autogen5 > ul:nth-child(1) > li:nth-child(2)").click()

@then(u'text "You can only select 1 item" is shown')
def step_impl(context):
    assert (context.driver.find_element(By.CSS_SELECTOR, ".select2-selection-limit")).text == "You can only select 1 item"








# @given(u'published Use cases are shown')
# def step_impl(context):
#     use_cases = context.driver.find_elements(By.CSS_SELECTOR, "article.entry")
#     assert len(use_cases) == 1
#     text = (context.driver.find_element(By.CSS_SELECTOR, f"article.entry:nth-child(1) > header:nth-child(1) > span:nth-child(1) > a:nth-child(1)")).text
#     assert text == "UC1 Trespassing Monitoring & Enforcing System"