from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    URL = 'http://localhost:4200/'
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, query):
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.presence_of_element_located((by, query)))

    def location(self):
        return driver.execute_script('return window.location')


class DashboardPage(BasePage):
    HERO_LOCATOR = (By.CSS_SELECTOR, '.module.hero')

    def is_loaded(self):
        self.wait_for_element(*self.HERO_LOCATOR)

    def open(self):
        self.driver.get(self.URL + 'dashboard')
        self.is_loaded()

    @property
    def heroes(self):
        return self.driver.find_elements(*self.HERO_LOCATOR)


class EditPage(BasePage):

    def is_loaded(self):
        self.wait_for_element(By.CSS_SELECTOR, 'my-hero-detail h2')

    def open(self, hero_id):
        self.driver.get(self.URL + 'detail/{}'.format(hero_id))
        self.is_loaded()

    @property
    def header(self):
        return self.driver.find_element_by_tag_name('h2')

    @property
    def name(self):
        return self.driver.find_element_by_css_selector('my-hero-detail input')

    @property
    def save_bnt(self):
        return self.driver.find_element_by_xpath('//my-hero-detail/div/button[text()="Save"]')
