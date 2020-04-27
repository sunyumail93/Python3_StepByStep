#!/usr/bin/env python3
"""
Day10_Subscript_ReadData.py
Read data, construct object and process the data
"""

import pandas as pd

#This object stores gene expression information (one gene at a time)
class GeneExp:
    def __init__(self, Name, Conditions, Values):
        self.Name = Name
        self.Conditions = Conditions
        self.Values=Values
        self.KD=(Values[2]+Values[3])/2
        self.WT=(Values[0]+Values[1])/2
        self.FoldChangeKD2WT=(self.KD+1)/(self.WT+1)

def ProcessData(InputFile):
	Data=pd.read_csv(InputFile, index_col=0)
	print("Data Loaded. The head of the data:")
	print(Data.head())
	GeneNames = Data.index.values
	DataConditions = Data.columns.values
	Mean_WT = []
	Mean_KD = []
	FoldChangeKD2WT = []

	for i in GeneNames:       #Loop through the table and store each gene as GeneExp object
		ExpValues = Data.loc[i]
		DataObj = GeneExp(i, DataConditions, ExpValues)
		Mean_WT.append(DataObj.WT)
		Mean_KD.append(DataObj.KD)
		FoldChangeKD2WT.append(DataObj.FoldChangeKD2WT)
	df=pd.DataFrame(list(zip(Mean_WT, Mean_KD, FoldChangeKD2WT)), columns=["Mean_WT", "Mean_KD", "FoldChangeKD2WT"], index = GeneNames)
	return(df)
	