import unittest
import requests

class test_suite(unittest.TestCase):



    def get_api(self,api):
        response = requests.get(api)
        return response

    def create_api(self,api,payload):
        reponse = requests.post(url=api,json=payload)
        print(reponse)
        return reponse
    
    
    def test1(self):
    
        resp = self.get_api('https://reqres.in/api/users/2')

        if resp.status_code == 200:
            print("pass")
            
    def test2(self):
        
        resp_create = self.create_api('https://reqres.in/api/users',{"name" : "morpheus" , "job" : "leader"})
       
        if resp_create.status_code == 201:
            print("pass")
            
            

if __name__ == '__main__':
    unittest.main()
            
            
