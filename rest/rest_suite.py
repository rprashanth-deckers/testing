import unittest
import requests

class test_suite(unittest.TestCase):



    def get_api(self,api):
        ''' Funtion used to get the user for the give API'''
        response = requests.get(api)
        return response

    def create_api(self,api,payload):
        ''' Function used to create the user for a given API'''
        
        reponse = requests.post(url=api,json=payload)
        print(reponse)
        return reponse
    
    
    def test1(self):
        
        ''' Test cases to validate the get request'''
    
        resp = self.get_api('https://reqres.in/api/users/2')

        if resp.status_code == 200:
            print("The test scenario is covered to test the reponse code 201 passed successfully")
            
    def test2(self):
        
        ''' Test case to Validate the create request '''
        
        resp_create = self.create_api('https://reqres.in/api/users',{"name" : "morpheus" , "job" : "leader"})  # can pass run time argument
       
        if resp_create.status_code == 201:
            print("The test scenario is covered to test the reponse code 201 passed successfully")
            
    def test3(self):
        
        ''' To test the invalid URL Scenrio'''
        
        
        try:
            resp_create = get('dummy.com')

        except:
            print("Invalid URL Provided and the test case is passed as the logic")
            
        finally:
            print("The test case is passed successfully")

            

if __name__ == '__main__':
    unittest.main()
            
            
