from pages.MainPage import RegistrationHelper


def test_registration():
    main_page = RegistrationHelper()
    main_page.start_site()
    main_page.registration_button()
    main_page.email_field("testemailforlab@gmail.com")
    main_page.continue_button()
    main_page.password_field("TestPassword123")
    main_page.continue_button()
    main_page.gender_button()
    main_page.name_field("Name123")
    main_page.day_field("10")
    main_page.month_button("Январь")
    main_page.year_field("1999")
    main_page.continue_button()
