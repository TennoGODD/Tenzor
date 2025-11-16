import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ContactsPage(BasePage):

    PAGE_URL = Links.CONTACTS

    TENZOR_FIELD = ("xpath", "(//a[@href='https://tensor.ru/'])[1]")
    REGION_DISPLAY = ("xpath", "(//span[contains(@class, 'sbis_ru-Region-Chooser__text')])[1]")
    PARTNERS_LIST = ("css selector", "[data-qa='item']")
    KAMCHATKA_REGION = ("xpath", "//span[@title='Камчатский край']")

    @allure.step("Click on Tensor banner and switch to new tab")
    def click_tensor(self):
        tensor_field = self.wait.until(
            EC.element_to_be_clickable(self.TENZOR_FIELD)
        )
        tensor_field.click()
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_current_region(self):
        region_element = self.wait.until(
            EC.visibility_of_element_located(self.REGION_DISPLAY)
        )
        region_name = region_element.text.strip()
        return region_name

    @allure.step("Verify region is {expected_region}")
    def verify_region(self, expected_region):
        current_region = self.get_current_region()
        assert expected_region.lower() in current_region.lower(), (
            f"Регион не соответствует ожидаемому. "
            f"Ожидался: {expected_region}, Текущий: {current_region}"
        )
        print(f"Регион корректный: {current_region}")
        return True

    def check_partners_list(self):
        partners = self.wait.until(
            EC.presence_of_all_elements_located(self.PARTNERS_LIST)
        )
        assert len(partners) > 0, "Список партнеров пуст"
        return partners

    @allure.step("Verify partners list changed")
    def verify_partners_list_changed(self, original_partners_count):
        new_partners = self.check_partners_list()
        new_count = len(new_partners)

        assert new_count != original_partners_count, (
            f"Список партнеров не изменился. "
            f"Было: {original_partners_count}, стало: {new_count}"
        )
        print(f"Список партнеров изменился. Было: {original_partners_count}, стало: {new_count}")
        return new_partners

    @allure.step("Change region to Kamchatka")
    def change_region_to_kamchatka(self):
        with allure.step("Click current region to open region list"):
            region_selector = self.wait.until(
                EC.element_to_be_clickable(self.REGION_DISPLAY)
            )
            region_selector.click()

        with allure.step("Select Kamchatka region from list"):
            kamchatka_element = self.wait.until(
                EC.element_to_be_clickable(self.KAMCHATKA_REGION)
            )
            self.driver.execute_script("arguments[0].click();", kamchatka_element)

        with allure.step("Wait for region change to complete"):
            self.wait.until(
                lambda driver: "камчат" in self.get_current_region().lower()
            )

    @allure.step("Verify URL matches Kamchatka pattern")
    def verify_url_kamchatka(self):
        current_url = self.driver.current_url
        expected_pattern = "41-kamchatskij-kraj"
        assert expected_pattern in current_url, (
            f"URL не соответствует Камчатскому краю. "
        )
        print(f"URL соответствует Камчатскому краю: {current_url}")
        return True