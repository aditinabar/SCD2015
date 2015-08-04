from __future__ import division

__author__ = 'naditi'

#import packages
import math
import decimal
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


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

## oregonator differential equation
def oregonator(t, x):
    x_dot = np.zeros((3, 1))
    x_dot[0] = 77.27 * (x[1] - x[0] * x[1] + x[0] - 8.375e-06*(x[0]**2))
    x_dot[1] = (x[2] - x[0]*x[1] - x[1]) / 77.27
    x_dot[2] = 0.161*(x[0] - x[2])
    return x_dot.T

global sigma, rho, beta

rho = 28.
sigma = 10.
beta = 8./3
def lorenz(t, x_init):
    x_out = np.zeros((3,1))
    x = x_init[0]
    y = x_init[1]
    z = x_init[2]
    x_out[0] = sigma*(y - x)
    x_out[1] = x*(rho - z)
    x_out[2] = x*y - beta*z
    return x_out.T[0]


# unused at the moment!
# euler step and iteration
def euler_step(f, start_time, start_position):
    y_prime = f(start_time, start_position)
    return y_prime

# Euler for scalars
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

# RK4 for scalars
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

# RK4 for vectors
def vector_rk4(f, t_0, t_fin, y_0, h, output):
    steps = int((t_fin - t_0)/h)
    dy = len(y_0)
    y_0a = np.array(y_0, dtype='int64', ndmin=2)
    t = np.zeros((steps, 1))
    t[0] = t_0
    global y_x
    global y_y
    global y_z
    y_x = []
    y_y = []
    y_z = []
    y = np.zeros((steps, dy))
    y[0] = y_0a
    for i in range(steps-1):
        k_1 = f(t[i], y[i])
        k_2y = y[i] + (h/2)*k_1
        k_2 = f(t[i] + h/2, k_2y)
        k_3y = y[i] + (h/2)*k_2
        k_3 = f(t[i] + h/2, k_3y)
        k_4y = y[i] + h*k_3
        k_4 = f(t[i] + h, k_4y)
        y[i+1] = (y[i] + ((h/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)))
        t[i+1] = t[i] + h
        # print("Done" + str(i)+ "times")
    print(y[1])
    print(y[1][1])
    print(y.shape)
    print(type(y))
    for i in range(y.shape[0]):
        y_x.append(y[i][0])
        y_y.append(y[i][1])
        y_z.append(y[i][2])
    print(y_x[0:11])
    print(y[1:11])
    # print(y_y)
    # print(y_z)
    if output == "print":
        print(t)
        print(y)
    elif output == "plot":
        fig = plt.figure()
        axis = fig.add_subplot(111, projection='3d')
        axis.plot(y_x, y_y, y_z)
        plt.show()

vector_rk4(lorenz, 0, 50, [4, 1.1, 4], 0.05, "plot")
