import allure

from helpers import Generator
from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage

class PasswordRecoveryPage(BasePage):

    @allure.step('Ввести email, на который придет код для восстановления пароля')
    def enter_email_to_recovery_password(self):
        generator = Generator()
        self.check_element_is_clickable(PasswordRecoveryLocators.SEARCH_RECOVERY_EMAIL_INPUT_FOCUSED)
        self.click_to_element(PasswordRecoveryLocators.SEARCH_RECOVERY_EMAIL_INPUT_FOCUSED)
        self.add_text_to_element(PasswordRecoveryLocators.SEARCH_RECOVERY_EMAIL_INPUT_FOCUSED,
                                 generator.generate_random_email(5))
        self.click_to_element(PasswordRecoveryLocators.SEARCH_RECOVERY_PASSWORD_BUTTON)

    @allure.step('Проверить наличие поля для ввода пароля на странице восстановления пароля')
    def check_password_recovery_field(self):
        return self.get_text_from_element(PasswordRecoveryLocators.SEARCH_RECOVERY_PASSWORD_INPUT)

    @allure.step('Скрыть вводимый пароль')
    def click_password_make_visible_hidden(self):
        self.check_element_is_clickable(PasswordRecoveryLocators.SEARCH_ICON_PASSWORD_RECOVERY_MAKE_VISIBLE)
        self.click_to_element(PasswordRecoveryLocators.SEARCH_ICON_PASSWORD_RECOVERY_MAKE_VISIBLE)

    @allure.step('Ввести новый пароль')
    def enter_new_password(self):
        self.check_element_is_clickable(PasswordRecoveryLocators.SEARCH_RECOVERY_ENTER_NEW_PASSWORD_FOCUSED)
        self.click_to_element(PasswordRecoveryLocators.SEARCH_RECOVERY_ENTER_NEW_PASSWORD_FOCUSED)
        generator = Generator()
        self.add_text_to_element(PasswordRecoveryLocators.SEARCH_RECOVERY_ENTER_NEW_PASSWORD_FOCUSED, generator.generate_random_string(8))

    @allure.step('Проверить, что пароль скрыт')
    def check_password_visible(self):
        return self.element_is_displayed(PasswordRecoveryLocators.PASSWORD_VISIBLE_FIELD_ACTIVE)

    @allure.step('Проверить, что пароль виден')
    def check_password_hidden(self):
        return self.element_is_displayed(PasswordRecoveryLocators.PASSWORD_HIDE_FIELD_NOT_ACTIVE)
