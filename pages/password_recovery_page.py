from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data import Url
import allure


class PasswordRecoveryPage(BasePage):
    # Локаторы элементов страницы
    RECOVERY_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    PASSWORD_VISIBLE_FIELD = (By.XPATH, "//input[@type='text']")

    @allure.step("Открыть страницу входа в личный кабинет")
    def open_login_page(self):
        """Открывает страницу входа в личный кабинет"""
        self.open(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        return self

    @allure.step("Перейти на страницу восстановления пароля")
    def go_to_password_recovery(self):
        """Переходит на страницу восстановления пароля"""
        self.click(self.RECOVERY_LINK)
        return self

    @allure.step("Проверить что открыта страница восстановления пароля")
    def is_password_recovery_page(self):
        """Проверяет, что текущая страница - восстановление пароля"""
        return self.get_current_url() == Url.URL_RECOVERY_PASSWORD_PAGE

    @allure.step("Открыть страницу восстановления пароля напрямую")
    def open_password_recovery_page(self):
        """Открывает страницу восстановления пароля напрямую"""
        self.open(Url.URL_RECOVERY_PASSWORD_PAGE)
        return self

    @allure.step("Ввести email '{email}' и отправить форму восстановления")
    def enter_email_and_submit(self, email="test@example.com"):
        """
        Вводит email и отправляет форму
        :param email: Email для восстановления
        """
        self.type_text(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT_BUTTON)
        return self

    @allure.step("Проверить отображение формы сброса пароля")
    def is_password_reset_form_displayed(self):
        """Проверяет отображение формы сброса пароля"""
        return self.get_current_url() == Url.URL_RECOVERY_PASSWORD_FORM

    @allure.step("Переключить видимость пароля")
    def toggle_password_visibility(self):
        """Переключает видимость пароля"""
        self.click(self.SHOW_PASSWORD_BUTTON)
        return self

    @allure.step("Проверить видимость пароля")
    def is_password_visible(self):
        """Проверяет, отображается ли пароль в открытом виде"""
        return self.is_element_visible(self.PASSWORD_VISIBLE_FIELD)