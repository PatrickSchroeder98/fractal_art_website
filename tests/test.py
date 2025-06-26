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
        # cls.base_url = "https://patrickschroeder98.github.io/fractal_art_website/index.html"
        cls.base_url = "http://127.0.0.1:5500/index.html"
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
        self.driver.find_element(
            By.CSS_SELECTOR, "h2[data-i18n='rel-title'] + a"
        ).click()
        title = self.driver.title
        self.assertEqual("Religiosity - Fractal Art", title)

    def test_inspiration(self):
        """Method that checks if the inspiration title is displayed correctly."""
        self.driver.find_element(
            By.CSS_SELECTOR, "h2[data-i18n='ins-title'] + a"
        ).click()
        title = self.driver.title
        self.assertEqual("Inspiration - Fractal Art", title)

    def test_spring_flowers(self):
        """Method that checks if the spring flowers title is displayed correctly."""
        self.driver.find_element(
            By.CSS_SELECTOR, "h2[data-i18n='sfd-title'] + a"
        ).click()
        title = self.driver.title
        self.assertEqual("Spring Flowers Draft - Fractal Art", title)

    def test_julia_set(self):
        """Method that checks if the julia set drafts title is displayed correctly."""
        self.driver.find_element(
            By.CSS_SELECTOR, "h2[data-i18n='jsd-title'] + a"
        ).click()
        title = self.driver.title
        self.assertEqual("Julia Set Drafts - Fractal Art", title)

    def test_mandelbrot_set(self):
        """Method that checks if the mandelbrot set drafts title is displayed correctly."""
        self.driver.find_element(
            By.CSS_SELECTOR, "h2[data-i18n='msd-title'] + a"
        ).click()
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
        img = self.driver.find_element(
            By.CSS_SELECTOR, "img[src='./assets/img/religiosity.jpg']"
        )
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Religiosity")

    def test_img_mainpage_ins(self):
        """Method that checks if image on the main page has correct attributes."""
        img = self.driver.find_element(
            By.CSS_SELECTOR, "img[src='./assets/img/inspiration.jpg']"
        )
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Inspiration")

    def test_img_mainpage_sfd(self):
        """Method that checks if image on the main page has correct attributes."""
        img = self.driver.find_element(
            By.CSS_SELECTOR, "img[src='./assets/img/flowers.jpg']"
        )
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Spring Flowers Draft")

    def test_img_mainpage_jsd(self):
        """Method that checks if image on the main page has correct attributes."""
        img = self.driver.find_element(
            By.CSS_SELECTOR, "img[src='./assets/img/set9.png']"
        )
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Julia Set")

    def test_img_mainpage_msd(self):
        """Method that checks if image on the main page has correct attributes."""
        img = self.driver.find_element(
            By.CSS_SELECTOR, "img[src='./assets/img/set3.png']"
        )
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Mandelbrot Set")

    def test_img_about(self):
        """Method that checks if image on the 'about' page has correct attributes."""
        self.driver.find_element(By.CSS_SELECTOR, "a[data-i18n='nav-about']").click()
        img = self.driver.find_element(
            By.CSS_SELECTOR, "img[src='./assets/img/sesja3153.jpg']"
        )
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Artist Photo")

    def test_img_religiosity(self):
        """Method that checks if image on the religiosity page has correct attributes."""
        self.driver.find_element(
            By.CSS_SELECTOR, "h2[data-i18n='rel-title'] + a"
        ).click()
        img = self.driver.find_element(
            By.CSS_SELECTOR, "img[src='./assets/img/religiosity.jpg']"
        )
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Religiosity Painting")

    def test_img_inspiration(self):
        """Method that checks if image on the inspiration page has correct attributes."""
        self.driver.find_element(
            By.CSS_SELECTOR, "h2[data-i18n='ins-title'] + a"
        ).click()
        img = self.driver.find_element(
            By.CSS_SELECTOR, "img[src='./assets/img/inspiration.jpg']"
        )
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Inspiration Painting")

    def test_img_flowers(self):
        """Method that checks if image on the spring flowers page has correct attributes."""
        self.driver.find_element(
            By.CSS_SELECTOR, "h2[data-i18n='sfd-title'] + a"
        ).click()
        img = self.driver.find_element(
            By.CSS_SELECTOR, "img[src='./assets/img/flowers.jpg']"
        )
        self.assertIsNotNone(img)
        self.assertEqual(img.get_attribute("alt"), "Spring Flowers Draft")

    def test_img_jsd(self):
        """Method that checks if images on the julia set page have correct attributes."""
        self.driver.find_element(
            By.CSS_SELECTOR, "h2[data-i18n='jsd-title'] + a"
        ).click()

        def run(val, txt):
            img = self.driver.find_element(By.CSS_SELECTOR, val)
            self.assertIsNotNone(img)
            self.assertEqual(img.get_attribute("alt"), txt)

        values = [
            "img[src='./assets/img/set9.png']",
            "img[src='./assets/img/set9a.png']",
            "img[src='./assets/img/set2.png']",
            "img[src='./assets/img/set888.png']",
        ]
        texts = [
            "Draft - White On Black",
            "Draft - Red On White",
            "Close-Up - Black On White",
            "Close-Up - Red On Yellow",
        ]

        self.assertEqual(len(values), len(texts))

        for i in range(len(values)):
            run(values[i], texts[i])

    def test_img_msd(self):
        """Method that checks if images on the mandelbrot set page have correct attributes."""
        self.driver.find_element(
            By.CSS_SELECTOR, "h2[data-i18n='msd-title'] + a"
        ).click()

        def run(val, txt):
            img = self.driver.find_element(By.CSS_SELECTOR, val)
            self.assertIsNotNone(img)
            self.assertEqual(img.get_attribute("alt"), txt)

        values = [
            "img[src='./assets/img/set3.png']",
            "img[src='./assets/img/2407_3.png']",
            "img[src='./assets/img/hsv9a.png']",
            "img[src='./assets/img/hsv_rotated_spiral_zoom2.png']",
            "img[src='./assets/img/hsv_rotated_spiral_zoom3.png']",
            "img[src='./assets/img/hsv4.png']",
            "img[src='./assets/img/hsv_rotated_spiral_zoom4.png']",
            "img[src='./assets/img/hsv_rotated_spiral_zoom5.png']",
        ]
        texts = [
            "Draft - Black On White",
            "Close-Up - White On Black",
            "Close-Up - Black on Blue-Red",
            "Close-Up - Black on Blue-Purple",
            "Close-Up - Black on Green Spectrum",
            "Close-Up - Red on Green-Blue Spectrum",
            "Close-Up - Black on Blue",
            "Close-Up - Black on Pink-Purple Spectrum",
        ]

        self.assertEqual(len(values), len(texts))

        for i in range(len(values)):
            run(values[i], texts[i])

    def test_copyright(self):
        """Method that checks if the copyright text in english is displayed correctly."""
        cpright = "All rights reserved. All logos are trademarks of their respective owners and are used here for informational purposes only."

        def check():
            txt = self.driver.find_element(By.CSS_SELECTOR, "p[data-i18n='copyright']")
            self.assertIsNotNone(txt)
            self.assertTrue(cpright in txt.text)

        def run(val):
            self.setUp()
            self.driver.find_element(By.CSS_SELECTOR, val).click()
            check()

        values = [
            "a[data-i18n='nav-about']",
            "h2[data-i18n='rel-title'] + a",
            "h2[data-i18n='ins-title'] + a",
            "h2[data-i18n='sfd-title'] + a",
            "h2[data-i18n='jsd-title'] + a",
            "h2[data-i18n='msd-title'] + a",
        ]

        check()
        for val in values:
            run(val)

    def test_copyright_pl(self):
        """Method that checks if the copyright text in polish is displayed correctly."""
        cpright = "Wszelkie prawa zastrzeżone. Wszystkie loga są znakami towarowymi ich właścicieli i są używane tutaj wyłącznie w celach informacyjnych."

        def check():
            txt = self.driver.find_element(By.CSS_SELECTOR, "p[data-i18n='copyright']")
            self.assertIsNotNone(txt)
            self.assertTrue(cpright in txt.text)

        def run(val):
            self.setUp()
            self.driver.find_element(By.CSS_SELECTOR, "a[data-lang='pl']").click()
            self.driver.find_element(By.CSS_SELECTOR, val).click()
            check()

        values = [
            "a[data-i18n='nav-about']",
            "h2[data-i18n='rel-title'] + a",
            "h2[data-i18n='ins-title'] + a",
            "h2[data-i18n='sfd-title'] + a",
            "h2[data-i18n='jsd-title'] + a",
            "h2[data-i18n='msd-title'] + a",
        ]

        self.driver.find_element(By.CSS_SELECTOR, "a[data-lang='pl']").click()
        check()
        for val in values:
            run(val)

    def test_copyright_de(self):
        """Method that checks if the copyright text in german is displayed correctly."""
        cpright = "Alle Rechte vorbehalten. Alle Logos sind Marken ihrer jeweiligen Besitzer und werden hier nur zu Informationszwecken verwendet."

        def check():
            txt = self.driver.find_element(By.CSS_SELECTOR, "p[data-i18n='copyright']")
            self.assertIsNotNone(txt)
            self.assertTrue(cpright in txt.text)

        def run(val):
            self.setUp()
            self.driver.find_element(By.CSS_SELECTOR, "a[data-lang='de']").click()
            self.driver.find_element(By.CSS_SELECTOR, val).click()
            check()

        values = [
            "a[data-i18n='nav-about']",
            "h2[data-i18n='rel-title'] + a",
            "h2[data-i18n='ins-title'] + a",
            "h2[data-i18n='sfd-title'] + a",
            "h2[data-i18n='jsd-title'] + a",
            "h2[data-i18n='msd-title'] + a",
        ]

        self.driver.find_element(By.CSS_SELECTOR, "a[data-lang='de']").click()
        check()
        for val in values:
            run(val)

    @classmethod
    def tearDownClass(cls):
        """Method that runs after testing."""
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
