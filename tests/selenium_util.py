from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

DELAY = 0.5

def update_stack_capacity(driver, val):
    capacity_input = driver.find_element(value="capacityInput")
    capacity_input.send_keys(val)


def click_stack_capacity(driver):
    capacity_button = driver.find_element(value="capacityButton")
    capacity_button.click()
    time.sleep(DELAY)


def check_stack_capacity(driver, val):
    capacity_input = driver.find_element(value="capacityInput")
    if capacity_input.text != val:
        raise Exception("Stack capacity not matched")


def stack_ops_availability(driver, state):
    stack_ops = driver.find_element(value="stackOps")
    is_stack_ops_visible = stack_ops.is_displayed()
    if is_stack_ops_visible != state:
        raise Exception("Stack operation not found")


def stack_push(driver, val):
    push_input = driver.find_element(value="pushInput")
    push_input.send_keys(val)
    push_button = driver.find_element(value="pushButton")
    push_button.click()
    time.sleep(DELAY)


def click_stack_display(driver):
    display_button = driver.find_element(value="displayButton")
    display_button.click()
    time.sleep(DELAY)


def click_stack_pop(driver):
    display_button = driver.find_element(value="popButton")
    display_button.click()
    time.sleep(DELAY)


def verify_stack_values(driver, values):
    stack_values = driver.find_element(value="stackValuesLabel")
    if ", ".join([str(val) for val in values]) != stack_values.text:
        raise Exception("stack content incorrect")


def click_stack_reset(driver):
    reset_button = driver.find_element(value="resetButton")
    reset_button.click()
    time.sleep(DELAY)


def check_alert_and_accept(driver):
    try:
        WebDriverWait(driver, 4).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
    except TimeoutException as error:
        print("no alert")
        raise error
