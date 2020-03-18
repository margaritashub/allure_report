
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Please choose localization language')
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser').lower()
    user_language = request.config.getoption("language")
    if browser_name == 'chrome':
        print("\nstart browser chrome for test...")
        chrome_options = webdriver.ChromeOptions()
        locale = request.config.getoption('language')
        chrome_options.add_argument(f"--lang={locale}")
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': locale})
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == 'firefox':
        print("\nstart browser firefox for test...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name should be Chrome or Firefox')

    yield browser

    browser.quit()
