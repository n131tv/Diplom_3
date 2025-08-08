from pages.password_recovery_page import PasswordRecoveryPage
from data import Url
import allure


class TestPasswordRecovery:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке Восстановить пароль')
    def test_check_transition_to_page_recovery_password(self, driver):
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        page = PasswordRecoveryPage(driver)
        new_url = page.check_transition_to_page_recovery_password()
        assert new_url == Url.URL_RECOVERY_PASSWORD_PAGE

    @allure.title('Проверка ввода почты и клик по кнопке Восстановить')
    def test_check_input_email_and_click_button_recovery(self, driver):
        driver.get(Url.URL_RECOVERY_PASSWORD_PAGE)
        page = PasswordRecoveryPage(driver)
        new_url = page.check_input_email_and_click_button_recovery()
        assert new_url == Url.URL_RECOVERY_PASSWORD_FORM

    @allure.title('Проверка активности поля при клике на иконку показать/скрыть пароль')
    def test_click_button_to_show_password(self, driver):
        driver.get(Url.URL_RECOVERY_PASSWORD_PAGE)
        page = PasswordRecoveryPage(driver)
        element = page.click_button_to_show_password()
        assert element is not None