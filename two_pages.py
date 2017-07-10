import time
from selenium import webdriver
from pages import DashboardPage, EditPage

driver = webdriver.Firefox()

class TestDashboardEdit():
    FIRST_HERO = 'Narco'
    FIRST_HERO_ID = 12

    def test_nav_to_edit(self):
        """ Dashboard has four heroes
            and first one is Narco
        """
        dashboard = DashboardPage(driver)
        dashboard.open()
        narco = dashboard.heroes[0]
        assert narco.text == self.FIRST_HERO
        narco.click()

        edit = EditPage(driver)
        edit.is_loaded()
        assert self.FIRST_HERO in edit.header.text

    def test_edit_to_nav(self):
        """ Edit page can edit name of the first hero
            and redirect to Dashboard
        """
        edit = EditPage(driver)
        edit.open(self.FIRST_HERO_ID)

        edit.name.clear()
        edit.name.send_keys("Dave")
        edit.save_bnt.click()

        dashboard = DashboardPage(driver)
        dashboard.is_loaded()

        # Aaaand it does not work.
        # Looks like we have found a bug in demo app
        # Which is why test separation is needed
        assert dashboard.heroes[0].text == 'Dave'


def teardown_module():
    driver.quit()