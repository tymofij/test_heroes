import time
from selenium import webdriver
from pages import DashboardPage

driver = webdriver.Firefox()

def test_dashboard_count():
    """ Dashboard has four heroes
        and first one is Narco
    """
    dashboard = DashboardPage(driver)
    dashboard.open()
    assert len(dashboard.heroes) == 4
    assert dashboard.heroes[0].text == 'Narco'

def teardown_module():
    driver.quit()