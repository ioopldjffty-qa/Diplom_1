import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import data

class MainPage(BasePage):

    @allure.step('Кликнуть по кнопке авторизации на сайте на главной странице')
    def click_login_button(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE)
        self.click_to_element(MainPageLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE)

    @allure.step('Кликнуть по кнопке перехода в личный кабинет пользователя')
    def click_account_button(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_PERSONAL_ACCOUNT_LINK)
        self.click_to_element(MainPageLocators.SEARCH_PERSONAL_ACCOUNT_LINK)

    @allure.step('Кликнуть по ссылке перехода в конструктор')
    def click_constructor_link(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_CONSTRUCTOR)
        self.click_to_element(MainPageLocators.SEARCH_CONSTRUCTOR)

    @allure.step('Проверить, что произошел переход на страницу конструктура')
    def check_constructor_title(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_CONSTRUCTOR_TITLE_TEXT)

    @allure.step('Перейти на страницу ленты заказов')
    def get_feed(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_FEED_VIA_MAIN_PAGE)
        self.click_to_element(MainPageLocators.SEARCH_FEED_VIA_MAIN_PAGE)

    @allure.step('Открыть модальное окно с информацией об ингредиенте')
    def get_ingredient_details(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_INGREDIENT_DETAILS)
        self.click_to_element(MainPageLocators.SEARCH_INGREDIENT_DETAILS)

    @allure.step('Проверить, что окно с информацией об ингредиенте открылось')
    def check_ingredient_title_text(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_INGREDIENT_DETAILS_MODAL_TITLE)

    @allure.step('Закрыть модальное окно с информацией об ингредиенте')
    def close_ingredient_details_modal(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_INGREDIENT_DETAILS_MODAL_CLOSE)
        self.click_to_element(MainPageLocators.SEARCH_INGREDIENT_DETAILS_MODAL_CLOSE)

    @allure.step('Проверить, что окно с информацией об ингредиенте закрылось')
    def check_ingredient_details_modal_closed(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_SAUCES_SECTION)

    @allure.step('Проверить колличество ингредиентов до добавления в корзину')
    def check_count_before_ingredient_added(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_COUNTER_INGREDIENT_NOT_ADDED)

    @allure.step('Перетащить ингредиент в корзину')
    def add_ingredient(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_FIRST_BUN_IN_CONSTRUCTOR)
        self.check_element_is_clickable(MainPageLocators.SEARCH_TARGET_BASKET)
        if data.DRIVER_NAME == data.browser_chrome:
            self.move_the_element(MainPageLocators.SEARCH_FIRST_BUN_IN_CONSTRUCTOR, MainPageLocators.SEARCH_TARGET_BASKET)
        elif data.DRIVER_NAME == data.browser_firefox:
            self.drag_and_drop_element(MainPageLocators.SEARCH_FIRST_BUN_IN_CONSTRUCTOR,
                                       MainPageLocators.SEARCH_TARGET_BASKET)

    @allure.step('Проверить колличество ингредиентов после его добавления в корзину')
    def check_count_after_ingredient_added(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_COUNTER_INGREDIENT_ADDED)

    @allure.step('Сделать заказ, кликнув по кнопке заказа')
    def click_make_order_button(self):
        self.check_element_is_clickable(MainPageLocators.SEARCH_MAKE_ORDER_BUTTON)
        self.click_to_element(MainPageLocators.SEARCH_MAKE_ORDER_BUTTON)

    @allure.step('Проверить наличие модального окна с информацией, что заказ сделан')
    def check_order_id_text(self):
        return self.get_text_from_element(MainPageLocators.SEARCH_ORDER_ID_TEXT)

    @allure.step('Подождать появления id заказа в модальном окне')
    def wait_and_get_order_id(self):
        order_id = '9999'
        while order_id == '9999':
            order_id = self.get_text_from_element(MainPageLocators.SEARCH_ORDER_ID_IN_MODAL)
        return order_id

    @allure.step('Получить id заказа')
    def check_order_id(self):
        element_text = self.get_text_from_element(MainPageLocators.SEARCH_ORDER_ID_IN_MODAL)
        return element_text

    @allure.step('Сделать заказ')
    def make_order(self):
        self.add_ingredient()
        self.click_make_order_button()

    @allure.step('Закрыть модальное окно с информацией о заказе')
    def close_new_order_modal(self):
        close_button = self.find_element_with_wait(MainPageLocators.SEARCH_CLOSE_MADE_ORDER_BUTTON)
        self.js_button_click(close_button)
