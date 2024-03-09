from selenium.webdriver.common.by import By


def test_currency_set_up(slow_down_tests, browser):
    currency_button = browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/span')
    currency_button.click()
    browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a').click()
    element_euro = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div/div/span[1]')
    text_element_euro = element_euro.text
    currency_button = browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/span')
    currency_button.click()
    browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[2]/a').click()
    element_pounds = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div/div/span[1]')
    text_element_pounds = element_pounds.text
    currency_button = browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/span')
    currency_button.click()
    browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[3]/a').click()
    element_dollars = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div/div/span[1]')
    text_element_dollars = element_dollars.text

    assert (text_element_euro.endswith('€') and text_element_pounds.startswith('£') and
            text_element_dollars.startswith('$')), 'Неправильно выставляются валюты'