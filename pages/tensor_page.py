import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class TensorPage(BasePage):
    PAGE_URL = Links.TENSOR

    BLOCK_FIELD = ("xpath", "//div[@class='tensor_ru-Index__block4-bg']")
    MORE_DETAILS_FIELD = ("xpath", "//a[@href='/about' and text()='Подробнее']")

    @allure.step("Check Tensor page is opened")
    def is_open(self):
        with allure.step("Tensor page is opened"):
            self.wait.until(EC.url_contains(Links.TENSOR))

    @allure.step("Scroll to 'Сила в людях' block")
    def scroll_to_people_block(self):
        block_element = self.wait.until(
            EC.presence_of_element_located(self.BLOCK_FIELD)
        )
        self.scroll_to_element(block_element)

    @allure.step("Click 'Подробнее' link")
    def click_more_details(self):
        details_link = self.wait.until(
            EC.element_to_be_clickable(self.MORE_DETAILS_FIELD)
        )
        details_link.click()
