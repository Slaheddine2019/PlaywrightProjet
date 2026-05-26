import csv
import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def data_csv():
    data = []
    with open("./data/userdata.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            # on attend: username, password, success
            data.append((row[0], row[1], row[2] == "True"))

    return data


@pytest.mark.order(2)
@pytest.mark.parametrize(
    "username,password,success",
    data_csv(),
)
def test_login_success(page: Page, username: str, password: str, success: bool):

    login_page = LoginPage(page)

    page.goto("https://www.saucedemo.com/")

    login_page.username(username)
    login_page.password(password)
    login_page.login()

    if success:

        expect(login_page.title_locator).to_contain_text("Swag Labs")
    else:
        expect(login_page.error_message_locator).to_contain_text(
            "Epic sadface: Username and password do not match any user in this service"
        )


@pytest.mark.order(1)
@pytest.mark.skip(reason="Ce test est obsolète, remplacé par test_login_success")
def test_login_failure(page: Page):

    login_page = LoginPage(page)

    page.goto("https://www.saucedemo.com/")

    login_page.username("standard_user123")
    login_page.password("secret_sauce123")
    login_page.login()

    expect(login_page.error_message_locator).to_contain_text(
        "Epic sadface: Username and password do not match any user in this service"
    )
