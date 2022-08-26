from .base_page import BasePage
from .locators import ImageSearchLocators


class ImageSearchPage(BasePage):
    def get_value_from_search_panel(self):
        element = self.wait_visible(ImageSearchLocators.SEARCH_PANEL)
        return element.get_attribute("value")
