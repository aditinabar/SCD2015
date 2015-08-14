from __future__ import division

__author__ = 'naditi'

#import packages
import math
import numpy as np
import matplotlib.pyplot as plt



# Collection of equations to test the functions below
def f_1(x, y):
    return 7*y**2*x**3

def f_2(x, y):
    return math.cos(x) + math.sin(y)


## oregonator differential equation
def oregonator(t, x):
    x_dot = np.zeros((3, 1))
    x_dot[0] = 77.27 * (x[1] - x[0] * x[1] + x[0] - 8.375e-06*(x[0]**2))
    x_dot[1] = (x[2] - x[0]*x[1] - x[1]) / 77.27
    x_dot[2] = 0.161*(x[0] - x[2])
    return x_dot.T[0]

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
    x_out[1] = x*(rho - z) -y
    x_out[2] = x*y - beta*z
    return x_out.T[0]


# unused at the moment!
# euler step and iteration
def euler_step(f, start_time, start_position):
    y_prime = f(start_time, start_position)
    return y_prime

####### NOTE: all functions are plotting two separate lines for the x and y variables vs
####### using them as the coordinates.
# Euler for scalars
def euler_iterate(f, t_0, end_time, y_0, h, output):
    n = int((end_time - t_0)/h)
    N = n+1
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
        plt.plot(t, y, 'r-')
        plt.show()

#DONE
# RK4 for scalars
def rk_iterate(f, start_time, start_position, h, output):
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
        plt.plot(t, y, 'b-')
        plt.show()
    else:
        pass


def fun_matrix(t,x,y,z):
    return 2*x + t
    return 3*xy
    return x-z

#DONE
# Euler for vectors
def vector_euler(f, t_0, end_time, y_0, h, output):
    n = int((end_time - t_0)/h)
    N = n+1
    t = np.zeros((N, 1))
    t[0] = t_0
    dy = len(y_0)
    y = np.zeros((N, dy))
    y[0] = y_0
    y_x = []
    y_y = []
    y_z = []
    for i in range(0, n-1):
        y[i+1] = y[i] + h*f(t[i], y[i])
        t[i+1] = t[i] + h
    for i in range(N):
        y_x.append(y[i][0])
        y_y.append(y[i][1])
        y_z.append(y[i][2])
    print("Length of y_x is" + str(len(y_x)))
    print("Length of t is" + str(len(t)))
    if output == "print":
        print(t)
        print(y)
    elif output == "plot":
        plt.plot(y_x, 'g-', y_y, 'r-', y_z, 'b-')
        plt.show()

#DONE
# RK4 for vectors
# only takes vectors with 2 and 3 elements
def vector_rk4(f, t_0, t_fin, y_0, h, output):
    steps = int((t_fin - t_0)/h)
    dy = len(y_0)
    y_0a = np.array(y_0, dtype='int64', ndmin=2)
    h_last = (t_fin - t_0) - steps*h
    if h_last == 0:
        t = np.zeros((steps+1, 1))
        y = np.zeros((steps+1, dy))
    elif h_last != 0:
        t = np.zeros((steps+2, 1))
        y = np.zeros((steps+2, dy))
    t[0] = t_0
    y[0] = y_0a
    y_x = []
    y_y = []
    y_z = []
    for i in range(t.shape[0]-2):
        k_1 = f(t[i], y[i])
        k_2y = y[i] + (h/2)*k_1
        k_2 = f(t[i] + h/2, k_2y)
        k_3y = y[i] + (h/2)*k_2
        k_3 = f(t[i] + h/2, k_3y)
        k_4y = y[i] + h*k_3
        k_4 = f(t[i] + h, k_4y)
        y[i+1] = (y[i] + ((h/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)))
        t[i+1] = t[i] + h
    if y.shape[1] == 2:
        for coord in range(t.shape[0]):
            y_x.append(y[coord][0])
            y_y.append(y[coord][1])
    else:
        for i in range(t.shape[0]):
            y_x.append(y[i][0])
            y_y.append(y[i][1])
            y_z.append(y[i][2])
    if h_last == 0:
        pass
    else:
        k_1 = f(t[t.shape[0]-2], y[t.shape[0]-2])
        k_2y = y[t.shape[0]-2] + (h_last/2)*k_1
        k_2 = f(t[t.shape[0]-2] + h_last/2, k_2y)
        k_3y = y[t.shape[0]-2] + (h_last/2)*k_2
        k_3 = f(t[t.shape[0]-2] + h_last/2, k_3y)
        k_4y = y[t.shape[0]-2] + h_last*k_3
        k_4 = f(t[t.shape[0]-2] + h_last, k_4y)
        y[y.shape[0]-1] = (y[t.shape[0]-2] + ((h_last/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)))
        t[t.shape[0]-1] = t[t.shape[0]-2] + h_last
    if y.shape[1] == 2:
        if output == "print":
            print(t)
            print(y)
        elif output == "plot":
            plt.plot(y_x, y_y)
            plt.show()
        elif output == "both":
            plt.plot(y_x, y_y)
            plt.show()
            print(t)
            print(y)
        else:
            pass
    else:
        if output == "print":
            print(t)
            print(y)
        elif output == "plot":
            fig = plt.figure()
            axis = fig.add_subplot(111, projection='3d')
            axis.plot(y_x, y_y, y_z)
            plt.show()
        elif output == "both":
            fig = plt.figure()
            axis = fig.add_subplot(111, projection='3d')
            axis.plot(y_x, y_y, y_z)
            plt.show()
            print(t)
            print(y)
        else:
            pass
