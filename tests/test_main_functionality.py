import pytest
import allure
from data import Url
from pages.base_page import BasePage
from pages.personal_account_page import PersonalAccountPage
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
from helpers.constructor_helpers import add_ingredients_to_constructor


class TestMainFunctionality:
    @allure.title('Проверка перехода на Конструктор из формы авторизации')
    def test_check_go_to_constructor_from_personal_account_unauthorized(self, driver):
        personal_account = PersonalAccountPage(driver)
        personal_account.open(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account.go_to_personal_account()

        constructor = ConstructorPage(driver)
        constructor.go_to_constructor()
        assert constructor.get_constructor_title() == 'Соберите бургер'

    @allure.title('Проверка перехода на Конструктор из Личного кабинета')
    def test_check_go_to_constructor_from_personal_account_authorized(self, driver):
        personal_account = PersonalAccountPage(driver)
        personal_account.open(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account.authorize()
        personal_account.go_to_personal_account()

        constructor = ConstructorPage(driver)
        constructor.go_to_constructor()
        assert constructor.get_constructor_title() == 'Соберите бургер'

    @allure.title('Проверка перехода на Ленту заказов из Конструктора')
    def test_check_go_to_order_feed_from_constructor(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open(Url.URL_HOME)
        order_feed.go_to_order_feed()
        assert order_feed.get_order_feed_title() == 'Лента заказов'

    @pytest.mark.parametrize("index", range(1, 16))
    @allure.title('Проверка открытия деталей ингредиента')
    def test_check_ingredient_details(self, driver, index):
        constructor = ConstructorPage(driver)
        constructor.open(Url.URL_HOME)
        constructor.open_ingredient_details(index)
        constructor.close_ingredient_details()
        assert constructor.get_ingredient_details_title() == 'Детали ингредиента'

    @pytest.mark.parametrize("ingredients", [[1], [2, 5], [1, 4, 14]])
    @allure.title('Проверка оформления заказа')
    def test_place_order_with_multiple_ingredients(self, driver, ingredients):
        personal_account = PersonalAccountPage(driver)
        personal_account.open(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account.authorize()

        constructor = ConstructorPage(driver)
        add_ingredients_to_constructor(constructor, ingredients)
        constructor.place_order()
        assert constructor.get_order_confirmation_text() == 'идентификатор заказа'
