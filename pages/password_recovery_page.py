from pages.base_page import BasePage
from locators import PasswordRecoveryLocators
import allure

class PasswordRecoveryPage(BasePage):
    @allure.step('Переход на страницу восстановления пароля')
    def check_transition_to_page_recovery_password(self):
        self.click_element(PasswordRecoveryLocators.BUTTON_RECOVERY_PASSWORD)
        return self.get_current_url()

    @allure.step('Ввод email и клик по кнопке Восстановить')
    def check_input_email_and_click_button_recovery(self):
        self.input_text(PasswordRecoveryLocators.INPUT_EMAIL, "test@example.com")
        self.click_element(PasswordRecoveryLocators.BUTTON_SUBMIT_RECOVERY)
        return self.get_current_url()

    @allure.step('Клик по иконке показать/скрыть пароль')
    def click_button_to_show_password(self):
        self.click_element(PasswordRecoveryLocators.BUTTON_SHOW_PASSWORD)
        return self.find_element_webdriverwait(PasswordRecoveryLocators.INPUT_PASSWORD)
