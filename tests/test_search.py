from pages.MainPage import SearchHelper


def test_search():
    main_page = SearchHelper()
    main_page.start_site()
    main_page.fill_search_field("DJ")
