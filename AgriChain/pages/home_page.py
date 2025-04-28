from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.input_box = (By.ID, "input-string")    # Assuming ID locator
        self.submit_button = (By.ID, "submit-btn")

    def enter_string(self, text):
        self.driver.find_element(*self.input_box).clear()
        self.driver.find_element(*self.input_box).send_keys(text)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()
