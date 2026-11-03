import allure

from pages.account_page import AccountPage
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestOrderFeedPage:

    @allure.title('Проверка открытия модального окна с деталями заказа')
    def test_get_order_details(self, driver):
        main_page = MainPage(driver)
        main_page.get_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_to_order()
        expected_result = 'Cостав'

        assert order_feed_page.get_order_details_text() == expected_result

    @allure.title('Проверка увеличения счётчика "Выполнено за всё время" при создании нового заказа')
    def test_order_counts_in_feed_page(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        main_page.click_login_button()
        email, password, _ = create_new_user_and_delete
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        account_page = AccountPage(driver)
        account_page.close_modal_for_ff()
        main_page.get_feed()
        order_feed_page = OrderFeedPage(driver)
        before_order = order_feed_page.get_orders_count_all_time()
        main_page.click_constructor_link()
        main_page.make_order()
        main_page.close_new_order_modal()
        account_page.close_modal_for_ff()
        account_page.close_modal_for_chrome()
        main_page.get_feed()
        after_order = order_feed_page.get_orders_count_all_time()

        assert int(before_order) < int(after_order)

    @allure.title('Проверка увеличения счётчика "Выполнено за сегодня" при создании нового заказа')
    def test_order_counts_today(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        main_page.click_login_button()
        email, password, _ = create_new_user_and_delete
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        account_page = AccountPage(driver)
        account_page.close_modal_for_ff()
        main_page.get_feed()
        order_feed_page = OrderFeedPage(driver)
        before_order = order_feed_page.get_orders_count_today()
        main_page.click_constructor_link()
        main_page.make_order()
        main_page.close_new_order_modal()
        account_page.close_modal_for_ff()
        account_page.close_modal_for_chrome()
        main_page.get_feed()
        after_order = order_feed_page.get_orders_count_today()

        assert int(before_order) < int(after_order)

    @allure.title('Проверка наличия id заказа после его создания в разделе "В работе".')
    def test_order_in_progress(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        main_page.click_login_button()
        email, password, _ = create_new_user_and_delete
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        account_page = AccountPage(driver)
        account_page.close_modal_for_ff()
        main_page.make_order()
        main_page.wait_and_get_order_id()
        id_in_modal = main_page.check_order_id()
        main_page.close_new_order_modal()
        account_page.close_modal_for_chrome()
        account_page.close_modal_for_ff()
        main_page.get_feed()
        order_feed_page = OrderFeedPage(driver)
        id_in_progress = order_feed_page.get_orders_in_progress()

        assert int(id_in_modal) == int(id_in_progress)

    @allure.title('Проверка: заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_history_order_in_feed_page(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        main_page.click_login_button()
        email, password, _ = create_new_user_and_delete
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        account_page = AccountPage(driver)
        account_page.close_modal_for_ff()
        main_page.make_order()
        main_page.close_new_order_modal()
        account_page.close_modal_for_chrome()
        account_page.close_modal_for_ff()
        main_page.click_account_button()
        account_page = AccountPage(driver)
        account_page.get_order_history()
        history_order_id = account_page.get_order_id_in_history()
        main_page.get_feed()
        order_feed_page = OrderFeedPage(driver)
        feed_order_id = order_feed_page.check_order_id_in_feed()

        assert int(history_order_id) == int(feed_order_id)
