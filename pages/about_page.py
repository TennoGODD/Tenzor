import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class AboutPage(BasePage):

    PAGE_URL = Links.ABOUT

    IMAGES_FIELD = ("xpath", "(//div[@class='s-Grid-container'])[3]")
    IMAGES = ("css selector", "img.tensor_ru-About__block3-image")

    @allure.step("Scroll to images")
    def scroll_to_images(self):
        block_element = self.wait.until(
            EC.presence_of_element_located(self.IMAGES_FIELD)
        )
        self.scroll_to_element(block_element)

    @allure.step("Check all images have same size")
    def size_images(self):
        with allure.step("Find and verify images dimensions"):
            images_element = self.wait.until(
                EC.presence_of_all_elements_located(self.IMAGES)
            )

            target_images = images_element[:4]
            self.wait.until(
                lambda driver: all(img.get_attribute("complete") for img in target_images)
            )
            first_size = target_images[0].size
            first_width, first_height = first_size['width'], first_size['height']
            all_sizes_match = True

            for i, img in enumerate(target_images, 1):
                current_size = img.size
                current_width, current_height = current_size['width'], current_size['height']

                status = "СОВПАДАЕТ" if current_size == first_size else "ОТЛИЧАЕТСЯ"

                print(f"Изображение {i}:")
                print(f"Ширина: {current_width}px")
                print(f"Высота: {current_height}px")

                if current_size != first_size:
                    all_sizes_match = False
                    print(f"Расхождение!")
            if all_sizes_match:
                print(f"Размеры всех изображений: {first_width} x {first_height} пикселей")
            else:
                print("Обнаружены изображения с разными размерами!")

            assert all_sizes_match, "Не все изображения имеют одинаковые размеры"

            return first_size