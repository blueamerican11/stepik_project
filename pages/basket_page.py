from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        self.is_not_element_present(*BasketPageLocators.ITEM_LIST)
        assert True, "Basket is not empty"

    def should_be_message_about_empty_cart(self):
        self.browser.find_element(*BasketPageLocators.MESSAGE_IS_EMPTY)
        assert True, "Message about empty basket is not found"
