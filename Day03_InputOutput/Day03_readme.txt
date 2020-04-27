3, 2020-04-09
Aim: Read a file, print, and write the first three columns of the first line to another new file.
Code: Day3_InputOutput.py

Some notes:
1, If the input is very big, reading everything using readlines takes longer time. We can consider alternative methods.
2, split function: by default split by whitespace (tab/space etc.), but you can customize this: split(list, ¡°_¡±)
3, Run script: Day03_InputOutput.py Input.bed2 Output.txt