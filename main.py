import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome("C:\Program Files (x86)\ChromeDriver.chromedriver.exe")
        self.driver.get("http://www.python.org")

    def test_search_python(self):
        #load the mainpage
        mainPage = page.MainPage(self.driver)
        #if the mainpage exist, continue
        assert mainPage.is_title_matches()
        #set search content to pycon
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        #initialize new searchresult page and return if results is found
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    # def test_title(self):
    #     mainPage = page.MainPage()
    #     assert mainPage.is_title_matches() 

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()