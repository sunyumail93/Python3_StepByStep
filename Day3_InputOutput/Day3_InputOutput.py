#!/usr/bin/python3
#Day3_InputOutput.py
#Aim: Read a file, print, and write the first three columns of the first line to another new file. 

import sys

Total_Argument=len(sys.argv)-1

if Total_Argument != 2:
	print("Please input two file names")
else:
	First_argument=sys.argv[1]
	Second_argument=sys.argv[2]

	print("Input file:",First_argument)
	print("Output file:",Second_argument)
	
	fi=open(First_argument, "r") 	 #r: read mode
	fo=open(Second_argument, "w") 	 #w: write mode
	text=fi.readlines()		 #Read all lines into a list	
	FirstLine=text[0].strip()    	 #Remove \n at the end of the first line text[0]
	Elements=FirstLine.split()	 #Split the first line based on tab
	
	fo.write(Elements[0]+"\t"+Elements[1]+"\t"+Elements[2]+"\n")  #Write to output file. Remember to add "\n"
	
	fi.close()			 #Close file
	fo.close()
