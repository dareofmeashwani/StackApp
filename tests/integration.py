import time
import unittest
from selenium import webdriver
import subprocess
import os
import signal
import selenium_util
import sys

sys.path.append('../')

flask_app_pid = None
URL = "http://localhost"


class StackIntegrationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global flask_app_pid
        flask_app_pid = subprocess.Popen("python ./../main.py").pid
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        os.kill(flask_app_pid, signal.SIGTERM)

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def tearDown(self):
        self.driver.close()

    def test_1_search_in_python_org(self):
        self.assertEqual({}, {})
        driver = self.driver
        driver.get(URL)
        selenium_util.update_stack_capacity(driver, 3)
        selenium_util.click_stack_capacity(driver)
        selenium_util.stack_ops_availability(driver, True)

    def test_2_push_print(self):
        self.assertEqual({}, {})
        driver = self.driver
        driver.get(URL)
        selenium_util.stack_push(driver, 3)
        selenium_util.click_stack_display(driver)
        selenium_util.verify_stack_values(driver, ['3'])

    def test_3_push_print(self):
        self.assertEqual({}, {})
        driver = self.driver
        driver.get(URL)
        selenium_util.stack_push(driver, 2)
        selenium_util.stack_push(driver, 1)
        selenium_util.click_stack_display(driver)
        selenium_util.verify_stack_values(driver, [3, 2, 1])

    def test_4_push_overflow(self):
        self.assertEqual({}, {})
        driver = self.driver
        driver.get(URL)
        selenium_util.stack_push(driver, 4)
        selenium_util.check_alert_and_accept(driver)
        selenium_util.click_stack_display(driver)
        selenium_util.verify_stack_values(driver, [3, 2, 1])

    def test_5_push_pop_print(self):
        self.assertEqual({}, {})
        driver = self.driver
        driver.get(URL)
        selenium_util.click_stack_pop(driver)
        selenium_util.click_stack_display(driver)
        selenium_util.verify_stack_values(driver, [3, 2])

    def test_6_stack_pop_till_empty(self):
        self.assertEqual({}, {})
        driver = self.driver
        driver.get(URL)
        selenium_util.click_stack_pop(driver)
        selenium_util.click_stack_pop(driver)
        selenium_util.click_stack_display(driver)
        selenium_util.verify_stack_values(driver, [])

    def test_7_stack_pop_underflow(self):
        self.assertEqual({}, {})
        driver = self.driver
        driver.get(URL)
        selenium_util.click_stack_pop(driver)
        selenium_util.click_stack_display(driver)
        selenium_util.verify_stack_values(driver, [])

    def test_8_stack_reset(self):
        self.assertEqual({}, {})
        driver = self.driver
        driver.get(URL)
        selenium_util.click_stack_reset(driver)
        selenium_util.stack_ops_availability(driver, False)
        selenium_util.check_stack_capacity(driver, "")

if __name__ == "__main__":
    unittest.main()