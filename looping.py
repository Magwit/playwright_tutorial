from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    #page.pause()
    page.wait_for_load_state("networkidle")
    page.get_by_role("link", name="Shop Women", exact=True).click()
    # page.wait_for_load_state("networkidle")
    all_links = page.get_by_role("link").all()
    for link in all_links:
        if "$85" in link.text_content():
            print("match!")
            assert 'socks' not in link.text_content().lower()


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)