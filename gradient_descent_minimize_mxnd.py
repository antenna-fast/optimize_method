import numpy as np
import matplotlib.pyplot as plt

# TODO

# gradient decent for object function: 
# h1 = x^2 + x + y^2 + 8y + 4*z^2 + 5*z + 1
# h2 = 3*x^2 + + 4*y^2 + 8y + 5*z + 1

# gen function sample data
# ori_x = []
# ori_y = []
# for i in range(-100, 100):
#     ori_x.append(i)
#     ori_y.append(i**2 + i + 1)

# initial point
x0 = np.array([100, 100, 100])

# h = x^2 + x + y^2 + 8y + 4*z^2 + 5*z + 1
lama = 0.1   # lambda (or learning rate)

# initial gradient
gx = 2*x0[0] + 1 
gy = 2*x0[1] + 8
gz = 8*x0[2] + 5
g = np.array([gx, gy, gz])

# Jacobin matrix dim: 2x3
J = np.array(
    [[2*x0[0]+1, 2*x0[1]+8, 8*x0[2] + 5],
     [6*x0[0],  8*x0[1] + 8, 5]
     ])

# iter_x = []

# y0 = x0**2 + x0 + 1
# iter_x.append(x0)
# iter_y.append(y0)

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

    # iter_x.append(x0)
    # iter_y.append(y0)

# plt.scatter(ori_x, ori_y, c="r")
# plt.scatter(iter_x, iter_y, c="b")
# plt.show()

h = x0[0]**2 + x0[0] + x0[1]**2 + 8*x0[1] + 4*x0[2]**2 + 5*x0[2] + 1

print('\nx_final is {0}, and min_y is {1}'.format(x0, h))
