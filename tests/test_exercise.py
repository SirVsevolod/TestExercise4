from pages.search_page import SearchPage
from pages.image_page import ImagePage
from pages.Image_search_page import ImageSearchPage

def test_should_search_panel_and_image_button(browser):
    link = 'https://yandex.ru/'
    page = SearchPage(browser, link)
    page.open()
    assert page.check_search_panel() and page.check_image_button()


def test_should_true_url(browser):
    link = 'https://yandex.ru/'
    page = SearchPage(browser, link)
    page.open()
    page.click_image_button()
    browser.switch_to.window(browser.window_handles[1])
    link = browser.current_url
    page = ImagePage(browser, link)
    assert page.check_url(link), f"ERROR: {link}"


def test_shod_true_categoryz(browser):
    link = 'https://yandex.ru/'
    page = SearchPage(browser, link)
    page.open()
    page.click_image_button()
    browser.switch_to.window(browser.window_handles[1])
    link = browser.current_url
    page = ImagePage(browser, link)
    name_categoryz_from_image_page = page.click_random_categoryz()
    link = browser.current_url
    page = ImageSearchPage(browser, link)
    name_categoryz_from_image_search_page = page.get_value_from_search_panel()
    assert name_categoryz_from_image_search_page == name_categoryz_from_image_page, f"ERROR: name_categoryz_from_image_page: {name_categoryz_from_image_page}, name_categoryz_from_image_search_page: {name_categoryz_from_image_search_page}"




