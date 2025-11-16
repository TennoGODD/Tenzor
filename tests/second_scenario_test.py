import allure
import pytest
from time import sleep
from base.base_test import BaseTest

@allure.feature("Profile Functionality")
class TestSecondScenario(BaseTest):

    @allure.title("Test region change to Kamchatka")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_region(self):
        self.saby_page.open()
        self.saby_page.hover_contacts()
        self.saby_page.click_show_more_contacts()
        self.contacts_page.is_open()
        self.contacts_page.verify_region("Ярославская")
        self.contacts_page.make_screenshot("The Yaroslavl Region page")
        original_count = len(self.contacts_page.check_partners_list())
        self.contacts_page.check_partners_list()
        self.contacts_page.change_region_to_kamchatka()
        self.contacts_page.verify_region("Камчатский")
        self.contacts_page.make_screenshot("The Kamchatka page")
        self.contacts_page.verify_url_kamchatka()
        self.contacts_page.verify_partners_list_changed(original_count)
