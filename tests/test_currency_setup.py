from selenium.webdriver.common.by import By
from page_object.currency_creation_setup import CurrencySetUp
from page_object.euro_setup import EuroSetUp
from page_object.pound_setup import PoundSetUp


def test_currency_set_up(slow_down_tests, browser):
    CurrencySetUp().currency_setup(browser)
    text_element_euro = EuroSetUp().setup_euro(browser)
    text_element_pounds = PoundSetUp().setup_pound(browser)
    text_element_dollars = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div/div/span[1]').text

    assert (text_element_euro.endswith('€') and text_element_pounds.startswith('£') and
            text_element_dollars.startswith('$')), 'Неправильно выставляются валюты'