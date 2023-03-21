# data_testing_package
This package is for the testing of InstrumentDetails.csv and PositionDetails.csv data from two files. 



**Code Structure:**
This pipeline is constructed with the following design: 

configurations for the specific load are read from the path data\ InstrumentDetails.csv and PositionDetails.csv file (e.g. file naming conventions) then an object for data_comparison is constructed by passing the arguments with  [InstrumentDetails.csv and Position Details.csv  ]


**Arguments:**

This code works with 2 files InstrumentDetails.csv and PositionDetails.csv ( follow the naming conventions )
Note* - source.csv and target.csv should have same column names and shape.


**Result:**

The data's are merged and formed PositionReport.csv with the below details 


Output File
File Name PositionReport.csv
Column details
ID Primary ID
PositionID Primary ID of position file
ISIN Unique Instrument Identifier
Quantity Number of instruments in position
Total Price Quantity * Unit Price
