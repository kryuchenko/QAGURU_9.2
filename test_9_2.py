import pytest
import time
from selene.support.shared import browser
from selene import be, have


@pytest.fixture(scope="function")
def setup_browser():
    browser.config.window_width = 1500
    browser.config.window_height = 1000
    yield
    browser.driver.delete_all_cookies()
    browser.execute_script("localStorage.clear();")
    browser.quit()


def test_google_search(setup_browser):
    browser.open('http://google.com')
    cookie_accept_button = browser.element('.QS5gu.sy4vM')
    if cookie_accept_button.matching(be.visible):
        cookie_accept_button.click()

    search_field = browser.element('[name="q"]')
    search_field.should(be.visible).type('test')
    time.sleep(1)
    search_field.press_enter()
    search_results = browser.element('#search')
    search_results.should(have.text('test'))

def test_google_search_invalid_result(setup_browser):
    browser.open('http://google.com')
    cookie_accept_button = browser.element('.QS5gu.sy4vM')
    if cookie_accept_button.matching(be.visible):
        cookie_accept_button.click()
    search_field = browser.element('[name="q"]')
    search_field.should(be.visible).type("ывпывпывп3п3пп33п3п")
    time.sleep(1)
    search_field.press_enter()
    browser.element('//*[@id="result-stats"]').should(have.text('About 0 results'))

