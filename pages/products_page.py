from playwright.sync_api import Page                    


class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_button = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.shopping_cart_link = page.locator("[data-test=\"shopping-cart-link\"]")
        self.checkout_button = page.locator("[data-test=\"checkout\"]")
        self.first_name_input = page.locator("[data-test=\"firstName\"]")
        self.last_name_input = page.locator("[data-test=\"lastName\"]")
        self.postal_code_input = page.locator("[data-test=\"postalCode\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")
        self.total_label_locator = page.locator("[data-test=\"total-label\"]")
        self.finish_button = page.locator("[data-test=\"finish\"]")
        self.complete_header_locator = page.locator("[data-test=\"complete-header\"]")

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def go_to_cart(self):
        self.shopping_cart_link.click()

    def checkout(self):
        self.checkout_button.click()

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()  
            