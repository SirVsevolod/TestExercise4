from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver


TIMEOUT = 4


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def wait_elements(self, locator):
        elements = WebDriverWait(self.browser, timeout=TIMEOUT).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def wait_visible(self, locator):
        try:
            element = WebDriverWait(self.browser, timeout=TIMEOUT).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"element {locator} not found")
        return element

    def get_url(self):
        driver = webdriver.Chrome()
        return driver.current_url