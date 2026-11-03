import allure

import urls
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestAccountPage:

    @allure.title('Проверка перехода в Личный кабинет пользователя')
    def test_account_button_click(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        main_page.click_account_button()
        email, password, _ = create_new_user_and_delete
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        account_page = AccountPage(driver)
        account_page.close_modal_for_ff()
        main_page.click_account_button()
        expected_result = 'Выход'

        assert account_page.check_logout_button() == expected_result

    @allure.title('Проверка перехода в раздел истории заказов пользователя')
    def test_orders_history_click(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        main_page.click_account_button()
        email, password, _ = create_new_user_and_delete
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        account_page = AccountPage(driver)
        account_page.close_modal_for_ff()
        main_page.click_account_button()
        account_page.get_order_history()
        expected_result = urls.ORDER_HISTORY_URL

        assert account_page.check_order_history_url() == expected_result

    # не всегдa стабилен в firefox
    @allure.title('Проверка выхода из аккаунта пользователя')
    def test_logout_from_account(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        main_page.click_account_button()
        email, password, _ = create_new_user_and_delete
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        account_page = AccountPage(driver)
        account_page.close_modal_for_ff()
        main_page.click_account_button()
        account_page.logout_from_account()
        expected_result = 'Войти'

        assert login_page.get_login_button_from_login_page() == expected_result
