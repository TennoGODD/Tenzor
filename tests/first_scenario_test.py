import allure
import pytest
from time import sleep
from base.base_test import BaseTest

@allure.feature("Profile Functionality")
class TestFirstScenario(BaseTest):

    @allure.title("Test images have same size")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_images_same_size(self):
        self.saby_page.open()
        self.saby_page.hover_contacts()
        self.saby_page.click_show_more_contacts()
        self.contacts_page.is_open()
        self.contacts_page.click_tensor()
        self.tensor_page.is_open()
        self.tensor_page.scroll_to_people_block()
        sleep(1)
        self.tensor_page.make_screenshot("Block 'Сила в людях'")
        self.tensor_page.click_more_details()
        self.about_page.is_open()
        self.about_page.scroll_to_images()
        sleep(1)
        self.about_page.make_screenshot("Block 'Работаем'")
        self.about_page.size_images()