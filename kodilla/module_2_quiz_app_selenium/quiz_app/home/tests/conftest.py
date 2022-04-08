import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    options = Options()
    # options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    chrome = Chrome(service=service, chrome_options=options)
    chrome.implicitly_wait(3)
    chrome.maximize_window()
    chrome.get("http://127.0.0.1:8001/")
    yield chrome
    chrome.quit()
