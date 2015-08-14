from __future__ import division
import random

def contagious(nruns):
    total = 0
    for run in range(nruns):
        prob = random.random()
        count = 0
        while prob != 1:
            if prob <= 0.05:
                count += 1
                prob = random.random()
            elif 0.05 < prob <= 0.2:
                count += 1
                prob = random.random()
            elif 0.2 < prob <= 1:
                count += 1
                total += count
                prob = 1
    print(total)
    avg = total/nruns
    return avg








for i in range(3):
    dig = random.random()
    print(dig)
    while dig < 0.5:
        dig += 0.1
        print(dig)




















