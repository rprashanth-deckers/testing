class data_merge():
    
    def __init__(self,src_file_path,target_file_path):
        
        """
         Initize the class object with the required informations as below 
         
         Manadatory Parameters:
         
         src_file_path : Pass the source file path  eg : 'app\input\InstrumentDetails.csv.csv'
         
         target_file_path : Pass the targe file path eg : 'app\inpout\PositionDetails.csv'
         
        """
        import pandas as pd
        import numpy as np

        self.source_table = pd.read_csv(src_file_path)#dtype={"client_id" :"float" ,"consumer_zip" : "float" })
        self.target_table = pd.read_csv(target_file_path)
        
        print(self.source_table.shape)
        print(self.target_table.shape)
        
        self.combined = pd.merge(self.source_table,self.target_table,how='left',left_on='ISIN',right_on='ISIN')
        print(self.combined)
        self.combined['price'] = self.combined['Quantity'] * self.combined['Unit_Price']
        print(self.combined)
