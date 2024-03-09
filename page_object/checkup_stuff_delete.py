from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

class CheckUpDelete:

    def __init__(self):
        self.form_creation = By.XPATH, '//*[@id="collapse-1"]/li[2]/a'
        self.form_model = By.XPATH, '//*[@id="input-model"]'
        self.form_filter = By.XPATH, '//*[@id="button-filter"]'
        self.form_del_1 = By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr/td[1]/input'
        self.form_del_2 = By.XPATH, '//*[@id="content"]/div[1]/div/div/button[3]'
        self.form_autocomplete = By.XPATH, '//*[@id="autocomplete-model"]/li/a'

    def check_up_delete(self, browser, model: str):
        browser.find_element(*self.form_creation).click()
        browser.find_element(*self.form_model).send_keys(model)
        browser.find_element(*self.form_model).click()
        browser.find_element(*self.form_autocomplete).click()
        time.sleep(1)
        browser.find_element(*self.form_filter).click()
        time.sleep(1)
        browser.find_element(*self.form_del_1).click()
        browser.find_element(*self.form_del_2).click()
        WebDriverWait(browser, 3).until(expected_conditions.alert_is_present())
        alert = browser.switch_to.alert
        alert.accept()
