import allure
import pytest
from pages.MainPage import SearchHelper


@allure.story('Search')
@allure.title('Test Search')
@pytest.mark.parametrize("text", ["DJ"])
def test_search(text):
    main_page = SearchHelper()
    main_page.start_site()
    main_page.fill_search_field(text)
