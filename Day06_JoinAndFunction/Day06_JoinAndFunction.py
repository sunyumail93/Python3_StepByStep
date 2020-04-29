#!/usr/bin/python3
#Day06_JoinAndFunction.py
#Aim: Convert bed format containing RNA sequences to a FASTA format, saving the bed information in the FASTA header
#Use Join and self-defined function

import sys
def ConvertBED2HeaderFasta():
	fi = open(sys.argv[1],'r')
	fo = open(sys.argv[2],'w')
	for line in fi:
		line=line.split()
		fo.writelines(">"+"_".join(line)+"\n")
		fo.writelines(line[6]+"\n")
	fi.close()
	fo.close()

if len(sys.argv) !=3:
	print("This script takes the BED2 data as input, converts it to a fasta format, and keeps original information in FASTA header")
	print("Example: Day6_JoinAndFunction.py [Input.bed2] [Output.fasta]")
else:
	ConvertBED2HeaderFasta()
