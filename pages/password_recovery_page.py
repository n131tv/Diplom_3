from data import UserData
from pages.base_page import BasePage
from locators import PasswordRecoveryLocators
import allure


class PasswordRecoveryPage(BasePage):
    @allure.step('Переход на страницу восстановления пароля')
    def check_transition_to_page_recovery_password(self):
        original_url = self.driver.current_url
        self.click_element(PasswordRecoveryLocators.BUTTON_RECOVERY_PASSWORD_PAGE)
        return self.wait_for_url_change(original_url)

    @allure.step('Ввод почты и клик по кнопке Восстановить')
    def check_input_email_and_click_button_recovery(self):
        original_url = self.driver.current_url
        self.add_text_to_element(PasswordRecoveryLocators.FIELD_EMAIL, UserData.email)
        self.click_element(PasswordRecoveryLocators.BUTTON_RECOVERY)
        return self.wait_for_url_change(original_url)

    @allure.step('Клик по иконке показать пароль')
    def click_button_to_show_password(self):
        self.add_text_to_element(PasswordRecoveryLocators.FIELD_EMAIL, UserData.email)
        self.click_element(PasswordRecoveryLocators.BUTTON_RECOVERY)
        self.add_text_to_element(PasswordRecoveryLocators.FIELD_PASSWORD, UserData.password)
        self.click_element(PasswordRecoveryLocators.ICON_HIDE_PASSWORD)
        self.click_element(PasswordRecoveryLocators.ICON_HIDE_PASSWORD)
        element = self.find_element_webdriverwait(PasswordRecoveryLocators.FIELD_FRAMING_ILLUMINATION)
        return element