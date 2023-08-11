# gradient decent for object function: 
# h = x^2 + x + y^2 + 8y - 4*z^2 + 5*z + 1

import numpy as np
import matplotlib.pyplot as plt

# initial point
x0 = np.array([100, 100, 100])

# h = x^2 + x + y^2 + 8y + 4*z^2 + 5*z + 1
lama = 0.1   # lambda (or learning rate)

# initial gradient
gx = 2*x0[0] + 1 
gy = 2*x0[1] + 8
gz = 8*x0[2] + 5
g = np.array([gx, gy, gz])

# y0 = x0**2 + x0 + 1

# perform gradient decent
print_counter = 0
while abs(np.linalg.norm(g)) > 0.00001:   # if partial x > epsilon(a very very small value), iterate it
    # update partial xyz
    gx = 2*x0[0] + 1 
    gy = 2*x0[1] + 8
    gz = 8*x0[2] + 5
    g = np.array([gx, gy, gz])

    x0 = x0 - lama*g    # update x0

    if(print_counter%10 == 0):
        h = x0[0]**2 + x0[0] + x0[1]**2 + 8*x0[1] + 4*x0[2]**2 + 5*x0[2] + 1
        print("iter {} gradient: {} fx={}".format(print_counter, np.linalg.norm(g), h))

    print_counter += 1

h = x0[0]**2 + x0[0] + x0[1]**2 + 8*x0[1] + 4*x0[2]**2 + 5*x0[2] + 1

print('\nx_final is {0}, and min_y is {1}'.format(x0, h))
