import allure
import pytest
from pages.MainPage import RegistrationHelper


@allure.story('User Registration')
@allure.title('Test User Registration')
@pytest.mark.parametrize("email, password, name, day, month, year", [("testemailforlab@gmail.com", "TestPassword123", "Name123", "10", "Январь", "1999")])
def test_registration(email, password, name, day, month, year):
    main_page = RegistrationHelper()
    main_page.start_site()
    main_page.registration_button()
    main_page.email_field(email)
    main_page.continue_button()
    main_page.password_field(password)
    main_page.continue_button()
    main_page.gender_button()
    main_page.name_field(name)
    main_page.day_field(day)
    main_page.month_button(month)
    main_page.year_field(year)
    main_page.continue_button()
    main_page.continue_button()
