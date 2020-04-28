#!/usr/bin/python
#Day05_DebarcodeFASTQ_ByChuck.py
#Aim: Loop through a FASTQ file containing sequenced reads. Find the adapter and put them into the first line of the FASTQ
#We look for CTCCAGTCAC and extract the 6 nt after that. Finally we put the information in line1 of each 4 lines.

import sys
TargetSeq='CTCCAGTCAC'
ChunkSize=1000
def ChunkGenerator(fi, block_size=ChunkSize):
    block=[]
    for line in fi:
        block.append(line)
        if len(block) == block_size:
            yield block
            block=[]
    if block:                #If the last block is not empty
        yield block

if len(sys.argv) !=3:
    print("This script loops through a FASTQ file containing sequenced reads, finds the adapter and puts it into the first line of the FASTQ")
    print("Example: Day5_DebarcodeFASTQ.py [Input.fastq] [Output.fastq]")
else:
    fi=open(sys.argv[1],'r') 
    fo=open(sys.argv[2],'w')
    BlockCounter=0
    for lines in ChunkGenerator(fi):
        BlockCounter+=ChunkSize
        print("Processing lines: "+str(BlockCounter))
        for i in range(0,len(lines),4):
            Sequence=lines[i+1].strip()
            pos=Sequence.find(TargetSeq)
            if pos >= 0 and pos+16 < len(Sequence):   #Make sure the Hexamer won't be out of the sequence
                Barcode=Sequence[pos+10:pos+16]
                #print("Found barcode: "+Barcode)
                fo.writelines(lines[i].strip()+":"+Barcode+"\n")
                fo.writelines(lines[i+1].strip()+"\n")
                fo.writelines(lines[i+2].strip()+"\n")
                fo.writelines(lines[i+3].strip()+"\n")
            else:
                #print("Skipping line")
                fo.writelines(lines[i].strip()+"\n")
                fo.writelines(lines[i+1].strip()+"\n")
                fo.writelines(lines[i+2].strip()+"\n")
                fo.writelines(lines[i+3].strip()+"\n")
    fi.close()
    fo.close()
