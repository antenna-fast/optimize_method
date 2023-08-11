# gradient decent for object function: 
# h = theta1 * x1 + theta2 * x2 + theta3 * x3
# we will give a list of [X, y] to train this model's parameter theta

# cost function: 
# residual = h(Theta, xi) - yi
# cost = 1/2 * residual^2 = 0.5 * (h(Theta, xi) - yi)^2

# adjust theta value to minimize cost

# TODO: not coverage at some init position!

import numpy as np
import matplotlib.pyplot as plt

import random

# gt theta: 
theta = np.array([2, 3, 4])

# generate train data
data = []
for x1 in range(-15, 10):
    for x2 in range(-15, 10):
        for x3 in range(-5, 10):
            y = theta[0] * x1 + theta[1] * x2 + theta[2] * x3
            data.append([x1, x2, x3, y])

# perform gradient descent
lama = 0.001
theta_init = np.array([5.5, 13.9, 4.3])
for d in data[:550]:
    d = random.choice(data)
    x = d[:3]
    y = d[3]

    res = theta_init[0] * x[0] + theta_init[1] * x[1] + theta_init[2] * x[2]
    cost = 0.5 * (y - res) * (y - res)

    partial_theta_1 = (res - y) * x[0]
    partial_theta_2 = (res - y) * x[1]
    partial_theta_3 = (res - y) * x[2]

    theta_init[0] = theta_init[0] - lama * partial_theta_1
    theta_init[1] = theta_init[1] - lama * partial_theta_2
    theta_init[2] = theta_init[2] - lama * partial_theta_3

    # print(theta_init[0])
    print("cost: ", cost)

print(theta_init)
