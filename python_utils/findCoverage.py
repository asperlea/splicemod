__author__ = 'adriana'

from collections import defaultdict

def main():
    if len(sys.argv) < 2:
        print "Need input file"
    inFile = open(sys.argv[1], "r") # fastq file

    coverage = defaultdict(int)
    while True:
        next_4_lines = list(islice(inFile, 4))
        if not next_4_lines:
            break

        sequence = next_4_lines[1]

        coverage[sequence] += 1

    print "Average coverage is ", sum(coverage.values()) / float(len(coverage.values()))

main()