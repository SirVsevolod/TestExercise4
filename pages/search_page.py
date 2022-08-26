from .base_page import BasePage
from .locators import SearchLocators


class SearchPage(BasePage):
    def check_search_panel(self):
        return True if self.wait_visible(SearchLocators.SEARCH_PANEL) != None else False


    def check_image_button(self):
        return True if self.wait_visible(SearchLocators.IMAGE_BUTTON) != None else False


    def click_image_button(self):
        button = self.wait_visible(SearchLocators.IMAGE_BUTTON)
        button.click()
