from __future__ import division
import numpy.random as npr

# DONE
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
    print(sum_flips)
    avg = float(sum_flips/nruns)
    return avg


