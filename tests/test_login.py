import allure
import pytest
from pages.MainPage import LoginHelper


@allure.story('User Login')
@allure.title('Test User Login')
@pytest.mark.parametrize("email, password", [("testemailforlab@gmail.com", "TestPassword123")])
def test_login(email, password):
    main_page = LoginHelper()
    main_page.start_site()
    main_page.login_button()
    main_page.email_field(email)
    main_page.password_field(password)
    main_page.continue_button()
