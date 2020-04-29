#!/usr/bin/python3
#Day07_SplitAndDictionary.py
#Aim: Loop through a FASTA file converted from bed file in Day 6, count sequences based on the gnomonic 5´-end position (rather than the sequence itself), 
# and report 5´-end positions and occurrence from dictionary
#You can take the first 12 lines from the data to test the script
#Use Split and Dictionary

import sys

if len(sys.argv) !=3:
	print("This script takes the FASTA data as input generated from Day6, counts sequences based on the gnomonic 5´-end position")
	print("The output is a two-column table")
	print("Example: Day7_SplitAndDictionary.py [Input.fasta] [Output.count.txt]")
else:
	fi = open(sys.argv[1],'r')
	fo = open(sys.argv[2],'w')
	Counts={}
	for line in fi:
		if line[0]=='>':
			elements=line.split("_")
			Chr=elements[0][1:]
			Col2=elements[1]
			Col3=elements[2]
			Reads=elements[3]
			Strand=elements[5]
			if Strand == "+":
				EndPos="_".join([Chr,Col2,str(int(Col2)+1),Strand])
			else:
				EndPos="_".join([Chr,str(int(Col3)-1),Col3,Strand])
			if EndPos in Counts:
				Counts[EndPos] +=int(Reads)
			else:
				Counts[EndPos] =int(Reads)
		else:
			pass   #This else and pass can be omitted
	#print(Counts)
	for k,v in Counts.items():
		print(k,"->",v)
		fo.writelines(k+"\t"+str(v)+"\n")
	fi.close()
	fo.close()
