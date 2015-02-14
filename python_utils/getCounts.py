__author__ = 'adriana'

import os
import sys
from collections import defaultdict

def main():
    if len(sys.argv) < 2:
        print "Need input file with unique contigs"
        exit(1)
    countsFile = open("countsPerbin.txt", "w")

    dirlist = ["1-22079057", "2-22079058", "3-22079059", "4-22079060",  "5-22079061", "6-22079062", "7-22079063", "8-22079064", "17-22079073"]
    binContigsDicts = []
    for dirct in dirlist:
        print "dir = ", dirct
        binContigsFile = open(dirct + "/perfectSeqs.txt")
        binContigs = defaultdict(int)
        for line in binContigsFile:
            contig = line.strip()
            binContigs[contig] += 1
        binContigsDicts.append(binContigs)

    contigsFile = open(sys.argv[1], "r") # contigs file
    idx = 0
    for line in contigsFile:
        contig = line.strip()
        countsPerBin = []
        idx += 1
        if idx % 100 == 0:
            print "Done with ", idx, " contigs."
        bidx = 0
        for binDict in binContigsDicts:
            counts = binDict[contig]
            countsPerBin.append(counts)
        countsFile.write(contig+"\n")
        countsFile.write(str(countsPerBin) + "\n")
    countsFile.close()

main()
