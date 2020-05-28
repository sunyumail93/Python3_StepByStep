# Python3_StepByStep
A step-by-step 10-day Python3 tutorial especially for bioinformatician

Codes:

Day01_ReadInput_ExecutablePython.py
* Read input using ‘sys', and make the python script executable.

Day02_IfElse.py
* Solve the missing/extra input problem using if/else statement. Use internal function len(), print()

Day03_InputOutput.py
* Read a file, print, and write the first three columns of the first line to another new file.

Day04_TranslateFASTA.py
* Loop through a FASTA file containing CDS regions. Translate them into protein sequences using dictionary.

Day05_DebarcodeFASTQ_ByChuck.py
* Loop through a FASTQ file containing sequenced reads. Find the adapter and put them into the first line of the FASTQ, and use `yield` to  be memory efficient.

Day06_JoinAndFunction.py
* Convert bed format containing RNA sequences to a FASTA format, saving the bed information in the FASTA header. Use `join` and self-defined function.

Day07_SplitAndDictionary.py
* Loop through a FASTA file converted from bed file in Day 6, `split` using separator and count sequences based on the gnomonic 5´-end position (rather than the sequence itself), and report 5´-end positions and occurrence from `dictionary`

Day08_TupleSet2DList.py
* Import ATACseq peaks and store chromosome and length information using `Tuple`, then count unique chr appeared using `Set`, and get a distribution of peak lengths using `2D List (Matrix)`, finally format the Matirx into a `Pandas DataFrame`

Day09_BioPython.py
* Import Genbank sequence record and process using Biopython package. Get familiar with `Seq`, `SeqRecord`, `SeqFeature`, `OrderedDict` objects and I/O methods

Day10_ClassAndPackages.py
* Implement Python class and other packages: `argparse`, `pandas`, `seaborn`, `matplotlib` to build a small software that can take gene expression values as input, calculate fold changes and plot figures
