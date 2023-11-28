import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pages.BasePage import BasePage


class SpotifyLocators:
    LOCATOR_SEARCH_INPUT = (By.XPATH, '//input[@class="Type__TypeElement-sc-goli3j-0 ieTwfQ QO9loc33XC50mMRUCIvf"]')
    LOCATOR_REGISTRATION_BUTTON = (By.XPATH, '//button[@class="Button-sc-1dqy6lx-0 eOxaqu sibxBMlr_oxWTfBrEz2G"]')
    LOCATOR_EMAIL_INPUT = (By.ID, 'username')
    LOCATOR_CONTINUE_BUTTON = (By.XPATH, '//span[@class="ButtonInner-sc-14ud5tc-0 bhKQRg encore-bright-accent-set"]')
    LOCATOR_PASSWORD_INPUT = (By.ID, 'new-password')
    LOCATOR_NAME_INPUT = (By.ID, 'displayName')
    LOCATOR_DAY_INPUT = (By.ID, 'day')
    LOCATOR_MONTH_BUTTON = (By.ID, 'month')
    LOCATOR_YEAR_BUTTON = (By.ID, 'year')
    LOCATOR_GENDER_BUTTON = (By.XPATH, '//span[@class="Type__TypeElement-sc-goli3j-0 bGROfl TextForLabel-sc-1wen0a8-0 bYKtOf"]')
    LOCATOR_LOGIN_BUTTON = (By.XPATH, '//span[@class="ButtonInner-sc-14ud5tc-0 bzuYkS encore-inverted-light-set"]')
    LOCATOR_EMAIL_LOGIN_INPUT = (By.ID, 'login-username')
    LOCATOR_PASSWORD_LOGIN_INPUT = (By.ID, 'login-password')
    LOCATOR_CONTINUE_LOGIN_BUTTON = (By.XPATH, '//span[@class ="ButtonInner-sc-14ud5tc-0 cJdEzG encore-bright-accent-set"]')


class SearchHelper(BasePage):
    def fill_search_field(self, text):
        search_field = self.find(SpotifyLocators.LOCATOR_SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(text)
        return search_field


class RegistrationHelper(BasePage):
    def registration_button(self):
        return self.find(SpotifyLocators.LOCATOR_REGISTRATION_BUTTON).click()

    def email_field(self, email):
        email_field = self.find(SpotifyLocators.LOCATOR_EMAIL_INPUT)
        email_field.clear()
        email_field.send_keys(email)
        WebDriverWait(self.driver, 1)
        return email_field

    def continue_button(self):
        time.sleep(1)
        return self.find(SpotifyLocators.LOCATOR_CONTINUE_BUTTON).click()

    def password_field(self, password):
        password_field = self.find(SpotifyLocators.LOCATOR_PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)
        WebDriverWait(self.driver, 1)
        return password_field

    def name_field(self, name):
        name_field = self.find(SpotifyLocators.LOCATOR_NAME_INPUT)
        name_field.clear()
        name_field.send_keys(name)
        WebDriverWait(self.driver, 1)
        return name_field

    def day_field(self, day):
        day_field = self.find(SpotifyLocators.LOCATOR_DAY_INPUT)
        day_field.clear()
        day_field.send_keys(day)
        WebDriverWait(self.driver, 1)
        return day_field

    def year_field(self, year):
        year_field = self.find(SpotifyLocators.LOCATOR_YEAR_BUTTON)
        year_field.clear()
        year_field.send_keys(year)
        WebDriverWait(self.driver, 1)
        return year_field

    def month_button(self, month_name):
        month_dropdown = self.find(SpotifyLocators.LOCATOR_MONTH_BUTTON)
        month_select = Select(month_dropdown)
        month_select.select_by_visible_text(month_name)

    def gender_button(self):
        return self.find(SpotifyLocators.LOCATOR_GENDER_BUTTON).click()


class LoginHelper(BasePage):
    def login_button(self):
        return self.find(SpotifyLocators.LOCATOR_LOGIN_BUTTON).click()

    def email_field(self, email):
        email_field = self.find(SpotifyLocators.LOCATOR_EMAIL_LOGIN_INPUT)
        email_field.clear()
        email_field.send_keys(email)
        WebDriverWait(self.driver, 10)
        return email_field

    def password_field(self, password):
        password_field = self.find(SpotifyLocators.LOCATOR_PASSWORD_LOGIN_INPUT)
        password_field.clear()
        password_field.send_keys(password)
        WebDriverWait(self.driver, 10)
        return password_field

    def continue_button(self):
        return self.find(SpotifyLocators.LOCATOR_CONTINUE_LOGIN_BUTTON).click()
