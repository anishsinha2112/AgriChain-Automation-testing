from selenium.webdriver.common.by import By

class ResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.output_text = (By.ID, "output-text")   # Assuming ID locator

    def get_result(self):
        return self.driver.find_element(*self.output_text).text
