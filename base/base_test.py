import pytest

from pages.saby_page import SabyPage
from pages.contacts_page import ContactsPage
from pages.tensor_page import TensorPage
from pages.about_page import AboutPage
from pages.download_page import DownloadPage


class BaseTest:

    saby_page: SabyPage
    contacts_page: ContactsPage
    tensor_page: TensorPage
    about_page: AboutPage
    download_page: DownloadPage


    @pytest.fixture(autouse=True)
    def setup(self,request,driver):
        request.cls.driver = driver
        request.cls.saby_page = SabyPage(driver)
        request.cls.contacts_page = ContactsPage(driver)
        request.cls.tensor_page = TensorPage(driver)
        request.cls.about_page = AboutPage(driver)
        request.cls.download_page = DownloadPage(driver)
