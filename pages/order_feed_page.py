from pages.base_page import BasePage
from locators import OrderFeedLocators
import allure

class OrderFeedPage(BasePage):
    @allure.step('Перейти в Ленту заказов')
    def go_to_order_feed(self):
        self.click_element(OrderFeedLocators.BUTTON_ORDER_FEED)

    @allure.step('Клик по первому заказу в ленте')
    def click_to_first_order_from_order_feed(self):
        self.click_element(OrderFeedLocators.FIRST_ORDER)

    @allure.step('Проверка появления окна с деталями заказа')
    def is_window_with_order_details_visible(self):
        return self.find_element_webdriverwait(OrderFeedLocators.ORDER_DETAILS_WINDOW)

    @allure.step('Найти заказ по ID')
    def order_by_id(self, order_id):
        locator = OrderFeedLocators.ORDER_BY_ID_TEMPLATE.format(order_id=order_id)
        return self.find_element_webdriverwait((OrderFeedLocators.ORDER_BY_ID_BY, locator))

    @allure.step('Получить значение счетчика "Выполнено за всё время"')
    def get_text_from_counter_completed_for_all_time(self):
        return int(self.get_text_from_element(OrderFeedLocators.COUNTER_COMPLETED_ALL_TIME))

    @allure.step('Получить значение счетчика "Выполнено за сегодня"')
    def get_text_from_counter_completed_for_today(self):
        return int(self.get_text_from_element(OrderFeedLocators.COUNTER_COMPLETED_TODAY))

    @allure.step('Ожидание появления заказа в разделе "В работе"')
    def wait_for_text_in_work_to_change(self):
        old_text = self.get_text_from_element(OrderFeedLocators.ORDER_IN_WORK)
        return self.wait_for_text_to_change(OrderFeedLocators.ORDER_IN_WORK, old_text)
