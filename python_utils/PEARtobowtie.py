__author__ = 'adriana'

import sys
from itertools import islice

def main():
    if len(sys.argv) < 3:
        print "Need input and output files"
        exit(1)
    inFile = open(sys.argv[1], "r") # fastq file
    outFile = open(sys.argv[2], "w")

    while True:
        next_4_lines = list(islice(inFile, 4))
        if not next_4_lines:
            break

        sequence = next_4_lines[1]
        quality = next_4_lines[3]

        oligoLengths = []
        pos = sequence.find("TTAATTAA")
        sequence = sequence[:pos]
        quality = quality[:pos]

        outFile.write(next_4_lines[0])
        outFile.write(sequence)
        outFile.write(next_4_lines[1])
        outFile.write(quality)

        oligoLengths.append(len(sequence))
        print "Average oligo length was: ", sum(oligoLengths) / float(len(oligoLengths))

    outFile.close()

main()