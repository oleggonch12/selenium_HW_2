import pytest
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions
import time


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--base_url", default="http://192.168.1.35:8081")

@pytest.fixture(autouse=True)
def slow_down_tests():
    yield
    time.sleep(1)

@pytest.fixture(scope='session')
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base_url")

    driver = None

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                  options=options)
        driver.get(base_url)
    elif browser_name == "ff":
        options = FFOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
        driver.get(base_url)
    elif browser_name == "ya":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        service = ChromeService(
            executable_path="/home/oleg/Загрузки/yandexdriver-24.1.1.918-linux/yandexdriver"
        )
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                  options=options)
        driver.get(base_url)

    driver.maximize_window()

    driver.base_url = base_url

    yield driver

    driver.close()
