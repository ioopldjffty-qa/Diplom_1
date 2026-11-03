import allure

from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    @allure.step('Проверить нахождение на странице ленты заказов')
    def check_feed_title_text(self):
        return self.get_text_from_element(OrderFeedPageLocators.SEARCH_FEED_TITLE_TEXT)

    @allure.step('Кликнуть на заказ для открытия модального окна с деталями заказа')
    def click_to_order(self):
        self.check_element_is_clickable(OrderFeedPageLocators.SEARCH_MADE_ORDER)
        self.click_to_element(OrderFeedPageLocators.SEARCH_MADE_ORDER)

    @allure.step('Проверить открытие модального окна с деталями заказа')
    def get_order_details_text(self):
        return self.get_text_from_element(OrderFeedPageLocators.SEARCH_ORDER_DETAILS_TEXT)

    @allure.step('Получить количество заказов за все время')
    def get_orders_count_all_time(self):
        self.element_is_displayed(OrderFeedPageLocators.SEARCH_COUNTER_OF_ALL_TIME_IN_FEED)
        all_element_text = self.get_text_from_element(OrderFeedPageLocators.SEARCH_COUNTER_OF_ALL_TIME_IN_FEED)
        return all_element_text

    @allure.step('Получить количество заказов за сегодня')
    def get_orders_count_today(self):
        self.scroll_into_view(OrderFeedPageLocators.SEARCH_COUNTER_FOR_TODAY_IN_FEED)
        self.element_is_displayed(OrderFeedPageLocators.SEARCH_COUNTER_FOR_TODAY_IN_FEED)
        today_element_text = self.get_text_from_element(OrderFeedPageLocators.SEARCH_COUNTER_FOR_TODAY_IN_FEED)
        return today_element_text

    @allure.step('Получить данные о заказах в работе')
    def get_orders_in_progress(self):
        self.element_is_displayed(OrderFeedPageLocators.SEARCH_ORDERS_IN_WORK_DONE)
        self.find_element_with_wait(OrderFeedPageLocators.SEARCH_ORDERS_IN_WORK_DONE)
        self.wait_disappear_element(OrderFeedPageLocators.SEARCH_ORDERS_IN_WORK_DONE)
        element_text = self.get_text_from_element(OrderFeedPageLocators.SEARCH_ORDER_IN_WORK)
        return element_text

    @allure.step('Подождать, когда появится номер заказа в работе')
    def wait_for_order_id_in_progress(self):
        order_id = 'Все текущие заказы готовы!'
        while order_id == 'Все текущие заказы готовы!':
            order_id = self.get_text_from_element(OrderFeedPageLocators.SEARCH_ORDER_IN_WORK)
            self.wait_for_order_id_in_progress(OrderFeedPageLocators.SEARCH_ORDER_IN_WORK)
        return order_id

    @allure.step('Проверить наличие номера заказа в работе')
    def check_order_id_in_progress(self):
        element_text = self.get_text_from_element(OrderFeedPageLocators.SEARCH_ORDER_IN_WORK)
        return element_text

    @allure.step('Проверить наличие номера заказа в ленте')
    def check_order_id_in_feed(self):
        self.element_is_displayed(OrderFeedPageLocators.SEARCH_ORDER_ID_IN_FEED)
        element_text =  self.get_text_from_element(OrderFeedPageLocators.SEARCH_ORDER_ID_IN_FEED)
        return element_text.lstrip('#')
