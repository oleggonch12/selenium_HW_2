from selenium.webdriver.common.by import By


class PoundSetUp:

    def setup_pound(self, browser):
        text_element_pound = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div/div/span[1]').text
        browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/span').click()
        browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[3]/a').click()
        return text_element_pound
