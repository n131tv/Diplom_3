import allure
from data import Url
from pages.base_page import BasePage
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderFeed:

    @allure.title('Проверка всплывающего окна с деталями заказа при клике на заказ')
    def test_check_window_with_order_details(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open(Url.URL_ORDER_FEED)
        order_feed.click_first_order()
        assert order_feed.is_order_details_visible()

    @allure.title('Проверка отображения заказов из Истории заказов пользователя в Ленте заказов')
    def test_check_show_orders_from_orders_history_on_order_feed(self, driver):
        personal_account = PersonalAccountPage(driver)
        order_feed = OrderFeedPage(driver)

        personal_account.open(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account.authorize()
        personal_account.go_to_order_history()
        order_id = personal_account.get_first_order_id()

        order_feed.open_order_feed()
        assert order_feed.is_order_visible(order_id)

    @allure.title('Проверка увеличения счетчика "Выполнено за все время"')
    def test_check_increment_counter_completed_for_all_time_when_creating_order(self, driver):
        personal_account = PersonalAccountPage(driver)
        order_feed = OrderFeedPage(driver)
        constructor = ConstructorPage(driver)

        personal_account.open(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account.authorize()

        order_feed.open_order_feed()
        counter_before = order_feed.get_all_time_orders_count()

        constructor.open_constructor()
        constructor.create_order()
        constructor.close_order_modal()

        order_feed.open_order_feed()
        counter_after = order_feed.get_all_time_orders_count()

        assert counter_after > counter_before

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня"')
    def test_check_increment_counter_completed_for_today_when_creating_order(self, driver):
        personal_account = PersonalAccountPage(driver)
        order_feed = OrderFeedPage(driver)
        constructor = ConstructorPage(driver)

        personal_account.open(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account.authorize()

        order_feed.open_order_feed()
        counter_before = order_feed.get_today_orders_count()

        constructor.open_constructor()
        constructor.create_order()
        constructor.close_order_modal()

        order_feed.open_order_feed()
        counter_after = order_feed.get_today_orders_count()

        assert counter_after > counter_before

    @allure.title('Проверка появления заказа в разделе "В работе"')
    def test_check_show_order_in_work_when_creating_order(self, driver):
        personal_account = PersonalAccountPage(driver)
        constructor = ConstructorPage(driver)
        order_feed = OrderFeedPage(driver)

        personal_account.open(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account.authorize()

        constructor.create_order()
        order_id = constructor.get_order_id()
        constructor.close_order_modal()

        order_feed.open_order_feed()
        assert order_feed.is_order_in_progress(order_id)
