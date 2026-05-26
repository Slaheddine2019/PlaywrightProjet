from playwright.sync_api import Page    
import pytest
import re

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("[data-test=\"username\"]")
        
        
        self.password_input = page.locator("[data-test=\"password\"]")
        #self.password_input = page.get_by_name("password")
        self.login_button = page.get_by_role("iinput_error form_input error" , name="password ")
        self.login_button = page.get_by_role("button", name="Login")
        self.title_locator = page.locator("[data-test=\"primary-header\"]")
        self.error_message_locator = page.locator("[data-test=\"error\"]")
        
    def username(self, username):
        self.username_input.fill(username)

    def password(self, password):
        self.password_input.fill(password)

    def login(self):
        self.login_button.click()
