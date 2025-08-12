import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import ConstructorLocators
import data


class ConstructorPage(BasePage):

    @allure.step('Перейти в конструктор')
    def go_to_constructor(self):
        self.click_element(ConstructorLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Проверить отображение заглавного текста в Конструкторе')
    def is_constructor_visible(self):
        return self.find_element_webdriverwait(ConstructorLocators.TEXT_COLLECT_BURGER)

    @staticmethod
    @allure.step('Получить локатор ингредиента по индексу: {index}')
    def burger_ingredient_by_index(index):
        return By.XPATH, ConstructorLocators.BURGER_INGREDIENT.format(index=index)

    @allure.step('Перейти к ингредиенту по индексу: {index}')
    def go_to_ingredient_by_index(self, index):
        self.click_element(self.burger_ingredient_by_index(index))

    @allure.step('Проверить отображение деталей ингредиента')
    def is_ingredient_details_visible(self):
        return self.find_element_webdriverwait(ConstructorLocators.TEXT_INGREDIENT_DETAILS)

    @allure.step('Закрыть окно деталей ингредиента')
    def close_ingredient_details(self):
        self.click_element(ConstructorLocators.BUTTON_CLOSE_INGREDIENT_DETAILS)

    @allure.step('Прокрутить к ингредиенту по индексу: {index}')
    def scroll_to_ingredient(self, index):
        self.scroll_to_element(self.burger_ingredient_by_index(index))

    @allure.step('Перетащить ингредиент по индексу: {index} в зону: {drop_zone_locator}')
    def drag_and_drop_ingredient(self, index, drop_zone_locator):
        self.scroll_to_ingredient(index)
        ingredient = self.find_element_webdriverwait(self.burger_ingredient_by_index(index))
        self.drag_and_drop(ingredient, drop_zone_locator)

    @allure.step('Перетащить ингредиент по индексу: {index} в Firefox')
    def drag_and_drop_ingredient_firefox(self, index, drop_zone_locator):
        ingredient = self.find_element_webdriverwait(self.burger_ingredient_by_index(index))
        self.drag_and_drop_firefox(ingredient, drop_zone_locator)

    @allure.step('Перетащить ингредиент по индексу: {index} с учётом браузера')
    def drag_and_drop_ingredient_by_counter(self, index):
        if data.DRIVER_NAME == 'chrome':
            self.drag_and_drop_ingredient(index, ConstructorLocators.DROP_ZONE_CONSTRUCTOR)
        else:
            self.drag_and_drop_ingredient_firefox(index, ConstructorLocators.DROP_ZONE_CONSTRUCTOR)

    @allure.step('Нажать кнопку "Оформить заказ"')
    def click_button_place_order(self):
        self.click_element(ConstructorLocators.BUTTON_PLACE_ORDER)

    @allure.step('Создать заказ')
    def create_order(self):
        self.drag_and_drop_ingredient_by_counter(2)
        self.click_button_place_order()

    @allure.step('Проверить отображение окна с номером заказа')
    def is_window_order_id_visible(self):
        return self.find_element_webdriverwait(ConstructorLocators.TEXT_ORDER_ID)

    @allure.step('Ожидание изменения номера заказа')
    def wait_for_id_to_change(self):
        self.wait_for_text_to_change(
            locator=ConstructorLocators.TEXT_IN_ORDER_ID,
            initial_text="9999"
        )
        return f"0{self.get_text_from_element(ConstructorLocators.TEXT_IN_ORDER_ID)}"

    @allure.step('Закрыть окно с номером заказа')
    def close_window_order_id(self):
        self.click_element(ConstructorLocators.BUTTON_CLOSE_ORDER_ID)

    @staticmethod
    @allure.step('Получить локатор счетчика ингредиента по индексу: {index}')
    def get_ingredient_by_counter(index):
        return By.XPATH, ConstructorLocators.INGREDIENT_COUNTER.format(index=index)

    @allure.step('Получить значение счётчика ингредиента по индексу: {index}')
    def get_counter_value(self, index):
        counter_element = self.find_element_webdriverwait(self.get_ingredient_by_counter(index))
        return int(counter_element.text)

