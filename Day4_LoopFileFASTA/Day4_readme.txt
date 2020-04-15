4, 2020-04-11
Aim: Loop through a FASTA file containing CDS regions. Translate them into protein sequences using dictionary.
Code: Day4_TranslateFASTA.py

Some notes:
1, Use dictionary
2, use internal python3 function and method: 
    functions: len(string or list), range(start, end, increment)
    method: string.find(¡®ATG¡¯), string.strip()
3, When looping FASTA, directly loop the fi without reading them using fi.readlines()
    For this task, we can do this way, but for the next task, we probably have to use fi.readlines()
4, This time we directly print the output to bash. You can do: python3 Day4_TranslateFASTA.py > result.txt
5, Run the script: Day4_TranslateFASTA.py
