#!/usr/bin/python3
#Day04_TranslateFASTA.py
#Aim: Loop through a FASTA file containing CDS regions. Translate them into protein sequences using dictionary.

import sys

#We defind all functions at the beginning
def translate(sequence):
    codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    }
    proteinsequence = ''
    sequence=sequence.upper()           #Change all letters to upper case
    start = sequence.find('ATG')        #Variable start returns the position of the first ATG
    if start >= 0:
        SequenceRange = sequence[int(start):]
        if len(proteinsequence) == 0 or proteinsequence[-1] != '*':     #If the protein sequence is empty (cannot get -1 value), or the last AA hasn't reached stop codon, continue translation.
            for n in range(0,len(SequenceRange),3):                     #Use range function: create a serial number within [0,len(SequenceRange)], increment with 3: e.g. 0,3,6,9...
                if SequenceRange[n:n+3] in codontable:
                    proteinsequence += codontable[SequenceRange[n:n+3]]
    else:                               #Guess if ATG not found, what's the value of 'start'?
        proteinsequence += '-'
    return(proteinsequence)

if len(sys.argv) != 2: #if the length of argv is not equal to 2, then print warning message
    print("This script takes DNA fasta seq as input, finds the first ATG and translates it until the stop codon")
    print("This script can only output the first found ORF (starts from the first ATG)")
    print("If the sequence doesn't have stop codon, it will translate into the last AA, and discard last 1 or 2 nt if the length cannot be divided by three")
    print("If no ATG found, it will return -")
    print("Usage: [Day4_TranslateFASTA.py] [Fasta]")
else:
    fi=open(sys.argv[1],'r')
    for line in fi:                     #We can skip fi.readlines() and directly loop fi
        if line[0] == '>':
            print(line.strip())         #Directly print FASTA header line
        else:
            seq=translate(line.strip())
            print(seq)
    fi.close()
