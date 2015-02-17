__author__ = 'adriana'

import os
import sys
from itertools import islice

def main():
    if len(sys.argv) < 3:
        print "Need input file to grep in and input file containing what to grep for"
        exit(1)
    words = open(sys.argv[1], "r")
    text = open(sys.argv[2], "w")

    # hash text
    text = {}
    while True:
        next_4_lines = list(islice(inFile, 4))
        if not next_4_lines:
            break

        header = next_4_lines[0].split()
        ID = header[0]
        sequence = next_4_lines[1].strip() + next_4_lines[2].strip() + next_4_lines[3].strip()
        text[sequence] = ID

    for line in words:
        word = line.strip()
        if word in text:
            print word, text[word]

main()
