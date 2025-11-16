import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Profile Functionality")
class TestThirdScenario(BaseTest):

    @allure.title("Test the file size")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_images_same_size(self):
        self.saby_page.open()
        self.saby_page.click_download_link()
        self.download_page.is_open()
        self.download_page.click_corporate_install()
        downloaded_file, expected_size = self.download_page.click_to_download()
        actual_size = self.download_page.get_file_size_mb(downloaded_file)
        assert abs(actual_size - expected_size) < 0.1, f"File size mismatch: {actual_size} vs {expected_size}"
        print(f"Successfully downloaded: {downloaded_file}")
        print(f"Expected size: {expected_size} MB, Actual size: {actual_size} MB")