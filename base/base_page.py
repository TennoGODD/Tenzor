import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10,poll_frequency=1)

    def hover_element(self, element):
        with allure.step(f"Hover over element"):
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    def is_open(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_contains(self.PAGE_URL))

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body = self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG,
        )

    def scroll_to_element(self, element):
        with allure.step("Scroll to element"):
            self.driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});",
                element
            )
