
from __future__ import print_function
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display

class TestSelenium(unittest.TestCase):
    #test case!!!!
    def test_browse_google(self):
        driver = webdriver.Chrome()
        driver.get('https://dev.worldunited.com/signup/register')
        print driver.title
        assert driver.title == 'World United'
        driver.quit()

    def test_browse_firefox(self):
        '''display = Display(visible=0, size=(800, 600))
        display.start()
        '''

        driver = webdriver.Firefox()
        driver.get('https://dev.worldunited.com/signup/register')
        print driver.title
        assert driver.title == 'World United'
        driver.quit()

    def test_signup_failure(self):
        email = 'test1@test.com'
        password = 'testpassword1'

        driver = webdriver.Chrome()
        driver.get('https://d2qa3wj7w00hfu.cloudfront.net/signup')
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/form/div/div/div[2]/div[1]/input').send_keys(email)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/form/div/div/div[3]/div[1]/div[1]/input').send_keys(password)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/form/div/div/div[4]/div[1]/div/input').send_keys(password)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/form/div/div/div[5]/div/label').click()
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[4]/button[1]').click()
        driver.implicitly_wait(10)


        # https://gist.github.com/huangzhichong/3284966

        # Wait for page to load
        # driver.implicitly_wait(10)

        # find element by xpath, insert text
        # find element by xpath, click
        
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH , '//*[@id="root"]/div/div/div/div/form/div/div/div[6]/div/div[1]')))
        finally:
            assert element.text.startswith('Signup failed')
            driver.quit()

if __name__=='__main__':
    unittest.main()


if __name__=='__main__':
    unittest.main()
