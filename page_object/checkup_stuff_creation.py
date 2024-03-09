from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class CheckUpCreation:

    def __init__(self):
        self.form_creation = By.XPATH, '//*[@id="collapse-1"]/li[2]/a'
        self.form_model = By.XPATH, '//*[@id="input-model"]'

    def check_up_creation(self, browser, model: str):
        browser.find_element(*self.form_creation).click()
        browser.find_element(*self.form_model).send_keys(model)
        WebDriverWait(browser, 30).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                        '//*[@id="button-filter"]')))
        browser.find_element(By.XPATH, '//*[@id="button-filter"]').click()
