from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import ConstructorLocators
import allure
import data

class ConstructorPage(BasePage):
    @allure.step('Перейти в конструктор')
    def go_to_constructor(self):
        self.click_element(ConstructorLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Дождаться загрузки заглавного текста в Конструкторе')
    def is_constructor_visible(self):
        return self.find_element_webdriverwait(ConstructorLocators.TEXT_COLLECT_BURGER)

    @staticmethod
    def burger_ingredient_by_index(index):
        return By.XPATH, ConstructorLocators.BURGER_INGREDIENT.format(index=index)

    def go_to_ingredient_by_index(self, index):
        self.click_element(self.burger_ingredient_by_index(index))

    def is_ingredient_details_visible(self):
        return self.find_element_webdriverwait(ConstructorLocators.TEXT_INGREDIENT_DETAILS)

    def close_ingredient_details(self):
        self.click_element(ConstructorLocators.BUTTON_CLOSE_INGREDIENT_DETAILS)

    def scroll_to_ingredient(self, index):
        self.scroll_to_element(self.burger_ingredient_by_index(index))

    def drag_and_drop_ingredient(self, index, drop_zone_locator):
        self.scroll_to_ingredient(index)
        ingredient = self.find_element_webdriverwait(self.burger_ingredient_by_index(index))
        self.drag_and_drop(ingredient, drop_zone_locator)

    def drag_and_drop_ingredient_firefox(self, index, drop_zone_locator):
        ingredient = self.find_element_webdriverwait(self.burger_ingredient_by_index(index))
        self.drag_and_drop_firefox(ingredient, drop_zone_locator)

    def drag_and_drop_ingredient_by_counter(self, index):
        if data.DRIVER_NAME == 'chrome':
            self.drag_and_drop_ingredient(index, ConstructorLocators.DROP_ZONE_CONSTRUCTOR)
        else:
            self.drag_and_drop_ingredient_firefox(index, ConstructorLocators.DROP_ZONE_CONSTRUCTOR)

    def click_button_place_order(self):
        self.click_element(ConstructorLocators.BUTTON_PLACE_ORDER)

    def create_order(self):
        self.drag_and_drop_ingredient_by_counter(2)
        self.click_button_place_order()

    def is_window_order_id_visible(self):
        return self.find_element_webdriverwait(ConstructorLocators.TEXT_ORDER_ID)

    def wait_for_id_to_change(self):
        def id_is_valid(driver):
            element = driver.find_element(*ConstructorLocators.TEXT_IN_ORDER_ID)
            text = element.text
            return text and text != "9999"

        WebDriverWait(self.driver, self.timeout).until(id_is_valid)
        return f"0{self.get_text_from_element(ConstructorLocators.TEXT_IN_ORDER_ID)}"

    def close_window_order_id(self):
        self.click_element(ConstructorLocators.BUTTON_CLOSE_ORDER_ID)

    @staticmethod
    def get_ingredient_by_counter(index):
        return By.XPATH, ConstructorLocators.INGREDIENT_COUNTER.format(index=index)

    def get_counter_value(self, index):
        counter_element = self.find_element_webdriverwait(self.get_ingredient_by_counter(index))
        return int(counter_element.text)
