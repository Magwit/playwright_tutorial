import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.get_by_text("Shop Women", exact=True).click()
    # Alternative by index
    # page.get_by_text("Shop Women").nth(0)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)