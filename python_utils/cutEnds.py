__author__ = 'adriana'

import sys

def main():
    if len(sys.argv) < 3:
        print "Need input and output files"
        exit(1)
    inFile = open(sys.argv[1], "r")
    outFile = open(sys.argv[2], "w")

    oligoLengths = []
    idx = 1
    for line in inFile:
        cleanLine = line.strip()
        pos = cleanLine.find("TTAATTAA")
        oligo = cleanLine[:pos]
        outFile.write(">oligo" + str(idx) + "\n")
        outFile.write(oligo + "\n")
        oligoLengths.append(len(oligo))
        idx += 1
    print "Average oligo length was: ", sum(oligoLengths) / float(len(oligoLengths))

    outFile.close()

main()