from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver, time=10):
        self.driver = driver
        self.time = time

    # Найти элемент
    def find_element_webdriverwait(self, locator):
        return WebDriverWait(self.driver, self.time).until(EC.visibility_of_element_located(locator))

    # Кликнуть элемент
    def click_element(self, locator):
        element = WebDriverWait(self.driver, self.time).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    # Ввести текст в элементе
    def add_text_to_element(self, locator, text):
        element = self.find_element_webdriverwait(locator)
        element.send_keys(text)

    # Получить текст элемента
    def get_text_from_element(self, locator):
        element = self.find_element_webdriverwait(locator)
        return element.text

    # Скроллить до элемента
    def scroll_to_element(self, locator):
        element = self.find_element_webdriverwait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    # Дождаться смены URL
    def url_changes(self, original_url):
        WebDriverWait(self.driver, self.time).until(EC.url_changes(original_url))

    # Получить новый URL
    def wait_for_url_change(self, original_url):
        self.url_changes(original_url)
        return self.driver.current_url

    # Дождаться, когда URL станет указанным
    def url_to_be(self, original_url):
        WebDriverWait(self.driver, self.time).until(EC.url_to_be(original_url))

    # Вернуть текущий URL
    def get_current_url(self):
        return self.driver.current_url

    # Клик по элементу с ожиданием
    def click_and_wait_for_visibility(self, click_locator, wait_locator):
        self.click_element(click_locator)
        self.find_element_webdriverwait(wait_locator)

    # Перетащить элемент
    def drag_and_drop(self, locator_from, locator_to):
        drop_zone = self.find_element_webdriverwait(locator_to)
        ActionChains(self.driver).drag_and_drop(locator_from, drop_zone).perform()

    # Перетащить элемент в бразуере Firefox
    def drag_and_drop_firefox(self, element_from, locator_to):
        element_to = self.find_element_webdriverwait(locator_to)
        self.driver.execute_script("""
            function simulateDragDrop(sourceNode, destinationNode) {
                const eventData = { bubbles: true, cancelable: true };
                // Событие начала перетаскивания
                let dragStartEvent = new Event('dragstart', eventData);
                sourceNode.dispatchEvent(dragStartEvent);
                // События над целевым элементом
                let dragEnterEvent = new Event('dragenter', eventData);
                destinationNode.dispatchEvent(dragEnterEvent);
                let dragOverEvent = new Event('dragover', eventData);
                destinationNode.dispatchEvent(dragOverEvent);
                // Событие отпускания элемента
                let dropEvent = new Event('drop', eventData);
                destinationNode.dispatchEvent(dropEvent);
                // Завершение перетаскивания
                let dragEndEvent = new Event('dragend', eventData);
                sourceNode.dispatchEvent(dragEndEvent);
            }
            // Вызываем функцию симуляции перетаскивания
            simulateDragDrop(arguments[0], arguments[1]);
        """, element_from, element_to)