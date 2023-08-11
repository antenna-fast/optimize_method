import numpy as np
import time
import matplotlib.pyplot as plt


# find the minimum of y
# y   = x^2 + x + 1
# y'  = 2x + 1
# y'' = 2

# iteration: x = x - f(x)'/f''(x)

# gen function sample data
ori_x = []
ori_y = []
for i in range(-100, 100):
    ori_x.append(i)
    ori_y.append(i**2 + i + 1)


x0 = 100
y0 = x0**2 + x0 + 1

iter_x = []
iter_y = []

iter_x.append(x0)
iter_y.append(y0)

# init g and gg
g = 2*x0 + 1  # f'(x0)
gg = 2        # f''(x0)

while abs(g) > 0.001:
    # update partial_x
    g = 2*x0 + 1  # f'(x0)

    # update two order partial, well, in this case it is constant
    gg = 2  # f''(x0)

    # update x0: this is essential of Newton method
    # it equals to get the zero point of first order partial
    x0 = x0 - g/gg

    print("g: {}".format(g))

    y0 = x0**2 + x0 + 1

    iter_x.append(x0)
    iter_y.append(y0)

y = x0**2 + x0 + 1
print('\nx_final is {0}, and min_y is {1}'.format(x0, y))


plt.scatter(ori_x, ori_y, c="r")
plt.scatter(iter_x, iter_y, c="b")
plt.show()
