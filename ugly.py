import time
from selenium import webdriver

driver = webdriver.Firefox()

def setup_module():
    driver.get('http://localhost:4200/dashboard')
    time.sleep(2)

def test_dashboard_count():
    heroes = driver.find_elements_by_css_selector('.module.hero')
    assert len(heroes) == 4

def test_dashboard_edit_narco():
    narco = driver.find_elements_by_css_selector('.module.hero')[0]
    assert narco.text == 'Narco'
    narco.click()
    time.sleep(2)

    header = driver.find_element_by_tag_name('h2')
    assert header.text == 'Narco details!'
    name = driver.find_element_by_css_selector('my-hero-detail input')
    name.clear()
    name.send_keys("Dave")
    save_btn = driver.find_element_by_xpath('//my-hero-detail/div/button[text()="Save"]')
    save_btn.click()
    time.sleep(2)

    dave = driver.find_elements_by_css_selector('.module.hero')[0]
    assert dave.text == 'Dave'

def teardown_module():
    driver.quit()