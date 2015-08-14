from __future__ import division
import random

# DONE
def doors(nwalks):
    door1_tot = 0
    door2_tot = 0
    door3_tot = 0
    for walk in range(nwalks):
        door1 = 0
        door2 = 0
        door3 = 0
        prob = random.random()
        door = random.randrange(1,4)
        while door == 1:
            if prob < 0.50:
                door1 += 1
                break
            elif prob >= 0.50:
                door2 += 1
                break
        while door == 2:
            if prob < 1/3:
                door1 += 1
                break
            elif (1/3) <= prob < (2/3):
                door2 += 1
                break
            elif prob >= 2/3:
                door3 += 1
                break
        while door == 3:
            if prob < 0.50:
                door3 += 1
                break
            elif prob >= 0.50:
                door2 += 1
                break
        door1_tot += door1
        door2_tot += door2
        door3_tot += door3
    total = door1_tot + door2_tot + door3_tot
    print(total)
    frac1 = door1_tot/total
    frac2 = door2_tot/total
    frac3 = door3_tot/total
    return frac1, frac2, frac3



