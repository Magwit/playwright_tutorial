from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.get_by_role("button", name="Log In").wait_for()
    expect(page.get_by_role("button", name="Log In")).to_be_visible()



    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)