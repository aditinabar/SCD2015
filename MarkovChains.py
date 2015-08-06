from __future__ import division
import sys

import numpy as np
import numpy.random as npr
from numpy import __all__
import matplotlib.pyplot as plt
import math


def test(n):
    flips = []
    for i in range(1, n+1):
        flips.append(npr.binomial(1, 0.5, 1)[0])
    print(flips)
    print(flips[len(flips)-1])
    if flips[len(flips)-1] == 1:
        print("True")
    else:
        print("False")


# flip = npr.binomial(1, 0.5, 1)
# print(flip)
# print(flip[0])
# print(type(flip))

# Total_fail = sum(flip == 0)/1000
# print(Total_fail)

#write a function that starts with coin clips

# def hht():
#     flips = []
#     while True:
#         global nflips
#         nflips = 0
#         for i in range(3):
#             flips.append(npr.binomial(1, 0.5, 1)[0])
#         print(flips)
#         if flips[len(flips)-1] == 0 & flips[len(flips)-2] == 1 & flips[len(flips)-3] == 1:
#             nflips = len(flips)
#             break
#         else:
#             hht()
#     print(nflips)

def hht_2(nruns):
    runs = np.zeros((1, nruns))[0]
    # print(runs)
    nflips = 1
    sum_flips = 0
    for i in range(nruns):
        flips = []
        for i in range(3):
            flips.append(npr.binomial(1, 0.5, 3)[i])
        if flips[len(flips)-1] == 0 and flips[len(flips)-2] == 1 and flips[len(flips)-3] == 1:
            runs[i] = nflips
            sum_flips += nflips
            print(runs)
            break
            # sys.exit()
        else:
            flips.append(npr.binomial(1, 0.5, 1)[0])
            nflips += 1
            # flips.append(npr.binomial(1, 0.5, 1)[0])
            # nflips += len(flips)
    print("Flips")
    print(flips)
    print("runs")
    print(runs)
    print("SUM")
    print(sum_flips)

def hht_3(nruns):
    flips = []
    # runs = np.empty((1, nruns))[0]
    first_three = npr.binomial(1, 0.5, 3)
    # flips.append()
    for i in range(first_three.shape[0]):
        flips.append(first_three[i])
    print(flips)
    print("Hello world")
    nflips = 3
    sum_flips = 0
    for i in range(nruns):
        if flips[len(flips)-1] == 0:
            if flips[len(flips)-2] == 1:
                if flips[len(flips)-3] == 1:
                    sum_flips += nflips
                    break
                else:
                    del flips[0]
                    flips.extend([npr.binomial(1, 0.5, 1)[0]])
            else:
                del flips[0]
                flips.extend([npr.binomial(1, 0.5, 1)[0]])
        else:
            del flips[0]
            flips.extend([npr.binomial(1, 0.5, 1)[0]])
    print(sum_flips)


def func():
    for i in range(5):
        flips = []
        for i in range(3):
            flips.append(npr.binomial(1, 0.5, 3)[i])
        if flips[len(flips)-1] == 0:
            flips.extend([npr.binomial(1, 0.5, 1)[0]])
        print(flips)





        # while (flips[len(flips)-1] == 0 and flips[len(flips)-2] == 1 and flips[len(flips)-3] == 1) == False:
        #     del flips[0]
        #     flips.extend([npr.binomial(1, 0.5, 1)[0]])
        #     print(flips)
        # if flips[len(flips)-1] == 0 and flips[len(flips)-2] == 1 and flips[len(flips)-3] == 1:
        #     sys.exit()
        #

