from pages.personal_account_page import PersonalAccountPage
from data import Url
import allure


class TestPersonalAccount:
    @allure.title('Проверка авторизации и перехода по клику на Личный кабинет')
    def test_check_transition_to_page_personal_account(self, driver):
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        page = PersonalAccountPage(driver)
        page.authorization()
        page.go_to_personal_account()
        button = page.is_profile_visible()
        assert button.text == 'Профиль'

    @allure.title('Проверка авторизации и перехода в раздел История заказов')
    def test_check_transition_to_page_order_history(self, driver):
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        page = PersonalAccountPage(driver)
        page.authorization()
        page.go_to_personal_account()
        page.go_to_order_history()
        assert page.get_current_url() == Url.URL_ORDER_HISTORY

    @allure.title('Проверка авторизации и выхода из аккаунта')
    def test_check_log_out_from_personal_account(self, driver):
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        page = PersonalAccountPage(driver)
        page.authorization()
        page.go_to_personal_account()
        page.log_out()
        assert page.get_current_url() == Url.URL_ENTRANCE_PERSONAL_ACCOUNT