5, 2020-04-13
Aim: Loop through a FASTQ file containing sequenced reads. Find the adapter and put them into the first line of the FASTQ
We look for CTCCAGTCAC and extract the 6 nt after that, put the information in line1 of each 4 lines.
Code: Day5_DebarcodeFASTQ.py
Some notes:
1, Compare Day4 and Day5. In Day 4 we can directly loop though fi (fast and efficient), but Day 5 we have to use fi.readlines(), which is more memory consuming.
2, Learn to use yield chunk generator, reading a chunk at one time, rather than the whole data
Example:
Input: 
@NB551651:198:H7J33BGXF:1:11101:14980:1054 1:N:0:0
AGACANCGATAGTGAACTAGTACCTGGAATTCTCGGGTGCCAAGGAACTCCAGTCACAGTCAAATCTCGTATGCC
+
AAAAA#AEEEEEAAEEAAEEEEAEEEEEEEEEEEEEAEE<EEAEEE/EEEEEEEEEEEEEAEEAE/EEEEEEAAE
Processing:
Base on our small RNA library construction protocol:
Adapter sequence: 5¡ä-rAppTGGAATTCTCGGGTGCCAAGG/ddC/-3¡ä
Then the Barcode primer containing the index Hexamer (highlighted part is reverse complement with the adapter, Hexamer):
5¡ä-CAAGCAGAAGACGGCATACGAGATTTGACTGTGACTGGAGTTCCTTGGCACCCGAGAATTCCA-3¡ä
Then we can find them in the sequenced reads:
AGACANCGATAGTGAACTAGTACCTGGAATTCTCGGGTGCCAAGGAACTCCAGTCACAGTCAAATCTCGTATGCC
We have many barcode sequences, and we need to extract the Hexamer and save them into the end of line1
Output:
@NB551651:198:H7J33BGXF:1:11101:14980:1054 1:N:0:0:AGTCAA
AGACANCGATAGTGAACTAGTACCTGGAATTCTCGGGTGCCAAGGAACTCCAGTCACAGTCAAATCTCGTATGCC
+
AAAAA#AEEEEEAAEEAAEEEEAEEEEEEEEEEEEEAEE<EEAEEE/EEEEEEEEEEEEEAEEAE/EEEEEEAAE

Some notes:
1, Day5_DebarcodeFASTQ_ByChuck.py: 
	Use fi.readlines() to read in all data at one time. This can be memory consuming when the input is very large.
	Day5_DebarcodeFASTQ_ByChuck.py WholeLane.fastq WholeLane.debarcoded.fastq
2, Day5_DebarcodeFASTQ_MemoryConsuming.py:
	This "yield" key word returns a chunk everytime, until the end of the file 
	Day5_DebarcodeFASTQ_MemoryConsuming.py WholeLane.fastq WholeLane.debarcoded.fastq
