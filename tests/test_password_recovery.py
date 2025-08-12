from pages.password_recovery_page import PasswordRecoveryPage
from data import Url
import allure

class TestPasswordRecovery:
    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_check_transition_to_page_recovery_password(self, driver):
        page = PasswordRecoveryPage(driver)
        page.open_login_page()
        page.go_to_password_recovery()
        assert page.is_password_recovery_page()

    @allure.title('Проверка восстановления пароля')
    def test_check_password_recovery_flow(self, driver):
        page = PasswordRecoveryPage(driver)
        page.open_password_recovery_page()
        page.enter_email_and_submit()
        assert page.is_password_reset_form_displayed()

    @allure.title('Проверка показа/скрытия пароля')
    def test_check_password_visibility_toggle(self, driver):
        page = PasswordRecoveryPage(driver)
        page.open_password_recovery_page()
        page.toggle_password_visibility()
        assert page.is_password_visible()