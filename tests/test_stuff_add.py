from selenium.webdriver.common.by import By
from page_object.stuff_creation import STUFF
from page_object.checkup_stuff_creation import CheckUpCreation
import os
import time


def test_stuff_add(slow_down_tests, browser):
    STUFF().create_stuff(browser, 'Смартфон TECNO CAMON',
                         '20 Pro',
                         'TECNO CAMON 20 Pro — универсальный смартфон, сочетающий в себе запоминающийся дизайн, выдающуюся производительность, четкие камеры и большой безрамочный дисплей. Благодаря специальному режиму пользователь может записывать видео одновременно с двух камер: основной и фронтальной.',
                         os.getcwd() + '/pics/Figure1.png', 'Phones & PDAs', 'TECNO_CAMON_20_Pro')
    CheckUpCreation().check_up_creation(browser, '20 Pro')
    time.sleep(3)
    assert (browser.find_element(By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr/td[3]').text ==
            'Смартфон TECNO CAMON\nEnabled')
