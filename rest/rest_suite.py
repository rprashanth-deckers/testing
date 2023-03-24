import unittest
import requests
import json
from ddt import ddt, data


with open("data.json") as file:
    try:
        data1= json.load(file) 
        print(data)
    except json.decoder.JSONDecodeError:
        print("Invalid JSON") 
    else:
        print("Valid JSON") 


@ddt
class test_suite(unittest.TestCase):
    
  

    def get_api(self,api):
        ''' FUNTION USED TO GET THE USER FOR THE GIVE API'''
        response = requests.get(api)
        return response

    def create_api(self,api,payload):
        ''' FUNCTION USED TO CREATE THE USER FOR A GIVEN API'''
        
        reponse = requests.post(url=api,json=payload)
        print(reponse)
        return reponse
    
    
    def test1(self):
        
        ''' TEST CASES TO VALIDATE THE GET REQUEST'''
    
        resp = self.get_api('https://reqres.in/api/users/2')

        if resp.status_code == 200:
            print("The test scenario is covered to test the reponse code 201 passed successfully")
            
    @data(data1[0],data1[1],data1[2])
    def test2(self,value):
        
        ''' TEST CASE TO VALIDATE THE CREATE REQUEST '''
        resp_create = self.create_api('https://reqres.in/api/users',value)  # can pass run time argument
       
        if resp_create.status_code == 201:
            print("The test scenario is covered to test the reponse code 201 passed successfully")
            
    def test3(self):
        
        ''' TO TEST THE INVALID URL SCENRIO'''
        
        
        try:
            resp_create = get('dummy.com')

        except:
            print("Invalid URL Provided and the test case is passed as the logic")
            
        finally:
            print("The test case is passed successfully")
            
            
    def test4(self):
        
        '''TEST CASE TO VALIDATE A WRONG REQUES REQUEST '''

        resp_create = self.create_api('https://reqres.in/api/users',{"name" : "morpheus" , "job" : "leader"})  # can pass run time argument
        
        try:
            if resp_create.status_code == 200:
                print("The test scenario is covered to test the reponse code 200 passed successfully")               
        except:
            print("Code error")
        else:
            print("The create response is {} not 200 ".format(resp_create))

            

if __name__ == '__main__':
    unittest.main()
            
            
