from selenium.webdriver.common.by import By


class CurrencySetUp:

    def currency_setup(self, browser):
        browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/span').click()
        browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a').click()
