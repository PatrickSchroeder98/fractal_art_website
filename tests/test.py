import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FractalArtWebsiteTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # cls.base_url = "https://patrickschroeder98.github.io/fractal_art_website/index.html"
        cls.base_url = "http://127.0.0.1:5500/index.html"
        cls.driver.get(cls.base_url)

    def setUp(self):
        self.driver.get(self.base_url)

    def test_title(self):
        title = self.driver.title
        self.assertEqual("Fractal Art Website", title)

    def test_religiosity(self):

        self.driver.find_element(By.CSS_SELECTOR, "h2[data-i18n='rel-title'] + a").click()
        title = self.driver.title
        self.assertEqual("Religiosity - Fractal Art", title)

    def test_inspiration(self):

        self.driver.find_element(By.CSS_SELECTOR, "h2[data-i18n='ins-title'] + a").click()
        title = self.driver.title
        self.assertEqual("Inspiration - Fractal Art", title)

    def test_spring_flowers(self):
        self.driver.find_element(By.CSS_SELECTOR, "h2[data-i18n='sfd-title'] + a").click()
        title = self.driver.title
        self.assertEqual("Spring Flowers Draft - Fractal Art", title)

    def test_julia_set(self):
        self.driver.find_element(By.CSS_SELECTOR, "h2[data-i18n='jsd-title'] + a").click()
        title = self.driver.title
        self.assertEqual("Julia Set Drafts - Fractal Art", title)

    def test_mandelbrot_set(self):
        self.driver.find_element(By.CSS_SELECTOR, "h2[data-i18n='msd-title'] + a").click()
        title = self.driver.title
        self.assertEqual("Mandelbrot Set Drafts - Fractal Art", title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
