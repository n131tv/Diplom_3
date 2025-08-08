from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import ConstructorLocators
import allure
import data
import time


class ConstructorPage(BasePage):
    @allure.step('Перейти в конструктор')
    def go_to_constructor(self):
        self.click_element(ConstructorLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Дождаться загрузки заглавного текста в Конструкторе')
    def is_constructor_visible(self):
        return self.find_element_webdriverwait(ConstructorLocators.TEXT_COLLECT_BURGER)

    @staticmethod
    @allure.step('Динамический локатор ингредиента по индексу')
    def burger_ingredient_by_index(index):
        return By.XPATH, ConstructorLocators.BURGER_INGREDIENT.format(index=index)

    @allure.step('Открыть "Детали ингредиента" по индексу ингредиента')
    def go_to_ingredient_by_index(self, index):
        locator = self.burger_ingredient_by_index(index)
        self.click_element(locator)

    @allure.step('Дождаться загрузки текста в окне Детали ингредиента')
    def is_ingredient_details_visible(self):
        return self.find_element_webdriverwait(ConstructorLocators.TEXT_INGREDIENT_DETAILS)

    @allure.step('Закрыть окно Детали ингредиента')
    def close_ingredient_details(self):
        self.click_element(ConstructorLocators.BUTTON_CLOSE_INGREDIENT_DETAILS)

    @allure.step('Скроллить до ингредиента')
    def scroll_to_ingredient(self, index):
        locator = self.burger_ingredient_by_index(index)
        self.scroll_to_element(locator)

    @allure.step('Перетащить ингредиент по индексу в зону конструктора')
    def drag_and_drop_ingredient(self, index, drop_zone_locator):
        self.scroll_to_ingredient(index)
        ingredient = self.find_element_webdriverwait(self.burger_ingredient_by_index(index))
        self.drag_and_drop(ingredient, drop_zone_locator)

    @allure.step('Перетащить ингредиент по индексу в зону конструктора в бразуере Firefox')
    def drag_and_drop_ingredient_firefox(self, index, locator_to):
        element_from = self.find_element_webdriverwait(self.burger_ingredient_by_index(index))
        self.drag_and_drop_firefox(element_from, locator_to)

    @allure.step('Выбор метода drag_and_drop, в зависимости от браузера')
    def drag_and_drop_ingredient_by_counter(self, index):
        if data.DRIVER_NAME == 'chrome':
            self.drag_and_drop_ingredient(index, ConstructorLocators.DROP_ZONE_CONSTRUCTOR)
        else:
            self.drag_and_drop_ingredient_firefox(index, ConstructorLocators.DROP_ZONE_CONSTRUCTOR)

    @allure.step('Клик по кнопке Оформить заказ')
    def click_button_place_order(self):
        self.click_element(ConstructorLocators.BUTTON_PLACE_ORDER)

    @allure.step('Оформить заказ')
    def create_order(self):
        if data.DRIVER_NAME == 'chrome':
            self.drag_and_drop_ingredient(2, ConstructorLocators.DROP_ZONE_CONSTRUCTOR)
        else:
            self.drag_and_drop_ingredient_firefox(2, ConstructorLocators.DROP_ZONE_CONSTRUCTOR)
        self.click_button_place_order()

    @allure.step('Дождаться появления окна с идентификатором заказа')
    def is_window_order_id_visible(self):
        return self.find_element_webdriverwait(ConstructorLocators.TEXT_ORDER_ID)

    @allure.step('Дождаться изменения текста идентификатора заказа')
    def wait_for_id_to_change(self):
        max_attempts = 10  # Максимальное количество попыток
        for _ in range(max_attempts):  # Цикл с фиксированным количеством итераций
            new_value = self.get_text_from_element(ConstructorLocators.TEXT_IN_ORDER_ID)
            if new_value and new_value != "9999":
                return f'0{new_value}'
            time.sleep(1)  # Пауза перед следующей попыткой
        raise Exception("Не удалось дождаться изменения текста идентификатора заказа.")

    @allure.step('Закрыть окно с id заказа')
    def close_window_order_id(self):
        self.click_element(ConstructorLocators.BUTTON_CLOSE_ORDER_ID)

    @staticmethod
    @allure.step('Динамический локатор счетчика по индексу')
    def get_ingredient_by_counter(index):
        return By.XPATH, ConstructorLocators.INGREDIENT_COUNTER.format(index=index)

    @allure.step('Получить значение счетчика ингредиента по индексу')
    def get_counter_value(self, index):
        counter_locator = self.get_ingredient_by_counter(index)
        counter_element = self.find_element_webdriverwait(counter_locator)
        return int(counter_element.text)