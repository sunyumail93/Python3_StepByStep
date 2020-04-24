#!/usr/bin/python3
#Day8_TupleSet2DList.py
#Aim: Besides list and dictionary, there are more objects/data structures: tuple, set and two dimensional list (array)
#Tuple: (1,2,3,’string’,1,2,3), different to List, Tuple is unmutable, so you cannot append or change values. Same as List, Tuple and can store repeated, different types of values.
#    But Tuple can only be created directly, or converted from a List (or Set). Looping through a Tuple is 10 times faster than looping a List.
#Set: {'Idrish', 'Archi', 'Jay’}, non-repetitive list, faster then list. Set doesn’t have order, and it will display by a default order. 
#    Set can be modified, or converted from a List or Tuple.
#2D List/Nested List: Can be used to represent matrix, 2D, 3D, etc.
#Here is the question: 
#1, Import ATACseq peaks and store chromosome and length  information using Tuples
#2, Count how many chr appeared using Set
#3, Get a distribution of peak lengths using 2D list (count by every 100 nt window from 0-1000 nt, and then >1000 nt) group by each chromosome
#4, Output a Pandas DataFrame containig length distribution to a csv format

import sys
import pandas as pd

if len(sys.argv) !=3:
	print("Import ATACseq peaks and store chromosome and length  information using Tuples")
	print("Count how many chr appeared using Set")
	print("Get a distribution of peak lengths using 2D list (count by every 100 nt window from 0-1000 nt, and then >1000 nt) group by each chromosome")
	print("Output a Pandas DataFrame containig length distribution to a csv format")
	print("Example: Day8_TupleSet2DList.py [Input.peaks] [Output.csv]")
else:
	fi = open(sys.argv[1],'r')
	
	#Use the following variables to store data
	Chr_List=[]
	Length_List=[]
	Chr_Set=set()
	
	for line in fi:
		line=line.split()
		Chr_List.append(line[0])
		Chr_Set.add(line[0])							#You can also use Chr_Set=set(Chr_Tuple) after this looping
		Length_List.append(int(line[2])-int(line[1]))
	Chr_Tuple=tuple(Chr_List)
	Length_Tuple=tuple(Length_List)
	print("Length of the List (data):",len(Chr_Tuple))
	print("Length of the Set (unique chromosome):",len(Chr_Set),Chr_Set)
	print("Max of Length:",max(Length_Tuple))
	
	#Prepare Tuples
	Windows=(0,100,200,300,400,500,600,700,800,900,1000,max(Length_Tuple)+1)   #Create a Tuple containing boundaries
	Chr=tuple(sorted(Chr_Set))												   #Sort the Set and convert to Tuple, since Set doesn't preserve a good order
	print("Sorted Chr:",Chr)
	
	#Construct 2D List called Matrix
	Matrix=[0]*len(Chr)					#Initialize the 0 to store each Chr length distribution
	for i in range(len(Chr)):
		Matrix[i]=[0]*(len(Windows)-1)  #You cannot do Histogram=[0]*(len(Windows)-1) then do Matrix.append(Histogram), since that will make each row the same List!
	print("Initialized Matrix:","\n",Matrix)						#Matrix initialized
	
	for i in range(len(Length_Tuple)):
		for w in range(0,len(Windows)-1):
			if Length_Tuple[i] >= Windows[w] and Length_Tuple[i] < Windows[w+1]:	#When the Length falls into a window
				loc=Chr.index(Chr_Tuple[i])											#Locate the index of current Chr_Tuple in Chr Tuple
				Matrix[loc][w]+=1
	print("Final Matrix:","\n",Matrix)
	
	df = pd.DataFrame(Matrix, columns=['0-100', '100-200', '200-300','300-400','400-500','500-600','600-700','700-800','800-900','900-1000','>1000'],
					index=Chr)
	print("Pandas Data Frame:","\n",df)
	df.to_csv(sys.argv[2])
	fi.close()
