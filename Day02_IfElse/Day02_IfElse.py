#!/usr/bin/python3
#Day2_IfElse.py
#Aim: Solve the missing/extra input problem using if/else statement. Use internal function len(), print()

#This sys package communicate Python with terminal
import sys

Total_Argument=len(sys.argv)-1   #sys.argv[0] is the script name

if Total_Argument == 0:
	print("Please input two arguments")
elif Total_Argument < 2:
	print("Argument not enough. Please input two arguments")
elif Total_Argument > 2:
	print("Two many arguments. Please input two arguments")
else:
	First_argument=sys.argv[1]
	Second_argument=sys.argv[2]
	#print
	print("First argument:",First_argument)
	print("Second argument:",Second_argument)