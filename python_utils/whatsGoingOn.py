__author__ = 'adriana'

import sys
from collections import defaultdict

def main():
    readsFile = open(sys.argv[1], "r")
    alignmentFile = open(sys.argv[2], "r")
    numMaps = defaultdict(int)

    alignmentDict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: "")))


    print "Creating dictionary from alignment file . . ."
    for line in alignmentFile:
        if line[0] != '@':
            data = line.split()
            read = data[9]
            if data[2] != "*":
                exon = data[2].split("-")[0]
                mutant = data[2].split("-")[1]
                MDZ = data[18]
                alignmentDict[read][exon][mutant] = MDZ
    print "Done."

    for line in readsFile:
        read = line.split()[1]
        count = int(line.split()[0])

        if count > 50 and len(read) == 170:
            print read
            for exon in alignmentDict[read]:
                print exon
                for mutant in alignmentDict[read][exon]:
                    print mutant, alignmentDict[read][exon][mutant]

main()
