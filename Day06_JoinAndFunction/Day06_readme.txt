6, 2020-04-15
Aim: Convert bed format containing RNA sequences to a FASTA format, saving the bed information in the FASTA header
Input data example:
chr1    3015605 3015633 1       18638   -       CCAGAAGCTGGAAAGAACCCAGATGCCC
chr1    3015606 3015633 5       18940   -       CCAGAAGCTGGAAAGAACCCAGATGCC
chr1    3015606 3015634 16      18381   +       GGCATCTGGGTTCTTTCCAGCTTCTGGC
Output example:
>chr1_3015605_3015633_1_18638_-_CCAGAAGCTGGAAAGAACCCAGATGCCC
CCAGAAGCTGGAAAGAACCCAGATGCCC
>chr1_3015606_3015633_5_18940_-_CCAGAAGCTGGAAAGAACCCAGATGCC
CCAGAAGCTGGAAAGAACCCAGATGCC
>chr1_3015606_3015634_16_18381_+_GGCATCTGGGTTCTTTCCAGCTTCTGGC
GGCATCTGGGTTCTTTCCAGCTTCTGGC
Code: Day6_JoinAndFunction.py

Some notes:
1, Use join function to concatenate values with a separator: ¡°_¡±.join(List)
2, Use self-defined function
3, Run the script: Day06_JoinAndFunction.py Data.bed2 Output.fa
