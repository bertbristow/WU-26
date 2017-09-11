from __future__ import print_function
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display

class TestSelenium(unittest.TestCase):
    
    def test_browse_google(self):
        driver = webdriver.Chrome()
        driver.get('https://dev.worldunited.com/signup/register')
        print(driver.title)
        assert driver.title == 'World United'
        driver.quit()

    def test_browse_firefox(self):
        driver = webdriver.Firefox()
        driver.get('https://dev.worldunited.com/signup/register')
        print(driver.title)
        assert driver.title == 'World United'
        driver.quit()

    def test_signup_failure(self):
        email = 'test@test.com'
        password = 'testpassword'

        driver = webdriver.Firefox()
        driver.get('https://d2qa3wj7w00hfu.cloudfront.net/signup')
        driver.find_element_by_xpath('//input[@name="emailAddress"]').send_keys(email)
        driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
        driver.find_element_by_xpath('//input[@name="confirmPassword"]').send_keys(password)
        driver.find_element_by_xpath('//input[@type="checkbox"]').click()
        driver.find_element_by_css_selector('button.ui.fluid.primary.button').click()
        
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR , 'div.ui.error.message')))
        finally:
            assert element.text == 'Signup failed, please try again later'
            driver.quit()


if __name__=='__main__':
    unittest.main()
