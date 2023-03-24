from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class test_suite(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        
        """ CREATNG  A SETUP FOR USING IN THE TEST SUITE"""
        
        self.driver = webdriver.Firefox()

        self.driver.get("https://reqres.in")
        
        print("SETUP IS CREATED SUCCESSFULLY")


    
    def test404(self):
        
        ''' TEST CASES TO VALIDATE THE 404 RESPONSE CODE FOR SINGLE USER NOT FOUND'''
        

        try:
            element =  self.driver.find_element("xpath","//*[text()='404']")
            
        except:
            
            print("element not found")


        time.sleep(5)

        element = self.driver.find_element("xpath","//a[text()=' Single user not found ']")

        element.click()
        
        time.sleep(5)

        element =  self.driver.find_element("xpath","//*[text()='404']")

        if element:
                  
                  print("Test case is succesfully executed")
                    
                    
    def testSupport(self):
        
        """ LIST THE SUPPORT PAGE """
        print("Entering case3")
        
        self.driver.get("https://reqres.in/#support-heading")
        time.sleep(5)
    
    @classmethod                
    def tearDownClass(self):
        
        """ TEARDOWN A SETUP """

        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()
