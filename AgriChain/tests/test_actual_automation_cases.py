import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
## This is my first push
@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # or Firefox(), Edge(), etc.
    driver.maximize_window()
    yield driver
    driver.quit()

class HomePage:
    def __init__(self, browser):
        self.browser = browser

    def enter_string(self, text):
        input_field = self.browser.find_element(By.ID, "input-string")
        input_field.send_keys(text)

    def click_submit(self):
        submit_button = self.browser.find_element(By.ID, "submit-button")
        submit_button.click()

class ResultPage:
    def __init__(self, browser):
        self.browser = browser

    def get_result(self):
        result_element = self.browser.find_element(By.ID, "result")
        return result_element.text

def test_longest_substring(browser):
    browser.get("https://agrichain.com")  # Homepage URL

    home_page = HomePage(browser)
    home_page.enter_string("abcabcbb")
    home_page.click_submit()

    result_page = ResultPage(browser)
    output = result_page.get_result()

    assert output == "3", f"Expected output to be 3 but got {output}"



    
