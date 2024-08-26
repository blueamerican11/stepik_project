from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart_from_product_page(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def check_message_about_item_add_to_cart(self, book_name):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_CART).text
        assert book_name == message, f"Book name in message is not correct, actual message: {message}, " \
                                     f"actual book name: {book_name}"

    def check_price_in_cart(self, price_in_item_page):
        price_in_cart = self.browser.find_element(*ProductPageLocators.PRICE_IN_CART).text
        assert price_in_item_page in price_in_cart, f"Price in cart is not correct, actual price: {price_in_item_page}"

    def get_item_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        return book_name

    def get_item_price(self):
        price_in_item_page = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        return price_in_item_page

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_TO_CART), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_TO_CART), \
            "Success message is not disappeared, but should be"
