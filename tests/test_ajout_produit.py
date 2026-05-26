import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage                
base_url = "https://www.saucedemo.com/"

def test_example(page):  
    products_page = ProductsPage(page) 
    login_page = LoginPage(page)                             
    #page.goto(base_url)
       
    login_page.username("standard_user")
    login_page.password("secret_sauce")
    login_page.login()     
    products_page.add_to_cart()
    products_page.go_to_cart()
    expect(page.locator("[data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Backpack")
    expect(page.locator("[data-test=\"inventory-item-price\"]")).to_contain_text("$29.99")
    products_page.checkout()
    products_page.fill_checkout_information("test", "test2", "6060")
    products_page.continue_checkout()
    expect(page.locator("[data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Backpack")
    expect(page.locator("[data-test=\"total-label\"]")).to_contain_text("Total: $32.39")
    expect(page.locator("[data-test=\"finish\"]")).to_contain_text("Finish")
    products_page.finish_checkout()
    expect(page.locator("[data-test=\"complete-header\"]")).to_contain_text("Thank you for your order!")
