from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data import Url
import allure


class PersonalAccountPage(BasePage):
    # Локаторы вынесены в константы класса
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    PROFILE_SECTION = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[contains(@href, '/account')]")

    @allure.step("Открыть страницу входа в личный кабинет")
    def open_login_page(self):
        """Открывает страницу входа в личный кабинет"""
        self.open(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        return self  # Возврат self для fluent-интерфейса

    @allure.step("Авторизоваться с email: {email}")
    def login(self, email="test@example.com", password="password"):
        """
        Выполняет авторизацию
        :param email: Email пользователя
        :param password: Пароль пользователя
        """
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    @allure.step("Перейти в личный кабинет")
    def go_to_personal_account(self):
        """Переходит в личный кабинет"""
        self.click(self.PERSONAL_ACCOUNT_LINK)
        return self

    @allure.step("Проверить видимость раздела профиля")
    def is_profile_section_visible(self):
        """Проверяет видимость раздела профиля"""
        return self.is_element_visible(self.PROFILE_SECTION)

    @allure.step("Перейти в историю заказов")
    def go_to_order_history(self):
        """Переходит в историю заказов"""
        self.click(self.ORDER_HISTORY_LINK)
        return self

    @allure.step("Проверить открытие страницы истории заказов")
    def is_order_history_page(self):
        """Проверяет, что текущая страница - история заказов"""
        return self.get_current_url() == Url.URL_ORDER_HISTORY

    @allure.step("Выйти из аккаунта")
    def logout(self):
        """Выполняет выход из аккаунта"""
        self.click(self.LOGOUT_BUTTON)
        return self

    @allure.step("Проверить открытие страницы входа")
    def is_login_page(self):
        """Проверяет, что текущая страница - страница входа"""
        return self.get_current_url() == Url.URL_ENTRANCE_PERSONAL_ACCOUNT