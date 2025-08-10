from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def click_element(self, locator):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator)).click()

    def find_element_webdriverwait(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def get_text_from_element(self, locator):
        return self.find_element_webdriverwait(locator).text

    def input_text(self, locator, text):
        element = self.find_element_webdriverwait(locator)
        element.clear()
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url
