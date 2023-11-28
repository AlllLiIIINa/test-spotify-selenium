from pages.MainPage import LoginHelper


def test_login():
    main_page = LoginHelper()
    main_page.start_site()
    main_page.login_button()
    main_page.email_field("testemailforlab@gmail.com")
    main_page.password_field("TestPassword123")
    main_page.continue_button()
