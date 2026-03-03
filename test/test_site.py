
import time
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_s6(browser):
    home_page = HomePage(browser)
    home_page.open()
    home_page.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')

def test_two_monitors(browser):
    home_page = HomePage(browser)
    home_page.open()
    home_page.click_monitor()
    time.sleep(3)
    home_page.check_products_count(2)