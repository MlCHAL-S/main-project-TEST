from selenium import webdriver
from selenium.webdriver.firefox.service import Service


WAIT_SECONDS = 10

def before_all(context):
    """ Executed once before all tests. """
    context.base_url = 'http://localhost:5000'
    context.wait_seconds = WAIT_SECONDS

    options = webdriver.FirefoxOptions()

    service = Service(executable_path='/snap/bin/geckodriver')
    context.driver = webdriver.Firefox(service=service, options=options)
    options.add_argument("--headless=new")

    context.driver.implicitly_wait(context.wait_seconds)


def after_all(context):
    """ Executed after all tests. """
    context.driver.quit()
