import unittest
from selenium import webdriver
from pyvirtualdisplay import Display

class TestSelenium(unittest.TestCase):
    #test case for google
    def test_browse_google(self):
        driver = webdriver.Chrome()
        driver.get('http://wu-web.s3-website-eu-west-1.amazonaws.com/')
        print driver.title
        assert driver.title == "React App"  

    def test_browse_firefox(self):
        display = Display(visible=0, size=(800, 600))
        display.start()
        driver = webdriver.Firefox()
        driver.get('http://wu-web.s3-website-eu-west-1.amazonaws.com/')
        print driver.title
        assert driver.title == "React App"

if __name__=='__main__':
    unittest.main()
