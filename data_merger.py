import unittest
import os 
import pandas as pd

class data_merge(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        
        try:
            if os.path.exists("input/InstrumentDetails.csv"):
                self.source_table = pd.read_csv("input/InstrumentDetails.csv")
                
        except:
            print("No such file exists namely input/InstrumentDetails.csv" )
            
            
        
        try:
            if os.path.exists("input/PositionDetails.csv"):
                self.target_table = pd.read_csv("input/PositionDetails.csv")
        except:
            print("No such file exists namely input/PositionDetails.csv")
            
            
                
        try:
            if os.path.exists("output/PositionReport.csv"):
                self.position_report= pd.read_csv("output/PositionReport.csv")
        except:
            print("No such file exists namely input/PositionReport.csv")


        
    def test_check_data_null_for_source(self):
        
        
        print(self.source_table)
        
        print(self.source_table.isnull().values.any())
        if self.source_table.isnull().values.any():
             self.fail("An value is empty")            
        else:
             print("Data's are ok")


        
    def test_check_data_null_for_target(self):
        
        
        print(self.target_table)
        
        print(self.target_table.isnull().values.any())
              
        
        if self.target_table.isnull().values.any():
             self.fail("An value is empty======> Explicity made to fail as there an empty data")
            
            
        else:
             print("Data's are ok")

                           
    def test_logic_check(self):
        
        
        self.combined = pd.merge(self.source_table,self.target_table,how='left',left_on='ISIN',right_on='ISIN')
        self.combined['price'] = self.combined['Quantity'] * self.combined['Unit_Price']
        
        if (self.combined['price'].equals(self.position_report['price'])):
            print("Data's are matching")
                          
        else:
            self.fail("The case is failing")
        
        
        
    def test_false_logic_check(self):
        
        
        self.combined = pd.merge(self.source_table,self.target_table,how='left',left_on='ISIN',right_on='ISIN')
        self.combined['price'] = self.combined['Quantity'] - self.combined['Unit_Price']
        
        if (self.combined['price'].equals(self.position_report['price'])):
            print("Data's are matching")
                          
        else:
            self.fail("The case is failing ====>====> this case is explicity failed")#====> this case is explicity failed
        
        
if __name__ == '__main__':
    unittest.main()
            
