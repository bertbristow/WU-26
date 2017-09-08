import unittest
from selenium import webdriver
from pyvirtualdisplay import Display

class TestSelenium(unittest.TestCase):
    #test case!!!!
    def test_browse_google(self):
        driver = webdriver.Chrome()
        # driver = webdriver.Remote()
        #     command_executor='http://127.0.0.1:4444/wd/hub',
        #     desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True})

        driver.get('https://dev.worldunited.com/signup/register')
        print driver.title
        assert driver.title == "World United"

    def test_browse_firefox(self):
        display = Display(visible=0, size=(800, 600))
        display.start()
        driver = webdriver.Firefox()
        driver.get('https://dev.worldunited.com/signup/register')
        print driver.title
        assert driver.title == "World United"

if __name__=='__main__':
    unittest.main()
