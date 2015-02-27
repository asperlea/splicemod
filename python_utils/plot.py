__author__ = 'adriana'

import numpy as np
import pylab as P
from collections import defaultdict
from itertools import islice


#binList = ["mut2", "mut5", "mut8", "mut9", "mut6", "mut10", "mut11", "mut12"] # mutant
binList = ["nat2", "nat5", "nat8", "nat9", "nat6", "nat10", "nat11", "nat12"] #natural

f_j = [0.1142340965, 0.02279123093, 0.09818295522, 0.0403015669, 0.06507313345, 0.1603029566, 0.1568286836, 0.1927874092] #natural
#f_j = [0.1460297264, 0.09276502227, 0.1159755557, 0.05147186398, 0.03581824841, 0.1537023114, 0.09926165828, 0.09509764232] # mutant

'''
Example of line in countsPerbin_*.txt
AAAAAAAAAAACCCACCTTGAAAAGTCTCCCTCTTACTTTCTTTCAGGTTCCTTTTTTGCCAGGAGATTCAGACCTTGATCAGCTAACAAGAATATTTGAAACTTTGGGCACACCAACTGAGGAACAGTGGCCGGTAAGCCTTTATGCATTTTCTTTGAAATGTAATTAG
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.184046614947161e-06]
'''

def main():
    dataFile = open("countsPerbin_nat.txt", "r")
    coverageFile = open("coveragePerbin.txt", "r")
    seqs = open("sequencesForPlot_nat.txt", "w")
    matrix = open("matrixForHeatmap_mut.nat", "w")
    data = []
    binTotals = defaultdict(int)
    numBins = 8
    a_i_j = []

    while True:
        next_2_lines = list(islice(dataFile, 2))
        if not next_2_lines:
            break
        n2l_cvg = list(islice(coverageFile, 2))
        if not n2l_cvg:
            break

        sequence = next_2_lines[0]
        counts = next_2_lines[1].strip("[]\n").split(", ")
        coverage = n2l_cvg[1].strip("[]\n").split(", ")
        a_i = []
        total_in_all_bins = 0
        for j in range(numBins):
            total_in_all_bins += (float(counts[j]) * (f_j[j]))
        if total_in_all_bins != 0:
            for j in range(numBins):
                a_i.append(float(counts[j]) * f_j[j] / total_in_all_bins)
            matrix.write(str(a_i[0]))
            for i in range(1, len(a_i)):
                matrix.write("," + str(a_i[i]))
            matrix.write("\n")
            if a_i[6] > 0.9 and coverage[6] > 20:
                print sequence.strip()
            a_i_j.append(a_i)
            seqs.write(sequence)

main()