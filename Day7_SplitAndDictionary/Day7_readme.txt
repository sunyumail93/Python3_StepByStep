7, 2020-04-23
Aim: Loop through a FASTA file converted from bed file in Day 6, count sequences based on the gnomonic 5´-end position (rather than the sequence itself), and report 5´-end positions and occurrence from dictionary
Input FASTA example:
>chr1_3015605_3015633_1_18638_-_CCAGAAGCTGGAAAGAACCCAGATGCCC
CCAGAAGCTGGAAAGAACCCAGATGCCC
>chr1_3015606_3015633_5_18940_-_CCAGAAGCTGGAAAGAACCCAGATGCC
CCAGAAGCTGGAAAGAACCCAGATGCC
>chr1_3015606_3015634_16_18381_+_GGCATCTGGGTTCTTTCCAGCTTCTGGC
GGCATCTGGGTTCTTTCCAGCTTCTGGC
Processing:
a, Only read the information from header, and split using “_” as separator
b, Get the 5’ 1 nt position considering strand + or -, and store the position as key, then store the reads number (column 4 after split) as value, using dictionary:
chr1_3015632_3015633_-    1
chr1_3015632_3015633_-    5
chr1_3015606_3015607_+    16
Since first and second are from the same 5’end, combine them: 
chr1_3015632_3015633_-    6
Finally output the dictionary into a two-column tab-delimited table
Code: Day7_SplitAndDictionary.py

Some notes:
1, Use split function with given separator
2, Use dictionary to store information dynamically. Use int and str conversion.
3, Loop through dictionary: Dict.items()
    Day7_SplitAndDictionary.py Input.fa Output.counts.txt