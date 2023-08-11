# gradient decent for object function: 
# y = x^2 + x + 1

import numpy as np
import matplotlib.pyplot as plt


# gen function sample data
ori_x = []
ori_y = []
for i in range(-100, 100):
    ori_x.append(i)
    ori_y.append(i**2 + i + 1)


x0 = 100       # start with x0

lama = 0.1   # lambda (or learning rate)
g = 2*x0 + 1 # initial gradient

iter_x = []
iter_y = []

y0 = x0**2 + x0 + 1
iter_x.append(x0)
iter_y.append(y0)

# perform gradient decent
print_counter = 0
while abs(g) > 0.00001:   # if partial x > epsilon(a very very small value), iterate it
    g = 2*x0 + 1        # update partial x
    x0 = x0 - lama*g    # update x0

    if(print_counter%10 == 0):
        y = x0**2 + x0 + 1
        print("iter {} gradient: {} fx={}".format(print_counter, g, y))
    print_counter += 1

    y0 = x0**2 + x0 + 1
    iter_x.append(x0)
    iter_y.append(y0)

plt.scatter(ori_x, ori_y, c="r")
plt.scatter(iter_x, iter_y, c="b")
plt.show()

y = x0**2 + x0 + 1
print('\nx_final is {0}, and min_y is {1}'.format(x0, y))
