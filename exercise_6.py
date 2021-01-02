from _ast import Assert

import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#1.https://www.spx.com.tr/ adresine gidin.
#2.Herhangi bir kategori sayfasına gidin.
#3.Herhangi bir ürün sayfasına gidin.
#4.Ürünü sepete ekleyin.
#5.Sepet sayfasına gidin.
#6.Anasayfaya geri dönün.


class Test(unittest.TestCase):

    def basicSeleniumProject(self):

        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 20)

        WOMAN_CATEGORY = (By.XPATH, "(//*[@class = 'navigation__desktop-link'])[3]")
        GO_TO_MAIN_PAGE = (By.CLASS_NAME, "header__icon")
        PRODUCT_PAGE = (By.XPATH, "(//div[@class = 'js-product-wrapper product-card-focus '])[1]")
        SELECT_SIZE = (By.XPATH, "(//*[@class = 'd-flex align-items-center justify-content-center text-reset product__variant product__size-variant mb-3 js-variant'])[1]")
        ADD_TO_CART = (By.XPATH, "//button[@class= 'btn pz-button__add-to-cart js-add-to-cart pz-button__action']")
        GO_TO_BASKET = (By.XPATH, "(//*[@class='button-wrapper'])[2]")
        PRODUCT_PAGE_ASSERTION = (By.ID, "ProductPage")
        driver.get("https://www.spx.com.tr/")
        driver.maximize_window()
        time.sleep(3)

        wait.until(EC.element_to_be_clickable(WOMAN_CATEGORY)).click()
        assert 'KADIN' in driver.title

        wait.until(EC.presence_of_element_located(PRODUCT_PAGE)).click()
        self.assertEqual(PRODUCT_PAGE_ASSERTION, ('id', 'ProductPage'))

        wait.until(EC.presence_of_element_located(SELECT_SIZE)).click()

        wait.until(EC.presence_of_element_located(ADD_TO_CART)).click()

        wait.until(EC.element_to_be_clickable(GO_TO_BASKET)).click()
        self.assertEqual("https://www.spx.com.tr/baskets/basket/", driver.current_url)

        wait.until(EC.presence_of_element_located(GO_TO_MAIN_PAGE)).click()
        self.assertEqual("https://www.spx.com.tr/", driver.current_url)

        driver.quit()


Test().basicSeleniumProject()
