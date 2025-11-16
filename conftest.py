import pytest
import os
from selenium import webdriver
from selenium.webdriver.edge.options import Options


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)
    print(f"Download directory: {download_dir}")

    edge_options = Options()

    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False,
        "profile.default_content_settings.popups": 0,
        "profile.content_settings.exceptions.automatic_downloads.*.setting": 1,
    }
    edge_options.add_experimental_option("prefs", prefs)

    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    edge_options.add_argument("--window-size=1920,1080")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--allow-running-insecure-content")
    edge_options.add_argument("--disable-web-security")
    edge_options.add_argument("--disable-features=DownloadBubble")

    edge_options.use_chromium = True
    edge_options.set_capability("ms:inPrivate", True)

    driver = webdriver.Edge(options=edge_options)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.quit()