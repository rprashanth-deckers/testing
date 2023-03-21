import input
import pandas as pd
from data_merger import data_merge 

obj = data_merge(r"input/InstrumentDetails.csv", r"input/PositionDetails.csv")

obj.combined.to_csv("output/PositionReport.csv")