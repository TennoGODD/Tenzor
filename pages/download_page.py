import allure
import os
import time
import re
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DownloadPage(BasePage):
    PAGE_URL = Links.DOWNLOAD

    CORPORATE_INSTALL = ("xpath", "(//div[@title='Корпоративный режим установки'])[1]")
    DOWNLOAD_BUTTON = ("xpath", "//a[contains(@href, 'sabycenter-setup.msi')]")

    @allure.step("Unwrap 'Корпоративный режим установки'")
    def click_corporate_install(self):
        corporate_install = self.wait.until(
            EC.element_to_be_clickable(self.CORPORATE_INSTALL)
        )
        corporate_install.click()

    @allure.step("Get expected file size from website")
    def get_expected_file_size(self):
        download_link = self.wait.until(
            EC.presence_of_element_located(self.DOWNLOAD_BUTTON)
        )
        link_text = download_link.text

        match = re.search(r'(\d+\.\d+)\s*МБ', link_text)
        if match:
            expected_size = float(match.group(1))
            print(f"Ожидаемый размер файла с сайта: {expected_size} MB")
            return expected_size
        else:
            raise Exception(f"Не удалось взять размер файла из: {link_text}")

    @allure.step("Download file and wait for completion")
    def click_to_download(self):
        expected_size = self.get_expected_file_size()

        download_link = self.wait.until(
            EC.element_to_be_clickable(self.DOWNLOAD_BUTTON)
        )
        download_link.click()

        download_dir = os.path.join(os.getcwd(), "downloads")
        downloaded_file = self.wait_for_download_complete(download_dir)

        return downloaded_file, expected_size

    @allure.step("Wait for download to complete")
    def wait_for_download_complete(self, download_dir, timeout=60):
        end_time = time.time() + timeout
        start_time = time.time()

        while time.time() < end_time:
            try:
                files = os.listdir(download_dir)
                temp_files = [f for f in files if f.endswith('.crdownload') or f.endswith('.tmp')]

                elapsed = int(time.time() - start_time)

                if temp_files:
                    print(f"Прошло {elapsed}с. {len(temp_files)}")
                else:
                    downloaded_files = [f for f in files if
                                        not f.startswith('.') and os.path.isfile(os.path.join(download_dir, f))]
                    if downloaded_files:
                        total_time = int(time.time() - start_time)
                        print(f"Загрузка завершена за {total_time} секунд!")
                        print(f"Скачанный файл: {downloaded_files[0]}")
                        return downloaded_files[0]

                time.sleep(2)

            except Exception as e:
                print(f"Ошибка при проверке загрузки: {e}")
                time.sleep(2)

        raise Exception(f"Загрузка не завершилась за {timeout} секунд")

    @allure.step("Get downloaded file size")
    def get_file_size_mb(self, filename):
        file_path = os.path.join(os.getcwd(), "downloads", filename)
        size_bytes = os.path.getsize(file_path)
        size_mb = size_bytes / (1024 * 1024)
        print(f"Размер скачанного файла: {size_mb:.2f} MB")
        return round(size_mb, 2)