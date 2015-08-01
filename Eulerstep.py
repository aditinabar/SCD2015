from __future__ import division

__author__ = 'naditi'

#import packages
import math
import decimal
import pylab as pl
import numpy as np

# Collection of equations to test the functions below
def f_1(x, y):
    return 7*y**2*x**3
    # y(2) = 3
# y' = t*y
# y(t) = ae^(1/2*t^2)
# y' = -2y
# y(t) = a*e^(-2t)
# y' = ty
# y(t) = a*e^(-1/2 t^2)
# eulerstep_iterate(f_euler(x), -4, 1, 0, 1000)
# eulerstep_iterate(lambda x, y: math.cos(x) + math.sin(y), 0, 1, 1, 1000)

def f_2(x, y):
    return math.cos(x) + math.sin(y)

def f_3(x, y):
    return -2*y

# unused at the moment!
# euler step and iteration
def euler_step(f, start_time, start_position):
    y_prime = f(start_time, start_position)
    return y_prime

# euler
# works for scalars
def euler_iterate(f, t_0, end_time, y_0, h, output):
    n = int((end_time - t_0)/h)
    N = n+1
    print(N)
    t = [0]*N
    t[0] = t_0
    y = [0]*N
    y[0] = y_0
    for i in range(0, n-1):
        y[i+1] = y[i] + h*f(t[i], y[i])
        t[i+1] = t[i] + h
    if output == "print":
        print(t)
        print(y)
    elif output == "plot":
        pl.plot(t,y,'go')
        pl.show()

# works for scalars
def rk_iterate(f, start_time, end_time, start_position, h, output):
    # step = (end_time - start_time)/n
    # N = n+1
    t = [0]*1001
    t[0] = start_time
    y = [0]*1001
    y[0] = start_position
    for i in range(1000):
        k_1 = f(t[i], y[i])
        k_2 = f(t[i] + h/2, y[i] + h*k_1/2)
        k_3 = f(t[i] + h/2, y[i] + h*k_2/2)
        k_4 = f(t[i] + h, y[i] + h*k_3)
        y[i+1] = y[i] + (h/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)
        t[i+1] = t[i] + h
    if output == "print":
        print(t)
        print(y)
    elif output == "plot":
        pl.plot(t,y,'go')
        pl.show()


def fun_matrix(t,x,y,z):
    return 2*x + t
    return 3*xy
    return x-z

## oregonator differential equation
def oregonator(t, x):
    x_dot = np.zeros((3, 1), dtype= np.float64)
    x_dot[0] = 77.27 * (x[1] - x[0] * x[1] + x[0] - 8.375e-06*(x[0]**2))
    x_dot[1] = (x[2] - x[0]*x[1] - x[1]) / 77.27
    x_dot[2] = 0.161*(x[0] - x[2])
    return x_dot.T

# Runge-Kutta 4 for vectors
def vector_rk4(f, t_0, t_fin, y_0, h):
    steps = int((t_fin - t_0)/h)
    dy = len(y_0)
    print(len(y_0))
    y_0a = np.array(y_0, ndmin=2)
    t = np.zeros((steps, 1))
    t[0] = t_0
    y = np.zeros((steps, dy))
    y[0] = y_0a
    print("y[0]")
    print(y[0])
    for i in range(steps-1):
        k_1 = f(t[i], y[i])
        #print("d")
        k_2y = y[i, np.newaxis] + (h/2)*k_1
        k_2 = f(t[i] + h/2, k_2y[0])
        #print("e")
        k_3y = y[i, np.newaxis] + (h/2)*k_2
        k_3 = f(t[i] + h/2, k_3y[0])
        #print("f")
        #print("ffffffff")
        k_4y = y[i, np.newaxis] + h*k_3
        k_4 = f(t[i] + h, k_4y[0])
        y[i+1, np.newaxis] = (y[i, np.newaxis] + ((h/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)))
        #print("g")
        t[i+1] = t[i] + h
        #print("Done "+str(i+1)+" times.")
    print(t)
    print(y)


