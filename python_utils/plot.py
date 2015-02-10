__author__ = 'adriana'

import numpy as np
import pylab as P

dataFile = open("../weirdExonLengths.txt", "r")
data = []
for line in dataFile:
    length = line.strip()
    if len(length) > 0:
        data.append(float(length))

print data
print min(data)
print max(data)
plot = P.hist(data, 50)
#n, bins, patches = P.hist(data, 50, normed=1, histtype='stepfilled')
#P.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

P.savefig("exonLengths.png")