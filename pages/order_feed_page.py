from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import OrderFeedLocators
import allure

class OrderFeedPage(BasePage):
    @allure.step('Перейти в "Ленту заказов"')
    def go_to_order_feed(self):
        self.click_element(OrderFeedLocators.BUTTON_ORDER_FEED)

    @allure.step('Дождаться загрузки заглавного текста в "Ленте заказов"')
    def is_order_feed_visible(self):
        return self.find_element_webdriverwait(OrderFeedLocators.TEXT_ORDER_FEED)

    @allure.step('Клик на первый заказ в списке "Ленты заказов"')
    def click_to_first_order_from_order_feed(self):
        self.click_element(OrderFeedLocators.ORDER_FROM_ORDER_FEED)

    @allure.step('Дождаться загрузки текста в окне "Детали заказа"')
    def is_window_with_order_details_visible(self):
        return self.find_element_webdriverwait(OrderFeedLocators.TEXT_COMPOSITION_ORDER)

    @staticmethod
    @allure.step('Динамический локатор заказа по его id в Ленте заказов')
    def order_by_id(order_id):
        return By.XPATH, OrderFeedLocators.ORDER_ID.format(order_id=order_id)

    @allure.step('Получить значение счетчика "Выполнено за все время"')
    def get_text_from_counter_completed_for_all_time(self):
        return self.get_text_from_element(OrderFeedLocators.TEXT_COUNTER_COMPLETED_FOR_ALL_TIME)

    @allure.step('Получить значение счетчика "Выполнено за сегодня"')
    def get_text_from_counter_completed_for_today(self):
        return self.get_text_from_element(OrderFeedLocators.TEXT_COUNTER_COMPLETED_FOR_TODAY)

    @allure.step('Дождаться изменения текста в разделе "В работе"')
    def wait_for_text_in_work_to_change(self):
        while True:
            new_value = self.get_text_from_element(OrderFeedLocators.TEXT_LIST_ON_WORK)
            if new_value and new_value != "Все текущие заказы готовы!":
                return new_value