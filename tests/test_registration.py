from selenium.webdriver.common.by import By
from page_object.user_creation import UserCreation


def test_registration(slow_down_tests, browser):
    UserCreation().create_user(browser)
    assert browser.find_element(By.XPATH, '//*[@id="content"]/h1').text == 'Your Account Has Been Created!'
