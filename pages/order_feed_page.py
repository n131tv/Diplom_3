from selenium.webdriver.common.by import By
from .base_page import BasePage
from data import Url
import allure


class OrderFeedPage(BasePage):
    # Локаторы элементов
    ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    ALL_TIME_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    FIRST_ORDER_LINK = (By.XPATH, "(//div[contains(@class, 'OrderHistory_link')])[1]")
    IN_PROGRESS_SECTION = (By.XPATH, "//section[contains(@class, 'OrderFeed_inProgress')]")

    @allure.step('Открыть страницу ленты заказов')
    def open_order_feed(self):
        """
        Открывает страницу ленты заказов
        :return: self для поддержки fluent-интерфейса
        """
        self.open(Url.URL_ORDER_FEED)
        return self

    @allure.step('Кликнуть на первый заказ в ленте')
    def click_first_order(self):
        """
        Кликает на первый заказ в ленте
        :return: self
        """
        self.click(self.FIRST_ORDER_LINK)
        return self

    @allure.step('Проверить видимость деталей заказа')
    def is_order_details_visible(self):
        """
        Проверяет видимость модального окна с деталями заказа
        :return: bool
        """
        return self.is_element_visible(self.ORDER_DETAILS_MODAL)

    @allure.step('Получить количество заказов за все время')
    def get_all_time_orders_count(self):
        """
        Получает количество выполненных заказов за все время
        :return: int
        """
        count_text = self.get_text(self.ALL_TIME_ORDERS_COUNT)
        return int(count_text) if count_text.isdigit() else 0

    @allure.step('Проверить видимость раздела "В работе"')
    def is_in_progress_section_visible(self):
        """
        Проверяет видимость раздела "В работе"
        :return: bool
        """
        return self.is_element_visible(self.IN_PROGRESS_SECTION)
