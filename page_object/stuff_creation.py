from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class STUFF:

    def __init__(self):
        self._baseurl = 'http://192.168.1.35:8081/administration'
        self._user = 'user'
        self._password = 'bitnami'

    def _authorize_meth(self, browser):
        browser.get(self.baseurl)
        username_field = browser.find_element(By.XPATH, '//*[@id="input-username"]')
        username_field.clear()
        username_field.send_keys('user')
        password_field = browser.find_element(By.XPATH, '//*[@id="input-password"]')
        password_field.clear()
        password_field.send_keys('bitnami')
        browser.find_element(By.XPATH, '//*[@id="form-login"]/div[3]/button').click()
        browser.implicitly_wait(5)

    def create_stuff(self, browser, model_name_long: str, model_name_short: str, description: str, path: str,
                     section: str, model_id: str):
        self._authorize_meth(browser)
        browser.find_element(By.XPATH, '//*[@id="menu-catalog"]/a').click()
        browser.find_element(By.XPATH, '//*[@id="collapse-1"]/li[2]/a').click()
        browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div/a').click()
        browser.find_element(By.XPATH, '//*[@id="input-name-1"]').send_keys(model_name_long)
        iframe = browser.find_element(By.XPATH, '//*[@id="cke_1_contents"]/iframe')
        browser.switch_to.frame(iframe)
        browser.find_element(By.XPATH, '/html/body/p').send_keys(description)
        browser.switch_to.default_content()
        browser.find_element(By.XPATH, '//*[@id="input-meta-title-1"]').send_keys(section)
        browser.find_element(By.XPATH, '//*[@id="form-product"]/ul/li[2]/a').click()
        browser.find_element(By.XPATH, '//*[@id="input-model"]').send_keys(model_name_short)
        browser.find_element(By.XPATH, '//*[@id="form-product"]/ul/li[9]/a').click()
        browser.find_element(By.XPATH, '//*[@id="image"]/div/button[1]').click()
        WebDriverWait(browser, 30).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="button-upload"]')))
        browser.find_element(By.XPATH, '//*[@id="button-upload"]').send_keys(path)
        browser.find_element(By.XPATH, '//*[@id="filemanager"]/div/div[2]/div[3]/div[4]/div[1]/a/img').click()
        browser.find_element(By.XPATH, '//*[@id="form-product"]/ul/li[11]/a').click()
        browser.find_element(By.XPATH, '//*[@id="input-keyword-0-1"]').send_keys(model_id)
        browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div/button').click()

    @property
    def baseurl(self):
        return self._baseurl

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password
