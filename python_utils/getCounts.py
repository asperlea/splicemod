__author__ = 'adriana'

import os
from collections import defaultdict

def main():
    if len(sys.argv) < 2:
        print "Need input file with unique contigs"
        exit(1)
    countsFile = open("countsPerbin.txt", "w")

    dirlist = [1-22079057, 2-22079058, 3-22079059, 4-22079060,  5-22079061, 6-22079062, 7-22079063, 8-22079064, 9-22079065]
    binContigsDicts = []
    for dir in dirlist:
        binContigsFile = open(dirlist + "/Data/Intensities/BaseCalls/PEARresults100.assembled.fastq")
        binContigs = defaultdict(int)
        for contig in binContigsFile:
            binContigs[contig] += 1
        binContigsDicts.append(binContigs)

    contigsFile = open(sys.argv[1], "r") # contigs file
    countsPerBin = []
    for contig in contigsFile:
        for binDict in binContigsDicts:
            counts = 0
            for binContig in binDict:
                if contig in binContig:
                    counts += binDict[binContig]
            countsPerBin.append(counts)
        countsFile.write(contig)
        countsFile.write(str(countsPerBin))
    countsFile.close()

main()