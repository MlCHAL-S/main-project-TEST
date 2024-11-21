from behave import given, when, then
from selenium.webdriver.common.by import By


@given(u'the app is running')
def step_impl(context):
    context.driver.get(context.base_url)




@given(u'I navigate to the Home Page')
def step_impl(context):
    context.driver.get(context.base_url)
    body = context.driver.find_element(By.TAG_NAME, "body")
    assert "Items" in body.text


@given(u'I enter "{text}" in the input')
def step_impl(context, text):
    input_box = context.driver.find_element(By.ID, "text")
    input_box.clear()
    input_box.send_keys(text)


@when(u'I press the "Submit" button')
def step_impl(context):
    submit_button = context.driver.find_element(By.ID, "index-submit-btn")
    submit_button.click()


@then(u'I should see "{text}" on the web page')
def step_impl(context, text):
    body = context.driver.find_element(By.TAG_NAME, "body")
    assert text in body.text

@then('close the browser')
def step_impl(context):
    context.driver.quit()