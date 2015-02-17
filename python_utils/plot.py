__author__ = 'adriana'

import numpy as np
import pylab as P
from collections import defaultdict

binList = ["nat2", "nat5", "nat8", "nat9", "nat6", "nat10", "nat11", "nat12"]

def main():
    dataFile = open("countsPerbin.txt", "r")
    data = []
    binDict = defaultdict(int)
    numDif = 0

    totalCountsum = 0


    for line in dataFile:
        if line[0] == '[':
            counts = line.strip("[]\n").split(", ")
            numBins = 0
            bins = []
            for i in range(len(counts) - 1):
                bin = int(counts[i])
                if bin != 0 and bin > 1000:
                    numBins += 1
                    bins.append(binList[i])
            if len(bins) == 1:
                binDict[bins[0]] += 1
            top = False
            bottom = False

            if ("nat5" in bins) or ("nat8" in bins) or ("nat9" in bins):
                top = True
            if ("nat10" in bins) or ("nat11" in bins) or ("nat12" in bins):
                bottom = True

            if top and bottom:
                numDif += 1

            data.append(numBins)

    print binDict
    for i in range(9):
        print i, data.count(i)
    print numDif, " in both top and bottom."
    P.hist(data)
    P.savefig("avgCounts.png")
main()