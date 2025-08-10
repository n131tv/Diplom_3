import allure
from data import Url
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage

class TestOrderFeed:

    @allure.title('Проверка всплывающего окна с деталями заказа при клике на заказ')
    def test_check_window_with_order_details(self, driver):
        page = OrderFeedPage(driver)
        driver.get(Url.URL_ORDER_FEED)
        page.click_to_first_order_from_order_feed()
        element = page.is_window_with_order_details_visible()
        assert element is not None

    @allure.title('Проверка отображения заказов из Истории заказов пользователя в Ленте заказов')
    def test_check_show_orders_from_orders_history_on_order_feed(self, driver):
        personal_account = PersonalAccountPage(driver)
        page = OrderFeedPage(driver)
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account.authorization()
        personal_account.go_to_personal_account()
        personal_account.go_to_order_history()
        order_id = personal_account.get_order_id_from_order_history()
        page.go_to_order_feed()
        element = page.order_by_id(order_id)
        assert element is not None

    @allure.title('Проверка увеличения счетчика Выполнено за все время при создании нового заказа')
    def test_check_increment_counter_completed_for_all_time_when_creating_order(self, driver):
        personal_account = PersonalAccountPage(driver)
        page = OrderFeedPage(driver)
        constructor = ConstructorPage(driver)
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account.authorization()
        page.go_to_order_feed()
        counter_before = page.get_text_from_counter_completed_for_all_time()
        constructor.go_to_constructor()
        constructor.create_order()
        constructor.close_window_order_id()
        page.go_to_order_feed()
        counter_after = page.get_text_from_counter_completed_for_all_time()
        assert counter_after > counter_before

    @allure.title('Проверка увеличения счетчика Выполнено за сегодня при создании нового заказа')
    def test_check_increment_counter_completed_for_today_when_creating_order(self, driver):
        personal_account = PersonalAccountPage(driver)
        page = OrderFeedPage(driver)
        constructor = ConstructorPage(driver)
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account.authorization()
        page.go_to_order_feed()
        counter_before = page.get_text_from_counter_completed_for_today()
        constructor.go_to_constructor()
        constructor.create_order()
        constructor.close_window_order_id()
        page.go_to_order_feed()
        counter_after = page.get_text_from_counter_completed_for_today()
        assert counter_after > counter_before

    @allure.title('Проверка появления заказа в разделе В работе после его оформления')
    def test_check_show_order_in_work_when_creating_order(self, driver):
        personal_account = PersonalAccountPage(driver)
        constructor = ConstructorPage(driver)
        page = OrderFeedPage(driver)
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account.authorization()
        constructor.create_order()
        order_id = constructor.wait_for_id_to_change()
        constructor.close_window_order_id()
        page.go_to_order_feed()
        order_id_in_work = page.wait_for_text_in_work_to_change()
        assert order_id == order_id_in_work
