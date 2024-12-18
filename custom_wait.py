from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    login_issue = True
    while login_issue:
        if not page.is_visible(("[data-testid=\"signUp.switchToSignUp\"]")):
            page.get_by_role("button", name="Log In").click()
        else:
            login_issue = False
        time.sleep(0.1)
    
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill(
        "bob.dobbs@fakemail.com"
    )
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("byxa111")
    page.get_by_label("Password").press("Enter")
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Log In")).to_be_hidden(timeout=6666)


   



    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)