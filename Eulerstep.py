from __future__ import division

__author__ = 'naditi'

import math
import decimal
import pylab as pl
import numpy as np

# #Enter function to test
def f_1(x, y):
    return 7*y**2*x**3
    # y(2) = 3
# y' = t*y
# y(t) = ae^(1/2*t^2)
# y' = -2y
# y(t) = a*e^(-2t)
# y' = ty
# y(t) = a*e^(-1/2 t^2)

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
# getting mad about n. find out why.
def euler_iterate(f, t_0, end_time, y_0, h, output):
    # step = (end_time - t_0)/n
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
        pl.plot(t,y,'go')
        pl.show()


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

# eulerstep_iterate(f_euler(x), -4, 1, 0, 1000)

# eulerstep_iterate(lambda x, y: math.cos(x) + math.sin(y), 0, 1, 1, 1000)

def fun_matrix(t,x,y,z):
    return 2*x + t
    return 3*xy
    return x-z

## oregonator differential equation
def oregonator(t, x):
    x_dot = np.zeros((3, 1), dtype= np.float64)
    print("b")
    print(x[1])
    x_dot[0] = 77.27 * (x[1] - x[0] * x[1] + x[0] - 8.375e-06*(x[0]**2))
    print("c")
    print(x_dot[0])
    x_dot[1] = (x[2] - x[0]*x[1] - x[1]) / 77.27
    x_dot[2] = 0.161*(x[0] - x[2])
    # x_dot.shape = (3,1)
    print(x_dot)
    return x_dot


def vector_ode(f, t_0, t_fin, y_0, h):
    steps = int((t_fin - t_0)/h)
    # N = n+1
    dy = len(y_0)
    print(len(y_0))
    y_0a = np.array(y_0, ndmin=2)
    t = np.zeros((steps, 1))
    t[0] = t_0
    y = np.zeros((steps, dy))
    print("y[0] shape")
    print(y[0].shape)
    print("y_0a")
    print(y_0a)
    print("y_0 shape:")
    print(y_0a.shape)
    y[0] = y_0a
    print("y[0]")
    print(y[0])
    print("y shape:")
    print(y.shape)
    # print("t shape:")
    # print(t.shape)
    for i in range(steps):
        print("a: y[i]")
        print(y[i])
        k_1 = f(t[i], y[i])
        print("d")
        print(k_1)
        print(y[i])
        print("y[i] + h/2 + k_1:")
        print(y[i] + h/2*k_1)
        # d = y[i] + h/2*k_1
        # print("d[i]")
        # print(d[i])
        k_2y = y[i] + (h/2)*k_1
        k_2 = f(t[i] + h/2, k_2y[i])
        print("e")
        print("HELLO WORLD HELLO WORLD HELLO WORLD HELLO WORLD")
        k_3y = y[i] + (h/2)*k_2
        k_3 = f(t[i] + h/2, k_3y[i])
        print("f")
        print("ffffffff")
        k_4y = y[i] + h*k_3
        k_4 = f(t[i] + h, k_4y[i])
        print("k_4")
        print(k_4)
        print(k_4.shape)
        print(k_4[0])
        print("shape y[i] =")
        print(y[i].shape)
        print("shape h/6.... ")
        print(((h/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)).shape)
        y[i+1] = y[i] + ((h/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)) #make sure these two parts have the same shape
        print("y[0]")
        print(y[0])
        print("y[1]")
        print(y[1])
        t[i+1] = t[i] + h
    print(t)
    print(y)

# decimal.Decimal(10*0.01536)

np.array([3,4,5],)