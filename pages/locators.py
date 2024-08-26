from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_FIELD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ADD_TO_CART = (By.CSS_SELECTOR, 'div.alertinner > strong')
    BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRICE_IN_CART = (By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs')
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    MESSAGE_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
    ITEM_LIST = (By.CSS_SELECTOR, '.basket-items')
