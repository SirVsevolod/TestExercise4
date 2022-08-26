from selenium.webdriver.common.by import By


class SearchLocators():
    SEARCH_PANEL = (By.CSS_SELECTOR, "input.input__control")
    IMAGE_BUTTON = (By.CSS_SELECTOR, "a[data-id='images']")


class ImageLocators():
    CATEGORIES = (By.CSS_SELECTOR, "div.PopularRequestList-Item")


class ImageSearchLocators(SearchLocators):
    pass
