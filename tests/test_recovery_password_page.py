import allure

from pages.password_recovery_page import PasswordRecoveryPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestPasswordRecoveryPage:

    @allure.title('Проверка возможности восстановления пароля')
    def test_password_recovery(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        main_page = MainPage(driver)
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.click_to_recovery_password_link()
        password_recovery_page.enter_email_to_recovery_password()
        expected_result = 'Пароль'

        assert password_recovery_page.check_password_recovery_field() == expected_result

    @allure.title('Проверка видимости вводимого пароля')
    def test_password_is_visible(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        main_page = MainPage(driver)
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.click_to_recovery_password_link()
        password_recovery_page.enter_email_to_recovery_password()
        password_recovery_page.enter_new_password()
        password_recovery_page.click_password_make_visible_hidden()

        assert password_recovery_page.check_password_visible()

    @allure.title('Проверка возможности скрыть вводимый пароль')
    def test_password_is_hidden(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        main_page = MainPage(driver)
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.click_to_recovery_password_link()
        password_recovery_page.enter_email_to_recovery_password()
        password_recovery_page.enter_new_password()
        password_recovery_page.click_password_make_visible_hidden()
        password_recovery_page.click_password_make_visible_hidden()

        assert password_recovery_page.check_password_hidden()
