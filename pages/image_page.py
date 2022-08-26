from .base_page import BasePage
from .locators import ImageLocators
from random import choice


class ImagePage(BasePage):
    def check_url(self, url):
        return 'https://yandex.ru/images/' in url


    def click_random_categoryz(self):
        categories = self.wait_elements(ImageLocators.CATEGORIES)
        categoryz = choice(categories)
        categoryz.click()
        return categoryz.get_attribute("data-grid-text")
