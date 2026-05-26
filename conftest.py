import pytest
from playwright.sync_api import Page, sync_playwright


@pytest.fixture(scope="session")
def browser():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        yield browser

        browser.close()


@pytest.fixture
def page(browser):

    context = browser.new_context()

    # START TRACE
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()

    yield page

    # STOP TRACE
    context.tracing.stop(path="test-results/trace.zip")

    context.close()


@pytest.fixture(autouse=True)
def go_to_base_url(page):
    base_url = "https://www.saucedemo.com/"
    page.goto(base_url)
