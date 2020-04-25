#!/usr/bin/python3
#Day9_BioPython.py
#Aim: Use BioPython to extract information from a Genbank record. 
#     Get familiar with Seq, SeqRecord, SeqFeature, OrderedDict objects and I/O methods.

from Bio import SeqIO
record = SeqIO.read("Gapdh.genbank", "genbank")
print("Imported record as SeqRecord object",record)                      #record is a SeqRecord object

print("Sequence:","\n",record.seq,"\n\n")                                #record.seq is a Seq object
print("Description of the gene: ","\n",record.description)

#Get CDS feature
print("CDS feature as a SeqFeature object:","\n",record.features[5])     #This feature is a SeqFeature object
print("SeqFeature type:","\n",record.features[5].type)
print("SeqFeature location:","\n",record.features[5].location)
print("SeqFeature qualifiers OrderedDict:","\n",record.features[5].qualifiers)

#Extract CDS information from the dictionary
CDSDict = record.features[5].qualifiers
for key,value in CDSDict.items():
	print(key,value)
TranslatedAA = CDSDict['translation'][0]
print("Translated sequence:\n",TranslatedAA)

#Play with the Seq object:
Sequence=record.seq
print(Sequence)
print("Length:",len(Sequence))
from Bio.SeqUtils import GC
print("GC percentage:",GC(Sequence))
print("Get the sequences:\n",str(Sequence))
print("Change to lower cases:\n",Sequence.lower())
print("Reverse complement:\n",Sequence.reverse_complement())
print("Convert to RNA:\n",Sequence.transcribe())
print("Translate the first ATG:\n",Sequence.translate(to_stop=True))

#Output sequences: Check https://biopython.org/wiki/SeqIO for more formats
SeqIO.write(record, "Sequence.multiline.fasta", "fasta")
SeqIO.write(record, "Sequence.2line.fasta", "fasta-2line")
SeqIO.write(record, "Sequence.embl.fasta", "embl")