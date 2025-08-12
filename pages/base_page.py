from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import allure


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    @allure.step('Найти элемент по локатору: {locator}')
    def find_element_webdriverwait(self, locator):
        """
        Ожидает появления элемента на странице.
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Кликнуть по элементу: {locator}')
    def click_element(self, locator):
        """
        Ожидает и кликает по элементу.
        """
        element = self.find_element_webdriverwait(locator)
        element.click()

    @allure.step('Получить текст из элемента: {locator}')
    def get_text_from_element(self, locator):
        """
        Получает текст из элемента.
        """
        element = self.find_element_webdriverwait(locator)
        return element.text

    @allure.step('Проскроллить к элементу: {locator}')
    def scroll_to_element(self, locator):
        """
        Скроллит к элементу.
        """
        element = self.find_element_webdriverwait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Перетащить элемент на целевой локатор')
    def drag_and_drop(self, source_element, target_locator):
        """
        Перетаскивает элемент на целевой локатор.
        """
        target_element = self.find_element_webdriverwait(target_locator)
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    @allure.step('Перетащить элемент (реализация для Firefox)')
    def drag_and_drop_firefox(self, source_element, target_locator):
        """
        Перетаскивание для Firefox (альтернативная реализация).
        """
        target_element = self.find_element_webdriverwait(target_locator)
        ActionChains(self.driver).click_and_hold(source_element).move_to_element(target_element).release().perform()

    @allure.step('Ожидать изменения текста элемента')
    def wait_for_text_to_change(self, locator, initial_text):
        """
        Ожидает, пока текст элемента изменится с initial_text.
        """
        def text_has_changed(driver):
            element = driver.find_element(*locator)
            return element.text and element.text != initial_text

        WebDriverWait(self.driver, self.timeout).until(text_has_changed)

