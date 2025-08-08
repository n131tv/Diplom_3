import pytest
import allure
from data import Url
from pages.personal_account_page import PersonalAccountPage
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage

class TestMainFunctionality:
    @allure.title('Проверка перехода на Конструктор из формы авторизации')
    def test_check_go_to_constructor_from_personal_account_unauthorized(self, driver):
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account = PersonalAccountPage(driver)
        personal_account.go_to_personal_account()
        constructor = ConstructorPage(driver)
        constructor.go_to_constructor()
        text = constructor.is_constructor_visible().text
        assert text == 'Соберите бургер'

    @allure.title('Проверка перехода на Конструктор из Личного кабинета')
    def test_check_go_to_constructor_from_personal_account_authorized(self, driver):
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account = PersonalAccountPage(driver)
        personal_account.authorization()
        personal_account.go_to_personal_account()
        constructor = ConstructorPage(driver)
        constructor.go_to_constructor()
        text = constructor.is_constructor_visible().text
        assert text == 'Соберите бургер'

    @allure.title('Проверка перехода на Конструктор из Ленты заказов')
    def test_check_go_to_constructor_from_order_feed(self, driver):
        driver.get(Url.URL_ORDER_FEED)
        constructor = ConstructorPage(driver)
        constructor.go_to_constructor()
        text = constructor.is_constructor_visible().text
        assert text == 'Соберите бургер'

    @allure.title('Проверка перехода на Ленту заказов из формы авторизации')
    def test_check_go_to_order_feed_from_personal_account_unauthorized(self, driver):
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account = PersonalAccountPage(driver)
        personal_account.go_to_personal_account()
        order_feed = OrderFeedPage(driver)
        order_feed.go_to_order_feed()
        text = order_feed.is_order_feed_visible().text
        assert text == 'Лента заказов'

    @allure.title('Проверка перехода на Ленту заказов из Личного кабинета')
    def test_check_go_to_order_feed_from_personal_account_authorized(self, driver):
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account = PersonalAccountPage(driver)
        personal_account.authorization()
        personal_account.go_to_personal_account()
        order_feed = OrderFeedPage(driver)
        order_feed.go_to_order_feed()
        text = order_feed.is_order_feed_visible().text
        assert text == 'Лента заказов'

    @allure.title('Проверка перехода на Ленту заказов из Конструктора')
    def test_check_go_to_order_feed_from_constructor(self, driver):
        driver.get(Url.URL_HOME)
        order_feed = OrderFeedPage(driver)
        order_feed.go_to_order_feed()
        text = order_feed.is_order_feed_visible().text
        assert text == 'Лента заказов'

    @pytest.mark.parametrize("index", range(1, 16))
    @allure.title('Проверка открытия всплывающего окна с деталями ингредиента и закрытия этого окна')
    def test_check_ingredient_details_go_to_ingredient(self, driver, index):
        driver.get(Url.URL_HOME)
        constructor = ConstructorPage(driver)
        constructor.go_to_ingredient_by_index(index)
        constructor.close_ingredient_details()
        text = constructor.is_ingredient_details_visible().text
        assert text == 'Детали ингредиента'

    @pytest.mark.parametrize("index", range(1, 16))
    @allure.title('Проверка увеличения счетчика ингредиента при добавлении данного ингредиента в заказ')
    def test_drag_and_drop_ingredient_with_counter(self, driver, index):
        driver.get(Url.URL_HOME)
        constructor = ConstructorPage(driver)
        constructor.drag_and_drop_ingredient_by_counter(index)
        counter = constructor.get_counter_value(index)
        assert counter > 0

    @pytest.mark.parametrize("ingredients", [[1], [2, 5], [1, 4, 14]])
    @allure.title('Проверка успешного оформления заказа с разными наборами ингредиентов авторизованным пользователем')
    def test_place_order_with_multiple_ingredients(self, driver, ingredients):
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account = PersonalAccountPage(driver)
        personal_account.authorization()
        constructor = ConstructorPage(driver)
        for index in ingredients:
            constructor.drag_and_drop_ingredient_by_counter(index)
        constructor.click_button_place_order()
        text = constructor.is_window_order_id_visible().text
        assert text == 'идентификатор заказа'