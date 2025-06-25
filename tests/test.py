import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FractalArtWebsiteTests(unittest.TestCase):
    """Class for Fractal Art Website Tests."""

    @classmethod
    def setUpClass(cls):
        """Method that prepares the driver for testing"""
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://patrickschroeder98.github.io/fractal_art_website/index.html"
        cls.driver.get(cls.base_url)

    def setUp(self):
        """Method that runs before each test."""
        self.driver.get(self.base_url)
        self.driver.find_element(By.CSS_SELECTOR, "a[data-lang='en']").click()

    def test_title(self):
        """Method that checks if the title is displayed correctly."""
        title = self.driver.title
        self.assertEqual("Fractal Art Website", title)

    def test_religiosity(self):
        """Method that checks if the religiosity title is displayed correctly."""
        self.driver.find_element(By.CSS_SELECTOR, "h2[data-i18n='rel-title'] + a").click()
        title = self.driver.title
        self.assertEqual("Religiosity - Fractal Art", title)

    def test_inspiration(self):
        """Method that checks if the inspiration title is displayed correctly."""
        self.driver.find_element(By.CSS_SELECTOR, "h2[data-i18n='ins-title'] + a").click()
        title = self.driver.title
        self.assertEqual("Inspiration - Fractal Art", title)

    def test_spring_flowers(self):
        """Method that checks if the spring flowers title is displayed correctly."""
        self.driver.find_element(By.CSS_SELECTOR, "h2[data-i18n='sfd-title'] + a").click()
        title = self.driver.title
        self.assertEqual("Spring Flowers Draft - Fractal Art", title)

    def test_julia_set(self):
        """Method that checks if the julia set drafts title is displayed correctly."""
        self.driver.find_element(By.CSS_SELECTOR, "h2[data-i18n='jsd-title'] + a").click()
        title = self.driver.title
        self.assertEqual("Julia Set Drafts - Fractal Art", title)

    def test_mandelbrot_set(self):
        """Method that checks if the mandelbrot set drafts title is displayed correctly."""
        self.driver.find_element(By.CSS_SELECTOR, "h2[data-i18n='msd-title'] + a").click()
        title = self.driver.title
        self.assertEqual("Mandelbrot Set Drafts - Fractal Art", title)

    def test_about(self):
        """Method that checks if the about page title is displayed correctly."""
        self.driver.find_element(By.CSS_SELECTOR, "a[data-i18n='nav-about']").click()
        title = self.driver.title
        self.assertEqual("About me - Fractal Art Website", title)

    def test_home_nav(self):
        """Method that checks if the home navigation button works correctly."""
        self.driver.find_element(By.CSS_SELECTOR, "a[data-i18n='nav-about']").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[data-i18n='nav-home']").click()
        title = self.driver.title
        self.assertEqual("Fractal Art Website", title)
        self.driver.find_element(By.CSS_SELECTOR, "a[data-i18n='nav-home']").click()
        title = self.driver.title
        self.assertEqual("Fractal Art Website", title)

    def test_pl(self):
        """Method that checks if the Polish translation button works correctly."""
        self.driver.find_element(By.CSS_SELECTOR, "a[data-lang='pl']").click()
        title = self.driver.title
        self.assertEqual("Fraktalna Sztuka", title)
        text = self.driver.find_element(By.CSS_SELECTOR, "h1[data-i18n='hero-title']")
        self.assertEqual("Witamy na Stronie o Fraktalnej Sztuce", text.text)

    def test_de(self):
        """Method that checks if the German translation button works correctly."""
        self.driver.find_element(By.CSS_SELECTOR, "a[data-lang='de']").click()
        title = self.driver.title
        self.assertEqual("Fraktal-Kunst-Website", title)
        text = self.driver.find_element(By.CSS_SELECTOR, "h1[data-i18n='hero-title']")
        self.assertEqual("Willkommen auf der Fraktal-Kunst-Website", text.text)

    def test_img_mainpage_rel(self):
        """Method that checks if image on the main page has correct attributes."""
        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/religiosity.jpg']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Religiosity")

    def test_img_mainpage_ins(self):
        """Method that checks if image on the main page has correct attributes."""
        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/inspiration.jpg']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Inspiration")

    def test_img_mainpage_sfd(self):
        """Method that checks if image on the main page has correct attributes."""
        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/flowers.jpg']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Spring Flowers Draft")

    def test_img_mainpage_jsd(self):
        """Method that checks if image on the main page has correct attributes."""
        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/set9.png']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Julia Set")

    def test_img_mainpage_msd(self):
        """Method that checks if image on the main page has correct attributes."""
        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/set3.png']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Mandelbrot Set")

    def test_img_about(self):
        """Method that checks if image on the 'about' page has correct attributes."""
        self.driver.find_element(By.CSS_SELECTOR, "a[data-i18n='nav-about']").click()
        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/sesja3153.jpg']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Artist Photo")


    def test_img_religiosity(self):
        """Method that checks if image on the religiosity page has correct attributes."""
        self.driver.find_element(By.CSS_SELECTOR, "h2[data-i18n='rel-title'] + a").click()
        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/religiosity.jpg']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Religiosity Painting")

    def test_img_inspiration(self):
        """Method that checks if image on the inspiration page has correct attributes."""
        self.driver.find_element(By.CSS_SELECTOR, "h2[data-i18n='ins-title'] + a").click()
        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/inspiration.jpg']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Inspiration Painting")

    def test_img_flowers(self):
        """Method that checks if image on the spring flowers page has correct attributes."""
        self.driver.find_element(By.CSS_SELECTOR, "h2[data-i18n='sfd-title'] + a").click()
        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/flowers.jpg']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Spring Flowers Draft")

    def test_img_jsd(self):
        """Method that checks if images on the julia set page have correct attributes."""
        self.driver.find_element(By.CSS_SELECTOR, "h2[data-i18n='jsd-title'] + a").click()

        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/set9.png']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Draft - White On Black")

        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/set9a.png']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Draft - Red On White")

        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/set2.png']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Close-Up - Black On White")

        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/set888.png']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Close-Up - Red On Yellow")

    def test_img_msd(self):
        """Method that checks if images on the mandelbrot set page have correct attributes."""
        self.driver.find_element(By.CSS_SELECTOR, "h2[data-i18n='msd-title'] + a").click()

        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/set3.png']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Draft - Black On White")

        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/2407_3.png']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Close-Up - White On Black")

        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/hsv9a.png']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Close-Up - Black on Blue-Red")

        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/hsv_rotated_spiral_zoom2.png']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Close-Up - Black on Blue-Purple")

        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/hsv_rotated_spiral_zoom3.png']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Close-Up - Black on Green Spectrum")

        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/hsv4.png']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Close-Up - Red on Green-Blue Spectrum")

        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/hsv_rotated_spiral_zoom4.png']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Close-Up - Black on Blue")

        img = self.driver.find_element(By.CSS_SELECTOR, "img[src='./assets/img/hsv_rotated_spiral_zoom5.png']")
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Close-Up - Black on Pink-Purple Spectrum")

    @classmethod
    def tearDownClass(cls):
        """Method that runs after testing."""
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
