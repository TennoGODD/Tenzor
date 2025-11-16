import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class SabyPage(BasePage):

    PAGE_URL = Links.SABY

    CONTACTS_FIELD = ("xpath", "//span[text()='Контакты']")
    SHOW_MORE_CONTACTS_FIELD = ("xpath", "//span[text()='Еще 13 офисов в регионе']")
    DOWNLOAD_LINK = ("xpath", "//a[text()='Скачать локальные версии']")

    @allure.step("Hover over contacts menu")
    def hover_contacts(self):
        contacts_element = self.wait.until(
            EC.presence_of_element_located(self.CONTACTS_FIELD)
        )
        self.hover_element(contacts_element)

    @allure.step("Click 'Еще 13 офисов в регионе' button")
    def click_show_more_contacts(self):
        more_element = self.wait.until(
            EC.element_to_be_clickable(self.SHOW_MORE_CONTACTS_FIELD)
        )
        more_element.click()

    @allure.step("Click 'Скачать локальные версии' link")
    def click_download_link(self):
        download_link = self.wait.until(
            EC.element_to_be_clickable(self.DOWNLOAD_LINK)
        )
        download_link.click()