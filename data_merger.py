class data_merge():
    
    def __init__(self,src_file_path,target_file_path):
        
        """
         Initize the class object with the required informations as below 
         
         Manadatory Parameters:
         
         src_file_path : Pass the source file path  eg : 'app\input\InstrumentDetails.csv'
         
         target_file_path : Pass the targe file path eg : 'app\inpout\PositionDetails.csv'
         
        """
        import pandas as pd
        import numpy as np

        self.source_table = pd.read_csv(src_file_path)
        self.target_table = pd.read_csv(target_file_path)
        
        
        print("################################# InstrumentDetails.csv #############################################################")
        print(self.source_table)
        
        print("################################# PositionDetails.csv #############################################################")

        print(self.target_table)
        
        self.combined = pd.merge(self.source_table,self.target_table,how='left',left_on='ISIN',right_on='ISIN')
        self.combined['price'] = self.combined['Quantity'] * self.combined['Unit_Price']

        

        print("################################# PositionReport.csv #############################################################")

        print(self.combined)
        self.combined.to_csv("output/PositionReport.csv")
        
        print(" The above merged data has been placed in PositionReport.csv file successfully")
