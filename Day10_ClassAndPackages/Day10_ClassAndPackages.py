#!/usr/bin/env python3
"""
Day10_ClassAndPackages.py
Aim: Python class and other packages: argparse, pandas, seaborn, matplotlib
In this last day tutorial, we are going to build a small software that can take arguments from command line, process data with object oriented programming, and output summary and figures.
Here are the steps:
1, Use argparse package to process arguments from command line
    Set -i (or --input) and -o (or --output)
2, Write functions in a separate script, including reading inputs and constructing objects.
    Construct a Gene object to store original data and average expression, fold changes between KD to WT
3, Output a table containing summary:
    For each gene, calculate average expression in KD and WT, then calculate a fold change
4, Also output a heatmap representing the summarized data table
"""

import sys
import pandas as pd
import argparse
import Day10_Subscript_ReadData as ReadData
import Day10_Subscript_PlotFigure as PlotFigure

if len(sys.argv) == 1:
	print("Please input arguments. Use -h or --help to see manual.")
else:
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--input", type=str, dest="InputFile", help="Input file in .csv format", required=True)
	parser.add_argument("-o", "--output", type=str, dest="Out_Prefix", help="Prefix of output files", default="Output")
	args = parser.parse_args()    #args is a list of arguments. If default values not set, it will be None or False
	
	print("Arguments received:")
	print("InputFile:",args.InputFile)
	print("Out_Prefix:",args.Out_Prefix)
	
	Summary = ReadData.ProcessData(args.InputFile)
	print("Data processed. The head of the data:")
	print(Summary.head())
	
	Summary.to_csv(args.Out_Prefix+".csv")
	
	PlotFigure.PlotHeatmap(Summary, args.Out_Prefix+".png")