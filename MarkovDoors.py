from __future__ import division
import random

def doors(ndays, nwalks):
    door1_tot = 0
    door2_tot = 0
    door3_tot = 0
    for day in range(ndays):
        for walk in range(nwalks):
            door1 = 0
            door2 = 0
            door3 = 0
            prob = random.random()
            door = random.randrange(1,4)
            while door == 1:
                if prob < 0.50:
                    # door = 1
                    door1 += 1
                elif prob >= 0.50:
                    # door = 2
                    door2 += 1
                break
            while door == 2:
                if prob < 1/3:
                    # door = 1
                    door1 += 1
                elif 1/3 <= prob < 2/3:
                    # door = 2
                    door2 += 1
                elif prob <= 2/3:
                    # door = 3
                    door3 += 1
                break
            while door == 3:
                if prob < 0.50:
                    # door = 3
                    door3 += 1
                elif prob >= 0.50:
                    # door = 2
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



# def doors2(nwalks):
#     for walk in range(nwalks):
#         door1 = 0
#         door2 = 0
#         door3 = 0
#         door = random.randrange(1, 4)
#         prob = random.random()
#         while door == 1:
#             if prob < 0.50:
#                 door = 1
#                 door1 += 1
#             else:
#                 door = 2
#                 door2 += 1
#             door = random.randrange(1,4)
#
#             break
#         while door == 2:
#             if prob < 1/3:
#                 door = 1
#                 door1 += 1
#             elif 1/3 <= prob < 2/3:
#                 door = 2
#                 door2 += 1
#             else:
#                 door = 3
#                 door3 += 1
#             door = random.randrange(1,4)
#             break
#         while door == 3:
#             if prob < 0.50:
#                 # door = 3
#                 door3 += 1
#             else:
#                 # door = 2
#                 door2 += 1
#             door = random.randrange(1,4)
#             break
#         # door1_tot += door1
#         # door2_tot += door2
#         # door3_tot += door3
#         total = door1 + door2 + door3
#     print(total)
#     # frac1 = door1_tot/total
#     # frac2 = door2_tot/total
#     # frac3 = door3_tot/total
#     return frac1, frac2, frac3



