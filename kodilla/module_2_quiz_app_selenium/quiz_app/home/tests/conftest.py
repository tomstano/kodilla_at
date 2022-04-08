import pytest
from pyvirtualdisplay import Display
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    options = ChromeOptions()
    # options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    dj_display = Display(backend="xvfb")
    dj_display.start()
    chrome = Chrome(service=service, chrome_options=options)
    chrome.implicitly_wait(3)
    chrome.maximize_window()
    chrome.get("http://127.0.0.1:8001/")
    yield chrome
    chrome.quit()
    dj_display.stop()
