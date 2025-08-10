from pages.base_page import BasePage
from locators import PersonalAccountLocators
import allure

class PersonalAccountPage(BasePage):
    @allure.step('Авторизация пользователя')
    def authorization(self):
        self.input_text(PersonalAccountLocators.INPUT_EMAIL, "test@example.com")
        self.input_text(PersonalAccountLocators.INPUT_PASSWORD, "password123")
        self.click_element(PersonalAccountLocators.BUTTON_LOGIN)

    @allure.step('Переход в Личный кабинет')
    def go_to_personal_account(self):
        self.click_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Проверка отображения кнопки Профиль')
    def is_profile_visible(self):
        return self.find_element_webdriverwait(PersonalAccountLocators.BUTTON_PROFILE)

    @allure.step('Переход в раздел История заказов')
    def go_to_order_history(self):
        self.click_element(PersonalAccountLocators.BUTTON_ORDER_HISTORY)

    @allure.step('Выход из аккаунта')
    def log_out(self):
        self.click_element(PersonalAccountLocators.BUTTON_LOGOUT)
