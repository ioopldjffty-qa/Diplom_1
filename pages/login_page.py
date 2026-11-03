import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

class LoginPage(BasePage):

    @allure.step('Проверить наличие кнопки авторизации на странице входа')
    def get_login_button_from_login_page(self):
        return self.get_login_button_text()

    @allure.step('Кликнуть по ссылке восстановления пароля')
    def click_to_recovery_password_link(self):
        self.check_element_is_clickable(LoginPageLocators.SEARCH_PASSWORD_RECOVERY_LINK_VIA_LOGIN_PAGE)
        self.click_to_element(LoginPageLocators.SEARCH_PASSWORD_RECOVERY_LINK_VIA_LOGIN_PAGE)

    @allure.step('Ввести email пользователя')
    def email_enter(self, email):
        self.add_text_to_element(LoginPageLocators.SEARCH_LOGIN_EMAIL_INPUT, email)

    @allure.step('Ввести пароль пользователя')
    def password_enter(self, password):
        self.add_text_to_element(LoginPageLocators.SEARCH_LOGIN_PASSWORD_INPUT, password)

    @allure.step('Кликнуть по кнопке входа на сайт')
    def login_button_click(self):
        self.check_element_is_clickable(LoginPageLocators.SEARCH_LOGIN_BUTTON)
        self.click_to_element(LoginPageLocators.SEARCH_LOGIN_BUTTON)

    @allure.step('Авторизоваться на сайте')
    def user_login(self, email, password):
        self.email_enter(email)
        self.password_enter(password)
        self.login_button_click()

    @allure.step('Проверить наличие кнопки входа на сайт')
    def get_login_button_text(self):
        return self.get_text_from_element(LoginPageLocators.SEARCH_LOGIN_BUTTON)
