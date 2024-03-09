from selenium.webdriver.common.by import By
from page_object.stuff_creation import STUFF
from page_object.checkup_stuff_delete import CheckUpDelete
import os
import time


def test_stuff_delete(slow_down_tests, browser):
    STUFF().create_stuff(browser, 'Смартфон Apple iPhone 13 128Gb Сияющая звезда',
                       'iPhone 13',
                       'Передовые камеры для отличных фотографий. Мощное обновление для отличных фото и видео. Широкоугольная камера, улавливающая больше света. Оптическая стабилизация изображения сдвигом матрицы. И ещё больше деталей в тёмных областях кадра при съёмке на сверхширокоугольную камеру.',
                       os.getcwd() + '/pics/Figure2.png', 'Phones & PDAs', 'iPhone_13')
    CheckUpDelete().check_up_delete(browser, 'iPhone 13')
    time.sleep(1)
    assert browser.find_element(By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr/td').text == 'No results!'