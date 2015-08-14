from Eulerstep import *

import numpy as np


#simulates the sin/cos function
def func(t, vector):
    y_out = np.zeros((2, 1))
    x = -vector[1]
    y = vector[0]
    y_out[0][0] = x
    y_out[1][0] = y
    return y_out.T[0]



# vector_euler(lorenz, 0, 1, [1, 1, 1], 0.05, "plot")
# vector_euler(lorenz, 0, 1, [1, 1, 1], 0.05/2, "plot")
# vector_euler(lorenz, 0, 1, [1, 1, 1], 0.05/4, "plot")
# vector_euler(lorenz, 0, 1, [1, 1, 1], 0.05/8, "plot")

# vector_rk4(f, t_0, t_fin, y_0, h, output)
vector_rk4(func, 0, 1, [1, 2], 0.05, "hi")
vector_rk4(func, 0, 1, [1, 2], 0.05/2, "hi")
vector_rk4(func, 0, 1, [1, 2], 0.05/4, "hi")

# vector_rk4(lorenz, 0, 10, [1, 1, 1], 0.05, "plot")
# vector_rk4(lorenz, 0, 1, [1, 1, 1], 0.05/2, "plot")
# vector_rk4(lorenz, 0, 1, [1, 1, 1], 0.05/4, "plot")
# vector_rk4(lorenz, 0, 1, [1, 1, 1], 0.05/8, "plot")

# rk_iterate(f, start_time, start_position, h, output)
