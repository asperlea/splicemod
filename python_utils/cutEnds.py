__author__ = 'adriana'

import sys

def main():
    if len(sys.argv) < 3:
        print "Need input and output files"
        exit(1)
    inFile = open(sys.argv[1], "r")
    outFile = open(sys.argv[2], "w")

    for line in inFile:
        cleanLine = line.strip()
        pos = cleanLine.find("TTAATTAA")
        exon = cleanLine[:pos]
        outFile.write(exon + "\n")

    outFile.close()

main()