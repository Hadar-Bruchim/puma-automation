from pages.account_settings_page import AccountSettingsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.item_page import ItemPage
from pages.products_page import ProductsPage
from pages.login_page import LoginPage

from pages.wishlist_page import WishlistPage



class BaseTest:
    products_page: ProductsPage
    login_page: LoginPage
    forgot_password_page: ForgotPasswordPage
    wishlist_page: WishlistPage
    item_page = ItemPage
    cart_page = CartPage
    checkout_page = CheckoutPage
    account_settings_page = AccountSettingsPage

