from pages.base_page import BasePage
from locators import PersonalAccountLocators
from data import Url, UserData
import allure


class PersonalAccountPage(BasePage):
    @allure.step('Перейти в личный кабинет')
    def go_to_personal_account(self):
        self.click_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Авторизация')
    def authorization(self):
        self.add_text_to_element(PersonalAccountLocators.FIELD_EMAIL, UserData.email)
        self.add_text_to_element(PersonalAccountLocators.FIELD_PASSWORD, UserData.password)
        self.click_element(PersonalAccountLocators.BUTTON_LOG_IN)
        self.url_to_be(Url.URL_HOME)

    @allure.step('Перейти в историю заказов')
    def go_to_order_history(self):
        self.click_element(PersonalAccountLocators.BUTTON_HISTORY_ORDERS)

    @allure.step('Получить номер последнего заказа в Истории заказов')
    def get_order_id_from_order_history(self):
        self.scroll_to_element(PersonalAccountLocators.LAST_ORDER_FROM_ORDER_HISTORY)
        return self.get_text_from_element(PersonalAccountLocators.LAST_ORDER_FROM_ORDER_HISTORY)

    @allure.step('Выйти из личного кабинета')
    def log_out(self):
        self.click_element(PersonalAccountLocators.BUTTON_LOGOUT)
        self.wait_for_url_change(Url.URL_ACCOUNT_PROFILE)

    @allure.step('Дождаться загрузки кнопки Профиль')
    def is_profile_visible(self):
        return self.find_element_webdriverwait(PersonalAccountLocators.BUTTON_PROFILE)