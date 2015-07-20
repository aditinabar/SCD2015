from __future__ import division

__author__ = 'naditi'

import math
import decimal
import pylab as pl

# #Enter function to test
def f_1(x, y):
    return 7*y**2*x**3
    # y(2) = 3
# y' = t*y
# y(t) = ae^(1/2*t^2)

def f_2(x, y):
    return math.cos(x) + math.sin(y)


#print(decimal.getcontext())

# euler step and iteration
def euler_step(f, start_time, start_position):
    y_prime = f(start_time, start_position)
    return y_prime

# euler
def euler_iterate(f, start_time, end_time, start_position, n, output):
    step = (end_time - start_time)/n
    N = n+1
    t = [0]*N
    t[0] = start_time
    y = [0]*N
    y[0] = start_position
    for i in range(0, n-1):
        y[i+1] = y[i] + step*f(t[i], y[i])
        t[i+1] = t[i] + step
    if output == "print":
        print(t)
        print(y)
    elif output == "plot":
        pl.plot(t,y,'go')
        pl.show()

def rk_iterate(f, start_time, end_time, start_position, n, output):
    step = (end_time - start_time)/n
    N = n+1
    t = [0]*N
    t[0] = start_time
    y = [0]*N
    y[0] = start_position
    for i in range(n-1):
        k_1 = f(t[i], y[i])
        k_2 = f(t[i] + step/2, y[i] + step*k_1/2)
        k_3 = f(t[i] + step/2, y[i] + step*k_2/2)
        k_4 = f(t[i] + step, y[i] + step*k_3)
        y[i+1] = y[i] + (step/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)
        t[i+1] = t[i] + step
    if output == "print":
        print(t)
        print(y)
    elif output == "plot":
        pl.plot(t,y,'go')
        pl.show()

#eulerstep_iterate(f_euler(x), -4, 1, 0, 1000)

# eulerstep_iterate(lambda x, y: math.cos(x) + math.sin(y), 0, 1, 1, 1000)


