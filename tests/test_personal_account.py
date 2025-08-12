from pages.personal_account_page import PersonalAccountPage
from data import Url
import allure

class TestPersonalAccount:
    @allure.title('Проверка авторизации и перехода в личный кабинет')
    def test_check_transition_to_personal_account(self, driver):
        account_page = PersonalAccountPage(driver)
        account_page.open_login_page()
        account_page.login()
        account_page.go_to_personal_account()
        assert account_page.is_profile_section_visible()

    @allure.title('Проверка перехода в историю заказов')
    def test_check_transition_to_order_history(self, driver):
        account_page = PersonalAccountPage(driver)
        account_page.open_login_page()
        account_page.login()
        account_page.go_to_order_history()
        assert account_page.is_order_history_page()

    @allure.title('Проверка выхода из аккаунта')
    def test_check_logout(self, driver):
        account_page = PersonalAccountPage(driver)
        account_page.open_login_page()
        account_page.login()
        account_page.logout()
        assert account_page.is_login_page()