from __future__ import division
import sys


import numpy.random as npr




# flip = npr.binomial(1, 0.5, 1)
# print(flip)
# print(flip[0])
# print(type(flip))

# Total_fail = sum(flip == 0)/1000
# print(Total_fail)

#write a function that starts with coin clips

def hht(nruns):
    sum_flips = 0
    for i in range(nruns):
        flips = []
        for j in range(3):
            flips.append(npr.binomial(1, 0.5, 3)[j])
        while not(flips[len(flips)-1] == 0 and flips[len(flips)-2] == 1 and flips[len(flips)-3] == 1):
            flips.extend([npr.binomial(1, 0.5, 1)[0]])
        else:
            pass
        sum_flips += len(flips)
        # print(flips) #; print(len(flips))
        # print(sum_flips)
    print(sum_flips)
    avg = float(sum_flips/nruns)
    return avg



def hth(nruns):
    sum_flips = 0
    for i in range(nruns):
        flips = []
        for j in range(3):
            flips.append(npr.binomial(1, 0.5, 3)[j])
        while not(flips[len(flips)-1] == 1 and flips[len(flips)-2] == 0 and flips[len(flips)-3] == 1):
            flips.extend([npr.binomial(1, 0.5, 1)[0]])
        else:
            pass
        sum_flips += len(flips)
        # print(flips) #; print(len(flips))
        # print(sum_flips)
    print(sum_flips)
    avg = float(sum_flips/nruns)
    return avg




        # while (flips[len(flips)-1] == 0 and flips[len(flips)-2] == 1 and flips[len(flips)-3] == 1) == False:
        #     del flips[0]
        #     flips.extend([npr.binomial(1, 0.5, 1)[0]])
        #     print(flips)
        # if flips[len(flips)-1] == 0 and flips[len(flips)-2] == 1 and flips[len(flips)-3] == 1:
        #     sys.exit()
        #

