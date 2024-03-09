from selenium.webdriver.common.by import By
import random
import string


class UserCreation:

    def _gen_user(self):
        return {
            "first_name": ''.join(random.choices(string.ascii_lowercase, k=6)),
            "last_name": ''.join(random.choices(string.ascii_lowercase, k=6)),
            "email": ''.join(random.choices(string.ascii_lowercase, k=5)) + '@' +
                     ''.join(random.choices(string.ascii_lowercase, k=4)) + '.ru',
            "password": ''.join(random.choices(string.ascii_lowercase, k=8))
        }

    def create_user(self, browser):
        user = self._gen_user()
        browser.get(browser.base_url + "/index.php?route=account/register")
        browser.find_element(By.XPATH, '//*[@id="input-firstname"]').send_keys(user['first_name'])
        browser.find_element(By.XPATH, '//*[@id="input-lastname"]').send_keys(user['last_name'])
        browser.find_element(By.XPATH, '//*[@id="input-email"]').send_keys(user['email'])
        browser.find_element(By.XPATH, '//*[@id="input-password"]').send_keys(user['password'])
        browser.find_element(By.XPATH, '//*[@id="form-register"]/div/div/input').click()
        browser.find_element(By.XPATH, '//*[@id="form-register"]/div/button').click()
        browser.implicitly_wait(1)
