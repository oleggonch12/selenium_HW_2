from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_stuff(browser):
    browser.get('http://192.168.1.35:8081/administration')
    username_field = browser.find_element(By.XPATH, '//*[@id="input-username"]')
    username_field.clear()
    username_field.send_keys('user')
    password_field = browser.find_element(By.XPATH, '//*[@id="input-password"]')
    password_field.clear()
    password_field.send_keys('bitnami')
    browser.find_element(By.XPATH, '//*[@id="form-login"]/div[3]/button').click()
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH, '//*[@id="menu-catalog"]/a').click()
    browser.find_element(By.XPATH, '//*[@id="collapse-1"]/li[2]/a').click()
    browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div/a').click()
    browser.find_element(By.XPATH, '//*[@id="input-name-1"]').send_keys('Смартфон Apple iPhone 13 128Gb Сияющая звезда')
    iframe = browser.find_element(By.XPATH, '//*[@id="cke_1_contents"]/iframe')
    browser.switch_to.frame(iframe)
    browser.find_element(By.XPATH, '/html/body/p').send_keys(
        'Передовые камеры для отличных фотографий. Мощное обновление для отличных фото и видео. Широкоугольная камера, улавливающая больше света. Оптическая стабилизация изображения сдвигом матрицы. И ещё больше деталей в тёмных областях кадра при съёмке на сверхширокоугольную камеру.')
    browser.switch_to.default_content()
    browser.find_element(By.XPATH, '//*[@id="input-meta-title-1"]').send_keys('Phones & PDAs')
    browser.find_element(By.XPATH, '//*[@id="form-product"]/ul/li[2]/a').click()
    browser.find_element(By.XPATH, '//*[@id="input-model"]').send_keys('iPhone 13')
    browser.find_element(By.XPATH, '//*[@id="form-product"]/ul/li[9]/a').click()
    browser.find_element(By.XPATH, '//*[@id="image"]/div/button[1]').click()
    WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="button-upload"]')))
    browser.find_element(By.XPATH, '//*[@id="button-upload"]').send_keys(os.getcwd() + '/pics/Figure2.png')
    browser.find_element(By.XPATH, '//*[@id="filemanager"]/div/div[2]/div[3]/div[4]/div[1]/a/img').click()
    browser.find_element(By.XPATH, '//*[@id="form-product"]/ul/li[11]/a').click()
    browser.find_element(By.XPATH, '//*[@id="input-keyword-0-1"]').send_keys('iPhone_13')
    browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div/button').click()


def test_stuff_add(slow_down_tests, browser):
    create_stuff(browser)
    browser.find_element(By.XPATH, '//*[@id="collapse-1"]/li[2]/a').click()
    browser.find_element(By.XPATH, '//*[@id="input-model"]').send_keys('iPhone 13')
    WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="button-filter"]')))
    browser.find_element(By.XPATH, '//*[@id="button-filter"]').click()
    browser.find_element(By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr/td[1]/input').click()
    browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div/button[3]').click()
    WebDriverWait(browser, 3).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert.accept()
    assert browser.find_element(By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr/td').text == 'No results!'